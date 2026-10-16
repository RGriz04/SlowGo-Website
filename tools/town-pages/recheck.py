#!/usr/bin/env python3
"""Re-check the official sources behind the town and state pages, and keep the check log.

    python3 tools/town-pages/recheck.py                      quarterly run: every published page's sources
    python3 tools/town-pages/recheck.py --page tybee-island  immediate recheck (complaint or official change)
    python3 tools/town-pages/recheck.py --all                published and held pages
    python3 tools/town-pages/recheck.py --dry-run            list what would be fetched, fetch nothing
    python3 tools/town-pages/recheck.py --schedule           only rewrite recheck-schedule.json (+ HUB copy)
    python3 tools/town-pages/recheck.py --mark-verified --url URL [--page SLUG] --note "what was read"
    python3 tools/town-pages/recheck.py --record SLUG URL FILE --note "how it was fetched"

What it does (see README.md in this folder):
  * fetches each unique source URL once (official, sources, map link), politely: one request at a time,
    at least 4 s apart, 20 s apart on the same host, at most 120 requests a run, never Municode or LexisNexis;
  * hashes the bytes (sha256) and the extracted text (HTML tags stripped / pdftotext), and compares the text
    hash with the last hashed row for that page and URL;
  * appends one row per page and URL to check-log.csv:
        page, source_url, fetched (YYYY-MM-DD), sha256, text_sha256, snapshot, result, verified, note
  * rewrites recheck-schedule.json and copies it to ~/Desktop/SlowGo/hub/data/town-rechecks.json.

A page's "Rules checked <date>" (build.py) is the OLDEST of its sources' latest verified rows: every source
was compared at least that recently. A row is verified only when
  * a person (or agent) read the fetched source and compared it with the page (--mark-verified / --record), or
  * an automatic fetch found the text unchanged from a previous VERIFIED row (same text_sha256).
"changed", "new baseline" and failed fetches are never verified, so the date only moves after a real fetch and
comparison. A changed source is listed as "needs read" in the schedule until someone reads it and marks it.
No network use except the fetches above. Doesn't edit pages: rebuild with build.py after a verified recheck.
"""
import csv, datetime, hashlib, html, json, os, re, shutil, subprocess, sys, tempfile, time, urllib.request, urllib.error
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "check-log.csv")
SCHEDULE = os.path.join(HERE, "recheck-schedule.json")
HUB_COPY = os.path.expanduser("~/Desktop/SlowGo/hub/data/town-rechecks.json")
FIELDS = ["page", "source_url", "fetched", "sha256", "text_sha256", "snapshot", "result", "verified", "note"]
UA = "Mozilla/5.0 (compatible; SlowGo-rules-recheck/1.0; +https://slowgoapp.com/cart-rules)"
GAP, HOST_GAP, CAP = 4.0, 20.0, 120
BANNED = ("municode.com", "lexisnexis.com", "lexis.com")     # Ron 2026-10-15/16: no agent reads these
QUARTER_DAYS = 91


def today():
    return datetime.date.today().isoformat()


def read_log():
    if not os.path.exists(LOG):
        return []
    with open(LOG, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_rows(rows):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def page_urls(t):
    """Every official URL a page cites: the official link, its sources and its map link (deduplicated, in order)."""
    out = [t["official"][1]] + [u for _, u in t["sources"]] + ([t["street_map"][1]] if t.get("street_map") else [])
    seen, res = set(), []
    for u in out:
        if u not in seen:
            seen.add(u); res.append(u)
    return res


def text_of(data, ctype, url):
    if data[:5] == b"%PDF-" or "pdf" in ctype:
        if shutil.which("pdftotext"):
            with tempfile.TemporaryDirectory() as d:
                p = os.path.join(d, "f.pdf")
                open(p, "wb").write(data)
                r = subprocess.run(["pdftotext", "-q", p, "-"], capture_output=True)
                s = r.stdout.decode("utf-8", "ignore")
                if s.strip():
                    return re.sub(r"\s+", " ", s).strip()
        return None          # scanned or unreadable PDF: compare bytes only
    s = data.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style|noscript|nav|header|footer|form)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def hashes(data, ctype, url):
    raw = hashlib.sha256(data).hexdigest()
    t = text_of(data, ctype, url)
    return raw, (hashlib.sha256(t.encode("utf-8")).hexdigest() if t is not None else raw)


