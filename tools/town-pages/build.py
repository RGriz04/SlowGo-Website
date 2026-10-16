#!/usr/bin/env python3
"""Build the "Golf Cart Rules in [Town]" pages, the /cart-rules hub and their sitemap entries.

    python3 tools/town-pages/build.py [site_dir]        (site_dir defaults to SlowGo-Launch)

Reads towns.py (content) and <site_dir>/safety.html (styles, favicon, fonts and footer are copied
from it, so a rebuild picks up site-wide changes). Writes:
    <site_dir>/golf-carts/<slug>.html   every town (publish=False pages stay noindex, unlinked)
    <site_dir>/cart-rules.html          the hub: published towns only, grouped by state
    <site_dir>/sitemap.xml              the block between the town-pages markers only
No JavaScript on any page. Each page carries FAQPage JSON-LD built from the same FAQ text it shows.
Download links are the counted links /t/<slug> (and /t/cart-rules on the hub), served by
netlify/functions/link.mjs once its /t/ paths are added (`python3 build.py --links` prints the
link.mjs list and the _redirects page rewrites the published set needs).
Check after every build: python3 tools/town-pages/check.py
"""
import html, importlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import FAQ_ORDER

# Content modules, in order. Each defines TOWNS (a list of page dicts in the towns.py schema).
# towns.py = the first 10 pages (2026-10-16); the rest = the scale-up of 2026-10-17 (state pages have kind="state").
MODULES = os.environ.get("TOWN_MODULES", "towns,towns_fl_coast,towns_fl_inland,towns_ga_az,states").split(",")   # TOWN_MODULES limits a test build
TOWNS = []
for _m in MODULES:
    try:
        TOWNS += importlib.import_module(_m).TOWNS
    except ModuleNotFoundError as _e:
        if _e.name != _m:
            raise

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
SITE = ARGS[0] if (ARGS and __name__ == "__main__") else os.path.join(ROOT, "SlowGo-Launch")
ORIGIN = "https://slowgoapp.com"
UPDATED = "October 2026"      # title "(Updated ...)" and "Rules checked ..."; change when the rules are re-checked
LASTMOD = "2026-10-16"        # sitemap lastmod for every town page and the hub
STATE_ORDER = ["Florida", "Georgia", "Arizona"]

safety = open(os.path.join(SITE, "safety.html"), encoding="utf-8").read()
STYLE = re.search(r"<style>(.*?)</style>", safety, re.S).group(1)
FOOTER = re.search(r'(<footer class="foot".*?</footer>)', safety, re.S).group(1)
FOOTER = FOOTER.replace("<li>Safety</li>", '<li><a href="/safety">Safety</a></li>')
ICON = re.search(r'(<link rel="icon"[^\n]*/?>)', safety).group(1)
FONTS = "\n".join(l for l in safety.splitlines() if "fonts.g" in l)

EXTRA = """
  /* -------- Town pages (tools/town-pages) -------- */
  .prose ul{ margin:16px 0 0; padding-left:1.2em; }
  .prose li{ margin:6px 0 0; }
  .indep{ max-width:74ch; margin:0 0 28px; padding:12px 16px; border:1px solid rgba(160,148,132,.45);
    border-radius:6px; font-size:14px; line-height:1.6; color:var(--moss); }
  .indep p{ margin:0; } .indep p + p{ margin-top:6px; }
  .meta{ font-family:var(--mono); font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--drift); }
  .prose .meta{ margin:14px 0 0; }
  .signs{ margin:40px 0 0; padding:20px 24px; background:var(--oat); border-left:3px solid var(--amber);
    border-radius:4px; color:var(--forest); }
  .signs p{ margin:0; }
  .prose .sources{ list-style:none; padding:0; }
  .prose .sources li{ margin:12px 0 0; }
  .prose .maplink{ margin:20px 0 0; }
  .get{ display:inline-block; margin:20px 0 0; padding:12px 22px; border-radius:999px; background:var(--forest);
    color:var(--cream); font-weight:600; font-size:16px; text-decoration:none; }
  .get:hover{ background:var(--charcoal); color:var(--cream); }
  .townfoot{ margin:56px 0 0; padding-top:24px; border-top:1px solid rgba(160,148,132,.28); font-size:15px; color:var(--moss); }
  .prose .townfoot p{ margin:0 0 8px; }
  .prose .towns{ list-style:none; padding:0; }
  .prose .towns li{ margin:18px 0 0; }
  .towns a{ font-family:var(--serif); font-size:21px; font-weight:500; }
  .towns span{ display:block; color:var(--moss); font-size:16px; }
"""


