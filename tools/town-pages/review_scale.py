#!/usr/bin/env python3
"""Review list for the town-pages scale-up (2026-10-17): one row per page (published and held) plus one
row per cart-towns database row in FL/GA/AZ that has no page (held, with the reason).

    python3 tools/town-pages/review_scale.py <out_dir> [cart-towns.csv]
Writes <out_dir>/index.html and <out_dir>/review-list.csv. Screenshots are expected in <out_dir>/screens/.
"""
import csv, html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import TOWNS, UPDATED, links_text, is_state, plain
import recheck
LOG = recheck.read_log()
SCHED = {x["page"]: x for x in __import__("json").load(open(recheck.SCHEDULE))["pages"]} if os.path.exists(recheck.SCHEDULE) else {}

OUT = sys.argv[1]
CSV = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    "~/dev/SlowGo-f20-towns/docs/research/cart-towns/cart-towns-2026-10-16.csv")
rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
mtime = __import__("time").strftime("%Y-%m-%d %H:%M", __import__("time").localtime(os.path.getmtime(CSV)))

# The first 10 pages (towns.py) predate the review fields.
FIRST10 = {"captiva": 49, "dunedin": 60, "gulf-breeze": 68, "jekyll-island": 144, "miami-lakes": 92, "mount-dora": 94,
           "pine-island": 106, "st-pete-beach": 122, "st-simons-island": 156, "tybee-island": 158}
PRIO10 = {"captiva": "beach", "dunedin": "beach", "gulf-breeze": "beach", "jekyll-island": "beach", "miami-lakes": "cart-friendly",
          "mount-dora": "cart-friendly", "pine-island": "beach", "st-pete-beach": "beach", "st-simons-island": "beach", "tybee-island": "beach"}
SKIP = {124: "Waits for Ron's Villages ruling (Sumter County).", 127: "Waits for Ron's Villages ruling (The Villages).",
        132: "Waits for Ron's Villages ruling (Wildwood)."}
HOLD_REASON = {
    57: "Dade City: the ordinance copy read is an unsigned agenda draft (adoption not confirmed) and the street-list resolution wasn't found.",
    59: "Destin: the city FAQ was seen only through a search extract, not read on the city site.",
    62: "Fernandina Beach: the city page covers LSVs only; no golf cart rule found.",
    67: "Fruitland Park: only the city's map and 2012 minutes; the current code (ch. 34) wasn't read and the age rule in hand is out of date.",
    70: "Gulfport: the only city source is 2014 council minutes plus the absence of a code section; no current city statement that carts are barred.",
    96: "New Port Richey: the only text is a 2021 draft amendment with old and new wording mixed; current code not confirmed.",
    130: "Walton County: the only source is the county code on Municode (read before the no-Municode rule); can't cite or re-check it. Carts banned from multi-use paths (sec. 20-50) per that read.",
    139: "Darien: the registration form doesn't say where carts may go; the 'under 35 mph' line is from news only and conflicts with the state's 25 mph cap for post-2012 ordinances.",
    159: "Tyrone: the 'streets posted 35 or less' line came from a search summary, not a read of the town page.",
    7: "Green Valley: state statute only (no county or community source). Covered by the Arizona state page.",
    8: "SaddleBrooke: state statute only. Covered by the Arizona state page.",
    9: "Sun City: state statute only, no county or community source beyond it. Covered by the Arizona state page.",
    10: "Sun City Grand (Surprise): state statute only. Covered by the Arizona state page.",
    11: "Sun City West: state statute only, no county or community source beyond it. Covered by the Arizona state page.",
    12: "Sun Lakes: state statute only, no county or community source beyond it. Covered by the Arizona state page.",
}
STATEWIDE = {6, 40, 134}
HELD_WHY = {  # Ron 2026-10-17 afternoon (D19/D20)
    "mount-dora": "Ron hold (D20, 2026-10-17 afternoon). Codex corrections applied anyway (designated-streets framing, LSV definition, no private/gated exemption claim).",
    "captiva": "Ron hold (2026-10-17); file moved out of SlowGo-Launch to tools/town-pages/held (D20).",
    "gulf-breeze": "Ron hold (2026-10-17); file moved out of SlowGo-Launch to tools/town-pages/held (D20).",
    "clearwater": "D19 hold: absence-based (no designation found). Now says 'We haven't verified public-road authorization.' Needs an official source that affirmatively prohibits before it can be a 'no carts' page.",
    "st-augustine-beach": "D19 hold: the city page affirmatively says traditional golf carts may not be operated on public streets (vehicle, roads, jurisdiction named), but it's one web page; ordinance (Municode) unread. Ron decides whether the city page meets D19.",
    "celebration": "D19 hold: the Osceola County policy (live osceola.org copy, Aug 2020) affirmatively bars carts from county roads/sidewalks without an ordinance, but which Celebration streets are county roads (vs CDD/private) is unverified.",
}
PRIO_ORDER = {"beach": 0, "retirement": 1, "cart-friendly": 2, "rider": 3}