def last_hashed(log, page, url):
    for r in reversed(log):
        if r["page"] == page and r["source_url"] == url and r["text_sha256"]:
            return r
    return None


def last_verified(log, page, url):
    for r in reversed(log):
        if r["page"] == page and r["source_url"] == url and r["verified"] == "yes":
            return r
    return None


def compare(log, page, url, raw, txt):
    prev = last_hashed(log, page, url)
    pv = last_verified(log, page, url)
    if pv and pv["text_sha256"] == txt:
        return "unchanged since last verified check", "yes"
    if prev is None or not prev["text_sha256"]:
        return "new baseline (not yet compared with the page)", "no"
    if prev["text_sha256"] == txt:
        return "unchanged since last fetch (that fetch wasn't verified)", "no"
    return "CHANGED since last fetch: needs a read", "no"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        return e.code, "", b""
    except Exception as e:   # timeouts, DNS, TLS
        return f"error: {type(e).__name__}", "", b""


def towns():
    sys.path.insert(0, HERE)
    from build import TOWNS
    return TOWNS


def run(selected, dry):
    log = read_log()
    url_pages = {}
    for t in selected:
        for u in page_urls(t):
            url_pages.setdefault(u, []).append(t["slug"])
    urls = list(url_pages)
    done_today = {(r["page"], r["source_url"]) for r in log if r["fetched"] == today() and r["text_sha256"]}
    todo = [u for u in urls if not all((p, u) in done_today for p in url_pages[u])]
    banned = [u for u in todo if any(b in urlparse(u).netloc for b in BANNED)]
    todo = [u for u in todo if u not in banned][:CAP]
    print(f"{len(urls)} unique URLs for {len(selected)} pages; {len(urls) - len(todo) - len(banned)} already fetched today; "
          f"{len(todo)} to fetch; {len(banned)} refused (Municode/LexisNexis)")
    if dry:
        for u in todo:
            print("  ", u)
        return
    last_host, last_any, rows, n = {}, 0.0, [], 0
    for u in todo:
        host = urlparse(u).netloc
        wait = max(last_any + GAP, last_host.get(host, 0) + HOST_GAP) - time.time()
        if wait > 0:
            time.sleep(wait)
        status, ctype, data = fetch(u)
        last_any = last_host[host] = time.time(); n += 1
        if status != 200 or not data:
            res, raw, txt, ver = f"fetch failed ({status})", "", "", "no"
        else:
            raw, txt = hashes(data, ctype, u)
        for p in url_pages[u]:
            if status == 200 and data:
                res, ver = compare(log, p, u, raw, txt)
            rows.append(dict(page=p, source_url=u, fetched=today(), sha256=raw, text_sha256=txt, result=res, verified=ver,
                             note="recheck.py automatic fetch"))
        print(f"  [{n}] {status} {u[:100]} -> {rows[-1]['result']}")
    for u in banned:
        for p in url_pages[u]:
            rows.append(dict(page=p, source_url=u, fetched=today(), result="refused: no agent reads this host", verified="no"))
    append_rows(rows)
    print(f"{n} requests; {len(rows)} log rows appended to {os.path.relpath(LOG)}")


def mark_verified(url, page, note):
    """After a person read the fetched source and compared it with the page: verify today's hashed rows for URL."""
    log = read_log()
    hits = [r for r in log if r["source_url"] == url and r["fetched"] == today() and r["text_sha256"]
            and (page is None or r["page"] == page) and r["verified"] != "yes"]
    pages = sorted({r["page"] for r in hits})
    if not hits:
        sys.exit(f"no unverified row fetched today for {url}{' / ' + page if page else ''}: fetch it first (recheck.py --page ...)")
    rows = []
    for p in pages:
        r = [x for x in hits if x["page"] == p][-1]
        rows.append(dict(r, verified="yes", result="read and compared with the page", note=note))
    append_rows(rows)
    print(f"verified {url} for {len(rows)} page(s): {', '.join(pages)}")


def record(page, url, path, note):
    """Record a source fetched another way (e.g. a host that blocks scripts), read and compared by a person."""
    data = open(path, "rb").read()
    raw, txt = hashes(data, "application/pdf" if data[:5] == b"%PDF-" else "text/html", url)
    append_rows([dict(page=page, source_url=url, fetched=today(), sha256=raw, text_sha256=txt,
                      result="read and compared with the page", verified="yes", note=note)])
    print(f"recorded {url} for {page} ({raw[:12]})")


