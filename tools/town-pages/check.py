#!/usr/bin/env python3
"""Check the built town pages and hub against Ron's 2026-10-17 rulings (morning format + afternoon D16-D24, A3, A5).
Read-only, no network.

    python3 tools/town-pages/check.py [site_dir]      exit 0 = all checks pass
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import FAQ_ORDER
from build import plain, UPDATED, ORIGIN, TOWNS, is_state, state_towns, page_path, state_page, HELD_DIR, SIGNS, SLOWGO_LEAD, LSV_LINE
import recheck

LOG = recheck.read_log()
BANNED_SIGNS = "final word"                                             # D17
FASTER = re.compile(r"faster stretch|36\s*(?:&ndash;|–|-|to)\s*45|include faster", re.I)      # A5
NOT_ALLOWED = re.compile(r"(aren.t|not|isn.t) allowed|prohibit|barred|can.t use|no carts", re.I)
NOT_FOUND = re.compile(r"(didn.t|did not|couldn.t) find|found no\b|found none|haven.t found|no such ordinance", re.I)


def sentences(text):
    return [x for x in re.split(r"(?<=[.!?])\s+", text) if x]

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "SlowGo-Launch")
fails, n = [], 0


def ok(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)


def check_faq_ld(page, src):
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
    ok(len(lds) == 1, f"{page}: exactly one JSON-LD block")
    if not lds:
        return
    try:
        d = json.loads(lds[0])
    except Exception as e:
        ok(False, f"{page}: JSON-LD parses ({e})"); return
    ok(d.get("@context") == "https://schema.org", f"{page}: @context schema.org")
    ok(d.get("@type") == "FAQPage", f"{page}: @type FAQPage")
    me = d.get("mainEntity")
    ok(isinstance(me, list) and len(me) == len(FAQ_ORDER), f"{page}: mainEntity has {len(FAQ_ORDER)} questions")
    h2s = [plain(h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", src, re.S)]
    vis = plain(src)
    for q in me or []:
        ok(q.get("@type") == "Question" and isinstance(q.get("name"), str) and q["name"], f"{page}: Question with name")
        a = q.get("acceptedAnswer") or {}
        ok(a.get("@type") == "Answer" and isinstance(a.get("text"), str) and len(a["text"]) > 20, f"{page}: Answer with text ({q.get('name')})")
        ok(q.get("name") in h2s, f"{page}: question shown as a visible heading ({q.get('name')})")
        ok(a.get("text", "") in vis, f"{page}: full answer text visible on the page ({q.get('name')})")


pub = [t for t in TOWNS if t["publish"]]
for t in TOWNS:
    page = f"golf-carts/{t['slug']}.html"
    src = open(page_path(t, SITE), encoding="utf-8").read()
    body = src.split("<body>", 1)[1].split('<footer class="foot"', 1)[0]
    noindex = 'name="robots" content="noindex' in src
    ok(noindex != t["publish"], f"{page}: noindex {'absent' if t['publish'] else 'present'}")
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    want_title = t.get("title") or f"Golf Cart Rules in {plain(t['name'])}, {t['st']} (Updated {UPDATED})"
    ok(html.unescape(title) == plain(want_title), f"{page}: title format ({title})")
    if is_state(t):
        ok(html.unescape(title) == f"Golf Cart Laws in {t['state']} (Updated {UPDATED})", f"{page}: state title format")
        for x in state_towns(t):
            ok(f'href="/golf-carts/{x["slug"]}"' in body, f"{page}: links town page {x['slug']}")
    if t["publish"]:
        ok(not re.search(r"New York|\bN\.?Y\.?\b", plain(body)), f"{page}: never names New York (Ron 2026-10-05/10-17)")
    if t.get("never_publish"):
        ok(not t["publish"] and "HELD: Ron ruling 2026-10-17, never name New York in public copy" in src, f"{page}: NY held marker")
        for o in TOWNS:
            if o is not t:
                osrc = open(page_path(o, SITE), encoding="utf-8").read()
                ok(f"/golf-carts/{t['slug']}" not in osrc, f"{page}: not linked from {o['slug']}")
    ok("SlowGo is an independent golf cart navigation app. This page isn&rsquo;t affiliated with or endorsed by" in body, f"{page}: independence line")
    ok(body.index('class="indep"') < body.index("<h1>"), f"{page}: independence line at the top")
    ok("publishes" in body and "plain-English summary" in body, f"{page}: respectful line")
    ok("Town staff: see something out of date? Email" in body and "not legal advice. Always follow posted signs and local rules." in body, f"{page}: town footer lines")
    # D23: the actual day, from the check log
    d = recheck.checked_date(t, LOG)
    ok(d is not None, f"{page}: every source has a verified check-log row")
    if d:
        dd = __import__("datetime").date.fromisoformat(d)
        day = f"{dd:%B} {dd.day}, {dd.year}"
        ok(body.count(f"Rules checked {day}") == 2, f"{page}: 'Rules checked {day}' (from check-log.csv) at the top and by the sources")
    ok(not re.search(r"Rules checked (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}", body),
       f"{page}: no month-only 'Rules checked'")
    ok("Always follow local signs" in body, f"{page}: follow signs line")
    # D17 signs sentence
    ok(SIGNS in body and BANNED_SIGNS not in src, f"{page}: new signs sentence, no 'final word'")
    # D18 SlowGo paragraph + prominent warning right above the download button
    if not t.get("slowgo_full"):
        ok(f"<p>{SLOWGO_LEAD}</p>" in body, f"{page}: standard SlowGo sentence")
        ok(not re.search(r"SlowGo plans routes", body), f"{page}: old SlowGo sentence gone")
        if t.get("counted", True):
            w, g = body.find('<div class="warn"'), body.find('class="get"')
            ok(0 < w < g and g - w < 1200 and "Check local rules before you ride." in body[w:g], f"{page}: local-rule warning box just above Get SlowGo")
    # D22 LSV line in the LSV answer
    ok(plain(LSV_LINE) in plain(t["faq"]["lsv"]), f"{page}: LSV answer has the D22 line")
    # A5
    ok(not FASTER.search(plain(body)), f"{page}: no faster-stretches / 36-45 wording")
    # D16 metadata matches the visible text
    lede = plain(re.search(r'<p class="lede">(.*?)</p>', body, re.S).group(1))
    for prop in [r'name="description"', r'property="og:description"', r'name="twitter:description"']:
        m = re.search(r'<meta ' + prop + r' content="([^"]*)"', src)
        ok(m and html.unescape(m.group(1)) == lede, f"{page}: {prop} equals the visible answer")
    # D21 state link
    sp = state_page(t)
    if sp:
        ok(f'<p class="statelink">State law: see <a href="/golf-carts/{sp["slug"]}">' in body, f"{page}: links its state page")
    elif not is_state(t):
        ok(t["state"] == "New York" or not t["publish"], f"{page}: has a published state page to link")
    # D19: no "no carts" claim resting on not finding permission; prohibition pages need an affirmative source
    if t["publish"]:
        for sn in sentences(plain(body)):
            ok(not (NOT_ALLOWED.search(sn) and NOT_FOUND.search(sn)), f"{page}: absence-based prohibition sentence: {sn[:90]}")
        if t.get("no_carts"):
            pr = t.get("prohibition") or {}
            ok(all(pr.get(k) for k in ("vehicle", "roads", "jurisdiction", "source")) and pr.get("source") in [u for _, u in t["sources"]],
               f"{page}: 'no carts' page names vehicle, roads, jurisdiction and an official source")
    # D24 state pages: 35 mph only ever for LSVs/NEVs (or SlowGo / state park roads)
    if is_state(t):
        for sn in sentences(plain(body)):
            if re.search(r"\b35\b", sn):
                ok(re.search(r"LSV|NEV|low-speed|neighborhood electric|SlowGo|state park", sn, re.I), f"{page}: '35' sentence without LSV/NEV: {sn[:90]}")
    if t.get("counted", True):
        ok(f'href="/t/{t["slug"]}"' in body, f"{page}: counted link /t/{t['slug']}")
    else:
        ok('href="/t/' not in body, f"{page}: no counted link")
    ok("<svg" not in body and "diagram" not in body and "legend" not in body, f"{page}: no drawn map (Ron 2026-10-17)")
    sm = t.get("street_map")
    link = re.findall(r'<p class="maplink">See <a href="([^"]+)" rel="noopener">(.*?)</a>\.', body)
    if sm:
        ok(link == [(sm[1], sm[0])], f"{page}: one map link, labelled as given")
        ok(not re.match(r"the (city|county|town|village)&rsquo;s", sm[0]) and "official" not in sm[0].lower(),
           f"{page}: map label names the publisher and says what the map is (D21)")
    else:
        ok(not link, f"{page}: no map link")
    ok(not re.search(r"<img\b", body), f"{page}: no images (no logos or seals)")
    ok(len(re.findall(r"<script(?![^>]*application/ld\+json)", src)) == 0, f"{page}: no JavaScript")
    off = [m.start() for m in re.finditer(r"official", plain(body), re.I)]
    ok(len(off) == 1 and "For official rules, see" in plain(body),
       f"{page}: 'official' only in the mandated sentence ({len(off)}x)")
    ok("doesn&rsquo;t know" in body or "don&rsquo;t know" in body, f"{page}: honest SlowGo paragraph")
    # D20: held pages live outside the publish folder; published pages never link to a held page
    if not t["publish"]:
        ok(page_path(t, SITE).startswith(HELD_DIR) and not os.path.exists(os.path.join(SITE, "golf-carts", t["slug"] + ".html")),
           f"{page}: held page lives in tools/town-pages/held, not SlowGo-Launch")
    else:
        for o in TOWNS:
            if not o["publish"]:
                ok(f'href="/golf-carts/{o["slug"]}"' not in body, f"{page}: doesn't link held page {o['slug']}")
    ok(not re.search(r"\bfolks\b", body, re.I) and (t.get("never_publish") or not re.search(r"New York", body)), f"{page}: copy rules (no 'folks', no New York)")
    # answer within the first sentences after the h1
    after = plain(body.split("</h1>", 1)[1])
    ok(after.startswith(plain(t["answer"])[:50]), f"{page}: answer first after the heading")
    ok(len(re.search(r"<style>(.*?)</style>", src, re.S).group(1)) < 12000, f"{page}: inline CSS under 12 KB")
    check_faq_ld(page, src)

hub = open(os.path.join(SITE, "cart-rules.html"), encoding="utf-8").read()
ok('name="robots"' not in hub, "hub: indexable")
ok('href="/t/cart-rules"' in hub, "hub: counted download link")
for t in TOWNS:
    linked = f'href="/golf-carts/{t["slug"]}"' in hub
    ok(linked == t["publish"], f"hub: {t['slug']} {'listed' if t['publish'] else 'not listed (held)'}")
ok(hub.index(">Florida</h2>") < hub.index(">Georgia</h2>"), "hub: grouped by state")
ok(not re.search(r"New York|\bN\.?Y\.?\b", plain(hub.split("<body>", 1)[1].split('<footer class="foot"', 1)[0])), "hub: never names New York")
for t in TOWNS:
    if is_state(t) and t["publish"]:
        grp = hub.split(f'>{t["state"]}</h2>', 1)[1].split("</ul>", 1)[0]
        first = re.search(r'href="/golf-carts/([a-z-]+)"', grp)
        ok(first and first.group(1) == t["slug"], f"hub: {t['state']} state page first in its group")
ok(not re.search(r"<img\b|<script", hub), "hub: no images, no JavaScript")
ok(SIGNS in hub and BANNED_SIGNS not in hub, "hub: new signs sentence, no 'final word'")
ok(not FASTER.search(plain(hub)), "hub: no faster-stretches / 36-45 wording")
ok("Check local rules before you ride." in hub and hub.find('class="warn"') < hub.find('href="/t/cart-rules"'), "hub: local-rule warning above Get SlowGo")
ok(not re.search(r"Rules checked (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}", hub), "hub: no month-only 'Rules checked'")
ok("<svg" not in hub.split("<body>", 1)[1], "hub: no drawn map")

# Ron 2026-10-17: no New York page may exist anywhere in the publish folder (a file there would ship).
for t in TOWNS:
    if t.get("never_publish"):
        ok(not page_path(t, SITE).startswith(os.path.abspath(SITE)) and os.path.exists(page_path(t, SITE)), f"{t['slug']}: held draft lives outside SlowGo-Launch")
ny_files = []
for dp, _, fs in os.walk(SITE):
    for fn in fs:
        fp = os.path.join(dp, fn)
        if "new-york" in fn.lower() or (fn.endswith((".html", ".xml", ".txt")) and "never name New York" in open(fp, encoding="utf-8", errors="ignore").read()):
            ny_files.append(os.path.relpath(fp, SITE))
ok(not ny_files, f"no New York page anywhere under the publish folder ({ny_files})")

sm = open(os.path.join(SITE, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", sm)
ok(f"{ORIGIN}/cart-rules" in locs, "sitemap: hub")
for t in TOWNS:
    ok((f"{ORIGIN}/golf-carts/{t['slug']}" in locs) == t["publish"], f"sitemap: {t['slug']} {'in' if t['publish'] else 'out (held)'}")
ok(len(locs) == len(set(locs)), "sitemap: no duplicates")

# D20: rewrites and counted links list published pages only
red = open(os.path.join(SITE, "_redirects"), encoding="utf-8").read()
red_slugs = set(re.findall(r"^/golf-carts/([a-z-]+) ", red, re.M))
ok(red_slugs == {t["slug"] for t in pub}, f"_redirects: /golf-carts/ rewrites = published pages ({sorted(red_slugs ^ {t['slug'] for t in pub})})")
cl = os.path.join(ROOT, "netlify", "counted-links.mjs")
if os.path.abspath(SITE) == os.path.join(ROOT, "SlowGo-Launch") and os.path.exists(cl):
    tl = re.search(r"export const TOWN_LINKS = \[(.*?)\];", open(cl, encoding="utf-8").read(), re.S).group(1)
    tl = set(re.findall(r"'([a-z-]+)'", tl))
    ok(tl == {"cart-rules"} | {t["slug"] for t in pub if t.get("counted", True)}, "counted-links.mjs: TOWN_LINKS = hub + published pages")

# D17 everywhere in the publish folder; D23 log file and schedule exist
for dp, _, fs in os.walk(SITE):
    for fn in fs:
        if fn.endswith(".html"):
            ok(BANNED_SIGNS not in open(os.path.join(dp, fn), encoding="utf-8", errors="ignore").read(), f"{fn}: no 'final word' sentence")
ok(os.path.exists(recheck.LOG) and os.path.exists(recheck.SCHEDULE), "check-log.csv and recheck-schedule.json exist")
ok(all(r["page"] and r["source_url"] and r["fetched"] and r["result"] and r["verified"] in ("yes", "no") for r in LOG), "check-log rows complete")

# Site menu and footer (Ron 2026-10-17): every page with the shared menu links the cart rules hub and /business,
# in the bar, in the phone Menu (<details class="mnav">) and in the footer. Never a held page.
MENU_LINKS = ('href="/cart-rules"', 'href="/business"')
menu_pages = ["index.html", "support.html", "safety.html", "terms.html", "privacy.html", "android.html", "beta.html",
              "404.html", "business.html", "cart-rules.html"]
menu_pages += [f for f in sorted(os.listdir(SITE)) if re.match(r"business-[a-z-]+\.html$", f)]
menu_pages += [f"golf-carts/{t['slug']}.html" for t in pub]
for mp in menu_pages:
    src = open(os.path.join(SITE, mp), encoding="utf-8").read()
    hd = re.search(r'<header class="topbar".*?</header>', src, re.S)
    ft = re.search(r'<footer class="foot".*?</footer>', src, re.S)
    ok(hd and ft, f"{mp}: has the shared header and footer")
    if not (hd and ft):
        continue
    hd, ft = hd.group(0), ft.group(0)
    panel = re.search(r'<details class="mnav">.*?</details>', hd, re.S)
    bar = re.sub(r'<details class="mnav">.*?</details>', "", hd, flags=re.S)
    for l in MENU_LINKS:
        ok(l in bar, f"{mp}: menu bar links {l}")
        ok(panel and l in panel.group(0), f"{mp}: phone Menu links {l}")
        ok(l in ft, f"{mp}: footer links {l}")
    ok(".topbar .mnav{ display:none; }" in src and ".topbar .mnav{ display:block; }" in src, f"{mp}: phone Menu CSS")
    for t in TOWNS:
        if not t["publish"]:
            ok(f'/golf-carts/{t["slug"]}"' not in hd + ft, f"{mp}: menu/footer never link held page {t['slug']}")
    ok("/business/setup" not in hd + ft, f"{mp}: menu/footer never link the held setup form")

print(f"{n - len(fails)}/{n} checks passed")
for f in fails:
    print("FAIL", f)
sys.exit(1 if fails else 0)
