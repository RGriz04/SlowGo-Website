#!/usr/bin/env python3
"""Check the built town pages and hub against Ron's rulings of 2026-10-17. Read-only, no network.

    python3 tools/town-pages/check.py [site_dir]      exit 0 = all checks pass

Ruling (latest): the original 2026-10-16 drafts (commit 37c0472) come back word for word, with only
these additions: short independence line + official link; "Rules checked"; "Always follow local
signs." as the signs-box lead; town-staff email in the closing; title / meta description / JSON-LD;
a plain "Get SlowGo" link /t/<slug>; the plain map line where the town has a map. No drawn maps.
JSON-LD is plain WebPage (not FAQPage): name = visible <h1>, description = visible lede.
When git has 37c0472, every line that differs from the original page must be one of the additions.
"""
import difflib, html, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import TOWNS
from build import plain, CHECKED, ORIGIN, HUB_H1, HUB_LEDE

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "SlowGo-Launch")
ORIGINAL = "37c0472"
fails, n = [], 0

# Lines allowed to differ from the original draft (removed from it / added to it).
ALLOWED_REMOVED = [r"<!-- DRAFT 2026-10-16", r"^\s+The noindex line below", r"^\s+counted Netlify deploy",
                   r'<meta name="robots" content="noindex, nofollow" />', r"<title>Golf carts in .* — SlowGo</title>",
                   r'<meta (name|property)="(description|og:title|og:description|twitter:title|twitter:description)"',
                   r"^\s*$", r"<strong>Check local signs\.</strong>", r'<p class="closing">.*Spot something out of date\?']
ALLOWED_ADDED = [r"<!-- Built by tools/town-pages/build.py", r"<!-- HELD \(Ron 2026-10-17\)", r"^\s+To publish: Ron's ruling",
                 r'<meta name="robots" content="noindex, nofollow" />', r"<title>Golf Cart Rules in .*\(Updated ",
                 r'<meta (name|property)="(description|og:title|og:description|twitter:title|twitter:description)"',
                 r"^\s+\.indep\{", r'<p class="indep">SlowGo is an independent app, not affiliated with',
                 r'<p class="mapline">', r"^\s*$", r"<strong>Always follow local signs\.</strong>",
                 r'<p><a href="/t/[a-z-]+">Get SlowGo</a></p>', r'<p class="closing">.*Town staff: see something out of date\? Email'] \
                + [r'^<script type="application/ld\+json">$', r"^</script>$", r'^\s*[{}"\]]', r"^\s*\}"]


def ok(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)


def git_original(path):
    try:
        return subprocess.run(["git", "-C", ROOT, "show", f"{ORIGINAL}:SlowGo-Launch/{path}"], capture_output=True,
                              text=True, check=True).stdout
    except Exception:
        return None


def check_ld(page, src, h1_text, lede_text, url):
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
    ok(len(lds) == 1, f"{page}: exactly one JSON-LD block")
    if not lds:
        return
    try:
        d = json.loads(lds[0])
    except Exception as e:
        ok(False, f"{page}: JSON-LD parses ({e})"); return
    ok(d.get("@context") == "https://schema.org" and d.get("@type") == "WebPage", f"{page}: JSON-LD is a schema.org WebPage")
    ok(d.get("name") == h1_text, f"{page}: JSON-LD name equals the visible heading")
    ok(d.get("description") == lede_text, f"{page}: JSON-LD description equals the visible lede")
    ok(d.get("url") == url, f"{page}: JSON-LD url equals canonical")
    meta = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', src).group(1))
    ok(meta == lede_text, f"{page}: meta description equals the visible lede")
    ok("FAQPage" not in src and "Question" not in lds[0], f"{page}: no FAQPage markup")