def page_status(t, log):
    """(checked_date or None, per-source detail) for one page."""
    detail, dates = [], []
    for u in page_urls(t):
        v = last_verified(log, t["slug"], u)
        h = last_hashed(log, t["slug"], u)
        last = next((r for r in reversed(log) if r["page"] == t["slug"] and r["source_url"] == u), None)
        needs = bool(last and last["verified"] != "yes" and (last["result"].startswith("CHANGED") or last["result"].startswith("fetch failed")))
        detail.append(dict(url=u, last_verified=v["fetched"] if v else None, last_fetch=last["fetched"] if last else None,
                           last_result=last["result"] if last else "never checked", needs_read=needs or v is None,
                           hashed=bool(h)))
        dates.append(v["fetched"] if v else None)
    return (None if None in dates or not dates else min(dates)), detail


def checked_date(t, log=None):
    """Used by build.py: the page's 'Rules checked' date (oldest of its sources' latest verified rows)."""
    return page_status(t, read_log() if log is None else log)[0]


def schedule(all_towns, copy=True):
    log = read_log()
    items = []
    for t in all_towns:
        d, det = page_status(t, log)
        due = (datetime.date.fromisoformat(d) + datetime.timedelta(days=QUARTER_DAYS)).isoformat() if d else None
        needs = [x["url"] for x in det if x["needs_read"]]
        status = ("held" if not t["publish"] else
                  "needs read" if needs else
                  "overdue" if due and due < today() else "ok")
        items.append(dict(page=t["slug"], name=re.sub(r"<[^>]+>", "", html.unescape(t["name"])), state=t["state"],
                          kind=t.get("kind", "town"), published=bool(t["publish"]), rules_checked=d, next_due=due,
                          status=status, sources=len(det), needs_read=needs,
                          url=f"https://slowgoapp.com/golf-carts/{t['slug']}" if t["publish"] else None))
    items.sort(key=lambda x: (not x["published"], x["next_due"] or "0000", x["page"]))
    out = dict(updated=today(), cadence="quarterly (every 91 days) + immediately on a complaint or an official change",
               how=("Written by tools/town-pages/recheck.py on drafts/town-pages (SlowGo-Website-drafts). rules_checked = oldest of "
                    "the page's sources' latest verified checks; next_due = rules_checked + 91 days. status: ok / overdue / "
                    "needs read (a source changed, failed, or was never compared) / held (not published)."),
               counts=dict(published=sum(i["published"] for i in items), held=sum(not i["published"] for i in items),
                           needs_read=sum(i["status"] == "needs read" for i in items),
                           overdue=sum(i["status"] == "overdue" for i in items)),
               pages=items)
    s = json.dumps(out, indent=1, ensure_ascii=False) + "\n"
    open(SCHEDULE, "w", encoding="utf-8").write(s)
    if copy:
        try:
            os.makedirs(os.path.dirname(HUB_COPY), exist_ok=True)
            open(HUB_COPY, "w", encoding="utf-8").write(s)
        except OSError as e:
            print(f"(HUB copy not written: {e})")
    print(f"schedule: {out['counts']} -> {os.path.relpath(SCHEDULE)}" + (f" + {HUB_COPY}" if copy else ""))


def arg(name, default=None):
    a = sys.argv
    return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default


if __name__ == "__main__":
    T = towns()
    if "--record" in sys.argv:
        i = sys.argv.index("--record")
        record(sys.argv[i + 1], sys.argv[i + 2], sys.argv[i + 3], arg("--note", "fetched and read by hand"))
    elif "--mark-verified" in sys.argv:
        mark_verified(arg("--url"), arg("--page"), arg("--note", "read and compared by hand"))
    elif "--schedule" not in sys.argv:
        sel = [t for t in T if (t["slug"] == arg("--page")) or (arg("--page") is None and ("--all" in sys.argv or t["publish"]))]
        if not sel:
            sys.exit(f"no page {arg('--page')}")
        run(sel, "--dry-run" in sys.argv)
    if "--dry-run" not in sys.argv:
        schedule(T, copy="--no-hub" not in sys.argv)