e = html.escape
out_rows, covered = [], set()
for t in TOWNS:
    db = t.get("db_row", FIRST10.get(t["slug"]))
    for d in (db if isinstance(db, list) else [db]):
        if d is not None:
            covered.add(d)
    first = db if not isinstance(db, list) else (db[0] if db else None)
    r = rows[first] if isinstance(first, int) else {}
    status = ("draft-publish" if t["publish"] else
              "held: " + ("Ron ruling 2026-10-17, never name New York in public copy" if t.get("never_publish") else
                          HELD_WHY.get(t["slug"]) or t.get("gap") or "Ron hold"))
    out_rows.append(dict(
        page=t["slug"], path=f"/golf-carts/{t['slug']}", state=t["st"], kind="state" if is_state(t) else "town",
        title=plain(t.get("title") or f"Golf Cart Rules in {t['name']}, {t['st']} (Updated {UPDATED})"),
        priority=t.get("prio", PRIO10.get(t["slug"], "")), priority_reason=plain(t.get("prio_note", "")),
        source_quality=t.get("quality", r.get("confidence", "")), source_type=t.get("source_type", r.get("source_type", "")),
        source_url=t["official"][1], checked=(recheck.checked_date(t, LOG) or "never") + (f" ({SCHED[t['slug']]['status']}; next due {SCHED[t['slug']]['next_due']})" if t["slug"] in SCHED else ""),
        honest_gap=plain(t.get("gap", "")), status=status, counted_link=f"/t/{t['slug']}" if (t["publish"] and t.get("counted", True)) else "",
        phone=f"screens/{t['slug']}-phone.png", desktop=f"screens/{t['slug']}-desktop.png"))
for i, r in enumerate(rows):
    if r["state"] not in ("FL", "GA", "AZ", "NY") or i in covered or i in STATEWIDE:
        continue
    reason = SKIP.get(i) or HOLD_REASON.get(i) or (
        f"Thin sourcing: confidence {r['confidence'] or 'none'}"
        + (f" ({r['source_type']})" if r["source_type"] else "; no town or county source found") + ".")
    out_rows.append(dict(page="", path="(no page)", state=r["state"], kind="town", title=r["town_or_community"],
        priority="", priority_reason="", source_quality=r["confidence"] or "none", source_type=r["source_type"],
        source_url=(r["source_url"] or "").split(" ; ")[0], checked=r["source_retrieved"], honest_gap=r["notes"][:300],
        status="held: " + reason, counted_link="", phone="", desktop=""))

def key(x):
    pub = x["status"] == "draft-publish"
    return (0 if pub else 1, x["state"], 0 if x["kind"] == "state" else 1, PRIO_ORDER.get(x["priority"], 9), x["title"])
out_rows.sort(key=key)

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "review-list.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys())); w.writeheader(); w.writerows(out_rows)