pub = [t for t in TOWNS if t["publish"]]
for t in TOWNS:
    page = f"golf-carts/{t['slug']}.html"
    src = open(os.path.join(SITE, page), encoding="utf-8").read()
    body = src.split("<body>", 1)[1].split('<footer class="foot"', 1)[0]
    url = f"{ORIGIN}/golf-carts/{t['slug']}"
    ok(('name="robots" content="noindex' in src) != t["publish"], f"{page}: noindex {'absent' if t['publish'] else 'present'}")
    ok(html.unescape(re.search(r"<title>(.*?)</title>", src).group(1)) == f"Golf Cart Rules in {plain(t['name'])}, {t['st']} (Updated {CHECKED})", f"{page}: title format")
    ok(f'<link rel="canonical" href="{url}" />' in src, f"{page}: canonical")
    ok('<p class="eyebrow"><span class="dot"></span> Local cart rules</p>' in body, f"{page}: original eyebrow")
    h1 = re.search(r"<h1>(.*?)</h1>", body).group(1)
    ok(h1 == f"Golf carts in {t['name']}", f"{page}: original H1")
    want_h2 = [h for h, _ in t["sections"]] + ["Official sources", "Using SlowGo here"]
    ok(re.findall(r"<h2[^>]*>(.*?)</h2>", body) == want_h2, f"{page}: original section order and headings")
    for h, b in t["sections"]:
        ok(b in body, f"{page}: original section text verbatim ({h})")
    ok(f'<p class="lede">{t["lede"]}</p>' in body and f"<p>{t['slowgo']}</p>" in body, f"{page}: original lede and SlowGo paragraph")
    for nm, u in t["sources"]:
        ok(f'<a href="{u}" rel="noopener">{nm}</a>' in body, f"{page}: source listed ({plain(nm)[:40]})")
    ind = re.findall(r'<p class="indep">(.*?)</p>', body)
    ok(len(ind) == 1 and ind[0].startswith(f"SlowGo is an independent app, not affiliated with {t['jur']}. For official rules, see ")
       and f'href="{t["official"][1]}"' in ind[0], f"{page}: short independence line with the official link")
    ok(body.index('class="indep"') < body.index('class="lede"'), f"{page}: independence line near the top")
    ok("endorsed" not in body and "plain-English summary" not in body, f"{page}: long endorsement and 'publishes' lines dropped")
    ok(f'<p class="checked">Rules checked {CHECKED}</p>' in body, f"{page}: rules checked")
    ok('<div class="signs"><p><strong>Always follow local signs.</strong> Posted signs and local officers have the final word, and rules can change after we check them. If a sign says something different from this page, follow the sign.</p></div>' in body,
       f"{page}: signs box: new lead, original sentences")
    closing = re.search(r'<p class="closing">(.*?)</p>', body, re.S).group(1)
    ok(closing.startswith(f"This page sums up the official sources above in plain words. It isn&rsquo;t legal advice. Rules change, so check with {t['jur']} if you&rsquo;re unsure. Town staff: see something out of date? Email "),
       f"{page}: original closing + town-staff line")
    ok("Spot something out of date" not in body and "general information" not in body, f"{page}: old email line and extra legal line gone")
    ok(body.count(f'<p><a href="/t/{t["slug"]}">Get SlowGo</a></p>') == 1 and 'class="get"' not in body, f"{page}: one plain counted link /t/{t['slug']}")
    slowgo_sec = body.split('<h2 id="slowgo">', 1)[1]
    ok(f'href="/t/{t["slug"]}"' in slowgo_sec, f"{page}: counted link inside 'Using SlowGo here'")
    ok("<svg" not in body and "<figure" not in body and "legend" not in body, f"{page}: no drawn map")
    ml = t.get("map_line")
    lines = re.findall(r'<p class="mapline">(.*?)</p>', body)
    if ml:
        ok(lines == [f'{ml[0]}<a href="{ml[2]}" rel="noopener">{ml[1]}</a>.'], f"{page}: one plain map line to the town's own map")
    else:
        ok(not lines, f"{page}: no map line (no town map)")
    ok(not re.search(r"<img\b", body), f"{page}: no images (no logos or seals)")
    ok(len(re.findall(r"<script(?![^>]*application/ld\+json)", src)) == 0, f"{page}: no JavaScript")
    check_ld(page, src, plain(h1), plain(t["lede"]), url)
    orig = git_original(page)
    if orig is not None:
        extra = [l for l in difflib.unified_diff(orig.splitlines(), src.splitlines(), lineterm="", n=0)
                 if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        bad = [l for l in extra if not any(re.search(p, l[1:]) for p in (ALLOWED_ADDED if l[0] == "+" else ALLOWED_REMOVED))]
        ok(not bad, f"{page}: differs from {ORIGINAL} only by the allowed additions (unexpected: {bad[:3]})")
    else:
        print(f"note: {ORIGINAL} not in git here; original-diff check skipped for {page}")

hub = open(os.path.join(SITE, "cart-rules.html"), encoding="utf-8").read()
hb = hub.split("<body>", 1)[1].split('<footer class="foot"', 1)[0]
ok('name="robots"' not in hub, "hub: indexable")
ok("Golf Cart Rules by Town (Updated" in hub, "hub: title")
ok('<p class="eyebrow"><span class="dot"></span> Local cart rules</p>' in hb and f"<h1>{HUB_H1}</h1>" in hb, "hub: restored page style")
ok(hb.count('<p><a href="/t/cart-rules">Get SlowGo</a></p>') == 1, "hub: plain counted link")
ok("Town staff: see something out of date? Email" in hb, "hub: town-staff line")
for t in TOWNS:
    ok((f'href="/golf-carts/{t["slug"]}"' in hub) == t["publish"], f"hub: {t['slug']} {'listed' if t['publish'] else 'not listed (held)'}")
ok(hb.index(">Florida</h2>") < hb.index(">Georgia</h2>"), "hub: grouped by state")
ok(not re.search(r"<img\b|<svg|<script(?![^>]*application/ld\+json)", hb), "hub: no images, maps or JavaScript")
check_ld("hub", hub, HUB_H1, plain(HUB_LEDE), f"{ORIGIN}/cart-rules")

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
