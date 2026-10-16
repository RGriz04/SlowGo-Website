#!/usr/bin/env python3
"""Check the built town pages and hub against Ron's 2026-10-17 rulings. Read-only, no network.

    python3 tools/town-pages/check.py [site_dir]      exit 0 = all checks pass
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import TOWNS, FAQ_ORDER
from build import plain, UPDATED, ORIGIN

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
        ok(a.get("text", "")[:60] in vis, f"{page}: answer text visible on the page ({q.get('name')})")


pub = [t for t in TOWNS if t["publish"]]
for t in TOWNS:
    page = f"golf-carts/{t['slug']}.html"
    src = open(os.path.join(SITE, page), encoding="utf-8").read()
    body = src.split("<body>", 1)[1].split('<footer class="foot"', 1)[0]
    noindex = 'name="robots" content="noindex' in src
    ok(noindex != t["publish"], f"{page}: noindex {'absent' if t['publish'] else 'present'}")
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    ok(html.unescape(title) == f"Golf Cart Rules in {plain(t['name'])}, {t['st']} (Updated {UPDATED})", f"{page}: title format ({title})")
    ok("SlowGo is an independent golf cart navigation app. This page isn&rsquo;t affiliated with or endorsed by" in body, f"{page}: independence line")
    ok(body.index('class="indep"') < body.index("<h1>"), f"{page}: independence line at the top")
    ok("publishes" in body and "plain-English summary" in body, f"{page}: respectful line")
    ok("Town staff: see something out of date? Email" in body and "not legal advice. Always follow posted signs and local rules." in body, f"{page}: town footer lines")
    ok(f"Rules checked {UPDATED}" in body and "Always follow local signs" in body, f"{page}: rules checked + follow signs")
    ok(f'href="/t/{t["slug"]}"' in body, f"{page}: counted link /t/{t['slug']}")
    ok("<svg" not in body and "diagram" not in body and "legend" not in body, f"{page}: no drawn map (Ron 2026-10-17)")
    sm = t.get("street_map")
    link = re.findall(r'<p class="maplink">See <a href="([^"]+)" rel="noopener">(.*?)</a>\.</p>', body)
    if sm:
        ok(link == [(sm[1], f"{t['name']}&rsquo;s official golf cart map")], f"{page}: one official map link to the town's own map")
    else:
        ok(not link and "golf cart map" not in body, f"{page}: no map link (no official map)")
    ok(not re.search(r"<img\b", body), f"{page}: no images (no logos or seals)")
    ok(len(re.findall(r"<script(?![^>]*application/ld\+json)", src)) == 0, f"{page}: no JavaScript")
    off = [m.start() for m in re.finditer(r"official", plain(body), re.I)]
    ok(len(off) == 1 + bool(t.get("street_map")) and "For official rules, see" in plain(body),
       f"{page}: 'official' only in the mandated sentence and the map link ({len(off)}x)")
    ok("doesn&rsquo;t know" in body or "don&rsquo;t know" in body, f"{page}: honest SlowGo paragraph")
    ok(not re.search(r"\bfolks\b|New York", body, re.I), f"{page}: copy rules (no 'folks', no New York)")
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
ok(not re.search(r"<img\b|<script", hub), "hub: no images, no JavaScript")
ok("<svg" not in hub.split("<body>", 1)[1], "hub: no drawn map")

sm = open(os.path.join(SITE, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", sm)
ok(f"{ORIGIN}/cart-rules" in locs, "sitemap: hub")
for t in TOWNS:
    ok((f"{ORIGIN}/golf-carts/{t['slug']}" in locs) == t["publish"], f"sitemap: {t['slug']} {'in' if t['publish'] else 'out (held)'}")
ok(len(locs) == len(set(locs)), "sitemap: no duplicates")

print(f"{n - len(fails)}/{n} checks passed")
for f in fails:
    print("FAIL", f)
sys.exit(1 if fails else 0)