def plain(s):
    """HTML fragment -> plain text (for meta descriptions and JSON-LD)."""
    s = re.sub(r"</li>\s*<li>", "; ", s)
    s = re.sub(r"</p>\s*<p>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).replace(" ;", ";").replace(" .", ".").replace(" ,", ",").replace(" :", ":").strip()


def slug_id(h):
    return re.sub(r"[^a-z]+", "-", plain(h).lower()).strip("-")[:60]


# ---------- Shared bits ----------
def head(title, desc, url, robots, og_type, jsonld=None, draft_note=""):
    rob = f'<meta name="robots" content="{robots}" />\n' if robots else ""
    ld = f'<script type="application/ld+json">\n{json.dumps(jsonld, indent=1, ensure_ascii=False)}\n</script>\n' if jsonld else ""
    t, d = html.escape(title), html.escape(desc)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<!-- Built by tools/town-pages/build.py from towns.py: edit those, not this file. -->{draft_note}
{rob}<title>{t}</title>
<meta name="description" content="{d}" />
<meta name="theme-color" content="#0B1F15" />
<meta name="apple-itunes-app" content="app-id=6803226504">
<link rel="canonical" href="{url}" />

<meta property="og:type" content="{og_type}" />
<meta property="og:title" content="{t}" />
<meta property="og:description" content="{d}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{ORIGIN}/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="The SlowGo wordmark above the line 'Life's better at 15 mph.'" />
<meta property="og:site_name" content="SlowGo" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{t}" />
<meta name="twitter:description" content="{d}" />
<meta name="twitter:image" content="{ORIGIN}/og-image.png" />
<meta name="twitter:image:alt" content="The SlowGo wordmark above the line 'Life's better at 15 mph.'" />

{ICON}

{FONTS}

<style>{STYLE}{EXTRA}</style>
{ld}</head>
<body>

<a class="skip" href="#doc">Skip to the page</a>

<header class="topbar" role="banner">
  <div class="topbar-inner">
    <a class="mark" href="/" aria-label="SlowGo home">Slow<em>Go</em></a>
    <nav aria-label="Primary">
      <a href="/cart-rules">All towns</a>
      <a href="/">Back to SlowGo</a>
    </nav>
  </div>
</header>
"""


TOWNFOOT = """      <div class="townfoot">
        <p>Town staff: see something out of date? Email <a href="mailto:hello@slowgoapp.com">hello@slowgoapp.com</a> and we&rsquo;ll fix it quickly.</p>
        <p>This page is general information, not legal advice. Always follow posted signs and local rules.</p>
      </div>"""

DRAFT = """
<!-- HELD (Ron 2026-10-17): not in the hub, not in sitemap.xml, noindex. publish=False in towns.py.
     To publish: Ron's ruling, then publish=True, rebuild, and a bundled, counted Netlify deploy. -->"""


def faq_items(t):
    return [(q.format(n=t["name"]), t["faq"][k]) for k, q in FAQ_ORDER]


def faq_jsonld(t):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": plain(q),
                        "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq_items(t)],
    }


def is_state(t):
    return t.get("kind") == "state"


def state_towns(t):
    """Published town pages in a state page's state (for its "Towns we've checked" section)."""
    return sorted((x for x in TOWNS if x["publish"] and not is_state(x) and x["state"] == t["state"]), key=lambda x: plain(x["name"]))