pub = [x for x in out_rows if x["status"] == "draft-publish"]
held = [x for x in out_rows if x["status"] != "draft-publish"]
count = lambda xs, st: sum(1 for x in xs if x["state"] == st)
summary = " · ".join(f"{st}: {count(pub, st)} published / {count(held, st)} held" for st in ("FL", "GA", "AZ", "NY"))
samples = [s for s in ("florida", "georgia", "arizona", "new-york") if os.path.exists(os.path.join(OUT, "screens", f"{s}-phone.png"))] + \
          sorted(f[:-10] for f in os.listdir(os.path.join(OUT, "screens")) if f.endswith("-phone.png") and f[:-10] not in ("florida", "georgia", "arizona", "new-york")) \
          if os.path.isdir(os.path.join(OUT, "screens")) else []

def tr(x):
    shots = f"<a href='{x['phone']}'>phone</a> · <a href='{x['desktop']}'>desktop</a>" if x["page"] in samples else ""
    src = f"<a href='{e(x['source_url'])}'>{e(x['source_type'] or 'source')}</a>" if x["source_url"] else e(x["source_type"])
    return (f"<tr><td><strong>{e(x['title'])}</strong><br><code>{e(x['path'])}</code>{'<br><code>' + e(x['counted_link']) + '</code>' if x['counted_link'] else ''}</td>"
            f"<td>{e(x['state'])}</td><td>{e(x['priority'])}<br><small>{e(x['priority_reason'])}</small></td>"
            f"<td>{e(x['source_quality'])}<br><small>{src}</small></td><td>{e(x['checked'])}</td><td><small>{e(x['honest_gap'])}</small></td>"
            f"<td>{e(x['status'])}</td><td>{shots}</td></tr>")

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Town pages scale review</title>
<style>
:root{{--bg:#FBF7EF;--fg:#1E3A2B;--mut:#5B7A5F;--line:#d8cfbf;--acc:#C8853A}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0B1F15;--fg:#F4EDE0;--mut:#A09484;--line:#2b4034;--acc:#E0A969}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 -apple-system,system-ui,sans-serif;margin:0;padding:24px 16px}}
h1,h2{{font-family:Georgia,serif;font-weight:500}} a{{color:inherit;text-decoration-color:var(--acc)}}
.wrap{{max-width:1500px;margin:0 auto}} .scroll{{overflow-x:auto}} pre{{overflow-x:auto;font-size:12.5px;border:1px solid var(--line);padding:12px}}
table{{border-collapse:collapse;width:100%;min-width:1100px}} th,td{{border-top:1px solid var(--line);padding:9px 8px;vertical-align:top;text-align:left}}
th{{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut)}} small{{color:var(--mut)}}
.thumbs{{display:flex;gap:12px;overflow-x:auto}} .thumbs a{{flex:0 0 auto;text-align:center;font-size:12px}} .thumbs img{{width:130px;display:block;border:1px solid var(--line)}}
</style></head><body><div class="wrap">
<h1>Town pages: review list (2026-10-17 afternoon: Codex corrections D16&ndash;D24, A3, A5)</h1>
<p>Website repo, local branch <code>drafts/town-pages-2026-10-16</code>, not pushed, not deployed. Format: the current FAQ layout (commit a1fd1f3), no drawn maps.
Source database: <code>{e(CSV)}</code> (file modified {mtime}, {len(rows)} rows). "Rules checked" now shows the actual day, from <code>tools/town-pages/check-log.csv</code> (Checked column: date, recheck status, next due).</p>
<p><strong>{len(pub)} published drafts, {len(held)} held</strong> ({summary}). Held rows without a page are database rows we didn't draft.</p>
<h2>Screenshot sample</h2>
<div class="thumbs">{''.join(f"<a href='screens/{s}-phone.png'><img src='screens/{s}-phone.png' alt=''>{s}</a>" for s in samples)}</div>
<h2>Pages and held rows</h2>
<div class="scroll"><table><thead><tr><th>Page / path</th><th>State</th><th>Priority</th><th>Source quality</th><th>Checked</th><th>Honest gap</th><th>Status</th><th>Screens</th></tr></thead>
<tbody>{''.join(tr(x) for x in out_rows)}</tbody></table></div>
<h2>Counted links and page rewrites the deploy needs</h2>
<pre>{e(links_text([t for t in TOWNS if t['publish']]))}</pre>
</div></body></html>"""
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(page)
print(f"wrote {OUT}: {len(pub)} published, {len(held)} held")