def map_link(t):
    """Plain text link to the town's own golf cart map, only where one exists (Ron 2026-10-17)."""
    sm = t.get("street_map")
    if not sm:
        return ""
    return f'      <p class="maplink">See <a href="{sm[1]}" rel="noopener">{t["name"]}&rsquo;s official golf cart map</a>.</p>\n'


def town_page(t):
    title = t.get("title") or f"Golf Cart Rules in {plain(t['name'])}, {t['st']} (Updated {UPDATED})"
    url = f"{ORIGIN}/golf-carts/{t['slug']}"
    h1 = t.get("h1") or f"Golf cart rules in {t['name']}, {t['state']}"
    eyebrow = t.get("eyebrow") or "Local cart rules"
    held = t.get("held_note") or DRAFT
    slug = t["slug"]
    get = f'\n      <a class="get" href="/t/{slug}">Get SlowGo</a>' if t.get("counted", True) else ""
    extra = list(t["extra"])
    if is_state(t):
        ts = state_towns(t)
        if ts:
            lis = "\n".join(f'        <li><a href="/golf-carts/{x["slug"]}">{x["name"]}</a><span>{x["hub"]}</span></li>' for x in ts)
            extra.append((f"Towns we&rsquo;ve checked in {t['state']}", f'<ul class="towns">\n{lis}\n      </ul>'))
    publishes = t.get("publishes") or f"{t['Org']} publishes its golf cart rules. Here&rsquo;s a plain-English summary."
    if "plain-English" not in publishes:
        publishes += " Here&rsquo;s a plain-English summary."
    secs = [(q, a) for q, a in faq_items(t)] + extra
    body = "\n\n".join(f'      <h2 id="{slug_id(h)}">{h}</h2>\n      {b}' for h, b in secs)
    srcs = "\n".join(f'        <li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in t["sources"])
    robots = None if t["publish"] else "noindex, nofollow"
    return head(title, plain(t["answer"]), url, robots, "article", faq_jsonld(t), "" if t["publish"] else held) + f"""
<main class="legal">
  <div class="wrap">
    <div class="indep">
      <p>SlowGo is an independent golf cart navigation app. This page isn&rsquo;t affiliated with or endorsed by {t['org']}. For official rules, see <a href="{t['official'][1]}" rel="noopener">{t['official'][0]}</a>.</p>
      <p>{publishes}</p>
    </div>
    <p class="eyebrow"><span class="dot"></span> {eyebrow} &middot; Updated {UPDATED}</p>
    <h1>{h1}</h1>

    <article class="prose" id="doc">

      <p class="lede">{t['answer']}</p>
      <p class="meta">Rules checked {UPDATED} &middot; Always follow local signs</p>

{map_link(t)}
{body}

      <div class="signs"><p><strong>Always follow local signs.</strong> Posted signs and local officers have the final word, and rules can change after we check them. If a sign says something different from this page, follow the sign.</p></div>

      <h2 id="slowgo">Using SlowGo here</h2>
      <p>{t['slowgo']}</p>{get}

      <h2 id="sources">Where these rules come from</h2>
      <ul class="sources">
{srcs}
      </ul>
      <p class="meta">Rules checked {UPDATED}</p>

{TOWNFOOT}

    </article>
  </div>
</main>

{FOOTER}

</body>
</html>
"""


def hub_page(pub):
    title = f"Golf Cart Rules by Town (Updated {UPDATED})"
    desc = ("Plain-English summaries of golf cart rules in Florida, Georgia and Arizona towns: where carts can go, "
            "licenses, age, permits, LSVs, and night driving, with links to each town's own rules.")
    groups = []
    for st in STATE_ORDER:
        sp = [t for t in pub if t["state"] == st and is_state(t)]
        ts = sp + sorted((t for t in pub if t["state"] == st and not is_state(t)), key=lambda t: plain(t["name"]))
        if not ts:
            continue
        lis = "\n".join(f'        <li><a href="/golf-carts/{t["slug"]}">{t.get("hub_name") or t["name"]}</a><span>{t["hub"]}</span></li>' for t in ts)
        groups.append(f'      <h2 id="{st.lower()}">{st}</h2>\n      <ul class="towns">\n{lis}\n      </ul>')
    return head(title, desc, f"{ORIGIN}/cart-rules", None, "website") + f"""
<main class="legal">
  <div class="wrap">
    <div class="indep">
      <p>SlowGo is an independent golf cart navigation app. These pages aren&rsquo;t affiliated with or endorsed by any town, city or county. Each page links to the rules its town or county publishes.</p>
    </div>
    <p class="eyebrow"><span class="dot"></span> Local cart rules &middot; Updated {UPDATED}</p>
    <h1>Golf cart rules by town</h1>

    <article class="prose" id="doc">

      <p class="lede">Golf cart rules change from town to town: which streets carts can use, who can drive, whether a cart needs a sticker, and whether it can go out after dark. These are our plain-English summaries, each with links to where the rules come from.</p>
      <p class="meta">Rules checked {UPDATED} &middot; Always follow local signs</p>
      <a class="get" href="/t/cart-rules">Get SlowGo</a>

{chr(10).join(groups)}

      <div class="signs"><p><strong>Always follow local signs.</strong> Posted signs and local officers have the final word, and rules can change after we check them.</p></div>

{TOWNFOOT.replace("This page is", "These pages are")}

    </article>
  </div>
</main>

{FOOTER}

</body>
</html>
"""


def update_sitemap(pub):
    path = os.path.join(SITE, "sitemap.xml")
    sm = open(path, encoding="utf-8").read()
    sm = re.sub(r"\n  <!-- town-pages:start.*?town-pages:end -->", "", sm, flags=re.S)
    urls = [f"{ORIGIN}/cart-rules"] + [f"{ORIGIN}/golf-carts/{t['slug']}" for t in pub]
    block = "\n  <!-- town-pages:start (tools/town-pages/build.py writes this block) -->" + "".join(
        f"\n  <url>\n    <loc>{u}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>"
        for u in urls) + "\n  <!-- town-pages:end -->"
    sm = sm.replace("\n</urlset>", block + "\n</urlset>")
    open(path, "w", encoding="utf-8").write(sm)
    return len(urls)


def links_text(pub):
    slugs = ["cart-rules"] + [t["slug"] for t in pub if t.get("counted", True)]
    rw = [("/cart-rules", "/cart-rules.html")] + [(f"/golf-carts/{t['slug']}", f"/golf-carts/{t['slug']}.html") for t in pub]
    lines = ["# netlify/functions/link.mjs: counted links /t/<name> -> source 't-<name>'",
             "export const TOWN_LINKS = [" + ", ".join(f"'{s}'" for s in slugs) + "];",
             "", "# SlowGo-Launch/_redirects: clean URLs for the pages (rewrites, status 200)"]
    for a, b in rw:
        lines += [f"{a:<34} {b:<40} 200", f"{a + '/':<34} {b:<40} 200"]
    return "\n".join(lines)


if __name__ == "__main__":
    pub = [t for t in TOWNS if t["publish"]]
    if "--links" in sys.argv:
        print(links_text(pub)); sys.exit(0)
    os.makedirs(os.path.join(SITE, "golf-carts"), exist_ok=True)
    for t in TOWNS:
        with open(os.path.join(SITE, "golf-carts", t["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(town_page(t))
    with open(os.path.join(SITE, "cart-rules.html"), "w", encoding="utf-8") as f:
        f.write(hub_page(pub))
    n = update_sitemap(pub)
    print(f"{len(TOWNS)} town pages ({len(pub)} published, {len(TOWNS) - len(pub)} held), hub, {n} sitemap entries -> {SITE}")
