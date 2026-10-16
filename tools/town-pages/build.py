#!/usr/bin/env python3
"""Build the "Golf carts in [town]" pages, the /cart-rules hub and their sitemap entries.

    python3 tools/town-pages/build.py [site_dir]          (site_dir defaults to SlowGo-Launch)
    python3 tools/town-pages/build.py --links             print the link.mjs list + _redirects rewrites
    python3 tools/town-pages/check.py                     run after every build

The page layout, wording and structure are the original 2026-10-16 drafts (commit 37c0472), restored
by Ron's ruling 2026-10-17. The only additions to the original template:
  1+2. a short independence line under the heading, with the official-rules link
  3.   "Rules checked [Month Year]" (already in the original)
  4.   the signs box leads with "Always follow local signs." (original sentences kept)
  5.   the closing ends with the town-staff email line (replaces "Spot something out of date? ...")
  6.   search markup: <title>, meta description (= the visible lede) and WebPage JSON-LD
  7.   a plain "Get SlowGo" counted link /t/<slug> in "Using SlowGo here"
  plus the plain map line where the town has its own map (no drawn maps), and noindex only on
  held pages (publish=False in towns.py).
Styles, favicon, fonts and footer are copied from <site_dir>/safety.html at build time.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import TOWNS

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
SITE = ARGS[0] if (ARGS and __name__ == "__main__") else os.path.join(ROOT, "SlowGo-Launch")
ORIGIN = "https://slowgoapp.com"
CHECKED = "October 2026"      # "Rules checked ..." and the title's "(Updated ...)"
LASTMOD = "2026-10-16"        # sitemap lastmod and JSON-LD dateModified
STATE_ORDER = ["Florida", "Georgia"]

safety = open(os.path.join(SITE, "safety.html"), encoding="utf-8").read()
style = re.search(r"<style>(.*?)</style>", safety, re.S).group(1)
footer = re.search(r'(<footer class="foot".*?</footer>)', safety, re.S).group(1)
footer = footer.replace("<li>Safety</li>", '<li><a href="/safety">Safety</a></li>')
icon = re.search(r'(<link rel="icon"[^\n]*/>)', safety).group(1)
fonts = "\n".join(l for l in safety.splitlines() if "fonts.g" in l)

EXTRA = """
  /* -------- Town pages (draft 2026-10-16) -------- */
  .prose ul{ margin:16px 0 0; padding-left:1.2em; }
  .prose li{ margin:6px 0 0; }
  .checked{
    margin:28px 0 0; font-family:var(--mono); font-size:12px; letter-spacing:.14em;
    text-transform:uppercase; color:var(--drift);
  }
  .signs{
    margin:40px 0 0; padding:20px 24px; background:var(--oat);
    border-left:3px solid var(--amber); border-radius:4px; color:var(--forest);
  }
  .signs p{ margin:0; }
  .prose .sources{ list-style:none; padding:0; }
  .prose .sources li{ margin:12px 0 0; padding-left:0; }
  .indep{ max-width:74ch; margin:24px 0 0; font-size:15px; line-height:1.6; color:var(--moss); }
"""

HELD_NOTE = """
<!-- HELD (Ron 2026-10-17): not in the hub, not in sitemap.xml, noindex. publish=False in tools/town-pages/towns.py.
     To publish: Ron's ruling, then publish=True, rebuild, and a bundled, counted Netlify deploy. -->
<meta name="robots" content="noindex, nofollow" />"""
BUILT = "\n<!-- Built by tools/town-pages/build.py from towns.py: edit those, not this file. -->"


def plain(s):
    """HTML fragment -> plain text (meta description, JSON-LD, checks)."""
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", html.unescape(s)).strip()
    return re.sub(r" ([.,;:])", r"\1", s)


def webpage_ld(name, desc, url):
    # Plain WebPage markup (not FAQPage): the pages are not written as questions and answers, so
    # name = the visible <h1> and description = the visible lede, word for word (check.py enforces it).
    return {"@context": "https://schema.org", "@type": "WebPage", "name": name, "description": desc,
            "url": url, "inLanguage": "en", "dateModified": LASTMOD,
            "isPartOf": {"@type": "WebSite", "name": "SlowGo", "url": ORIGIN + "/"}}


def head(title, desc, url, og_type, robots_block, ld):
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />{robots_block}
<title>{t}</title>
<meta name="description" content="{d}" />
<meta name="theme-color" content="#0B1F15" />
<meta name="apple-itunes-app" content="app-id=6803226504">
<link rel="canonical" href="{url}" />

<meta property="og:type" content="{og_type}" />
<meta property="og:title" content="{t}" />
<meta property="og:description" content="{d}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="https://slowgoapp.com/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="The SlowGo wordmark above the line 'Life's better at 15 mph.'" />
<meta property="og:site_name" content="SlowGo" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{t}" />
<meta name="twitter:description" content="{d}" />
<meta name="twitter:image" content="https://slowgoapp.com/og-image.png" />
<meta name="twitter:image:alt" content="The SlowGo wordmark above the line 'Life's better at 15 mph.'" />

{icon}

{fonts}

<style>{style}{EXTRA}</style>
<script type="application/ld+json">
{json.dumps(ld, indent=1, ensure_ascii=False)}
</script>
</head>
<body>

<a class="skip" href="#doc">Skip to the page</a>

<header class="topbar" role="banner">
  <div class="topbar-inner">
    <a class="mark" href="/" aria-label="SlowGo home">Slow<em>Go</em></a>
    <nav aria-label="Primary">
      <a href="/">Back to SlowGo</a>
    </nav>
  </div>
</header>
"""


def page(t):
    title = f"Golf Cart Rules in {plain(t['name'])}, {t['st']} (Updated {CHECKED})"
    url = f"{ORIGIN}/golf-carts/{t['slug']}"
    h1 = f"Golf carts in {t['name']}"
    desc = plain(t["lede"])
    secs = "\n\n".join(
        f'      <h2 id="{re.sub(r"[^a-z]+", "-", h.lower()).strip("-")}">{h}</h2>\n      {body}'
        for h, body in t["sections"])
    srcs = "\n".join(f'        <li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in t["sources"])
    ml = t.get("map_line")
    map_p = f'\n      <p class="mapline">{ml[0]}<a href="{ml[2]}" rel="noopener">{ml[1]}</a>.</p>\n' if ml else ""
    robots = BUILT if t["publish"] else BUILT + HELD_NOTE
    return head(title, desc, url, "article", robots, webpage_ld(plain(h1), desc, url)) + f"""
<main class="legal">
  <div class="wrap">
    <p class="eyebrow"><span class="dot"></span> Local cart rules</p>
    <h1>{h1}</h1>
    <p class="indep">SlowGo is an independent app, not affiliated with {t['jur']}. For official rules, see <a href="{t['official'][1]}" rel="noopener">{t['official'][0]}</a>.</p>

    <article class="prose" id="doc">

      <p class="lede">{t['lede']}</p>
{map_p}
{secs}

      <div class="signs"><p><strong>Always follow local signs.</strong> Posted signs and local officers have the final word, and rules can change after we check them. If a sign says something different from this page, follow the sign.</p></div>

      <h2 id="sources">Official sources</h2>
      <ul class="sources">
{srcs}
      </ul>
      <p class="checked">Rules checked {CHECKED}</p>

      <h2 id="slowgo">Using SlowGo here</h2>
      <p>{t['slowgo']}</p>
      <p><a href="/t/{t['slug']}">Get SlowGo</a></p>

      <p class="closing">This page sums up the official sources above in plain words. It isn&rsquo;t legal advice. Rules change, so check with {t['jur']} if you&rsquo;re unsure. Town staff: see something out of date? Email <a href="mailto:hello@slowgoapp.com">hello@slowgoapp.com</a> and we&rsquo;ll fix it quickly.</p>

    </article>
  </div>
</main>

{footer}

</body>
</html>
"""


HUB_H1 = "Golf cart rules by town"
HUB_LEDE = ("Golf cart rules change from town to town: which streets carts can use, who can drive, whether a cart "
            "needs a sticker, and whether it can go out after dark. Here are the rules in plain words for the towns "
            "we&rsquo;ve checked, each with links to the official sources.")


def hub(pub):
    url = f"{ORIGIN}/cart-rules"
    desc = plain(HUB_LEDE)
    groups = []
    for st in STATE_ORDER:
        ts = sorted((t for t in pub if t["state"] == st), key=lambda t: plain(t["name"]))
        if ts:
            lis = "\n".join(f'        <li><a href="/golf-carts/{t["slug"]}">{t["name"]}</a>. {t["hub"]}</li>' for t in ts)
            groups.append(f'      <h2 id="{st.lower()}">{st}</h2>\n      <ul>\n{lis}\n      </ul>')
    return head(f"Golf Cart Rules by Town (Updated {CHECKED})", desc, url, "website", BUILT,
                webpage_ld(HUB_H1, desc, url)) + f"""
<main class="legal">
  <div class="wrap">
    <p class="eyebrow"><span class="dot"></span> Local cart rules</p>
    <h1>{HUB_H1}</h1>
    <p class="indep">SlowGo is an independent app, not affiliated with any town, city or county.</p>

    <article class="prose" id="doc">

      <p class="lede">{HUB_LEDE}</p>

{chr(10).join(groups)}

      <div class="signs"><p><strong>Always follow local signs.</strong> Posted signs and local officers have the final word, and rules can change after we check them. If a sign says something different from these pages, follow the sign.</p></div>
      <p class="checked">Rules checked {CHECKED}</p>

      <h2 id="slowgo">Using SlowGo</h2>
      <p>SlowGo plans golf cart and LSV routes on roads posted 35 mph and under. It doesn&rsquo;t know these town rules yet, so each page above says what to check before you ride.</p>
      <p><a href="/t/cart-rules">Get SlowGo</a></p>

      <p class="closing">These pages sum up each town&rsquo;s official sources in plain words. They aren&rsquo;t legal advice. Town staff: see something out of date? Email <a href="mailto:hello@slowgoapp.com">hello@slowgoapp.com</a> and we&rsquo;ll fix it quickly.</p>

    </article>
  </div>
</main>

{footer}

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
    open(path, "w", encoding="utf-8").write(sm.replace("\n</urlset>", block + "\n</urlset>"))
    return len(urls)


def links_text(pub):
    slugs = ["cart-rules"] + [t["slug"] for t in pub]
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
            f.write(page(t))
    with open(os.path.join(SITE, "cart-rules.html"), "w", encoding="utf-8") as f:
        f.write(hub(pub))
    n = update_sitemap(pub)
    print(f"{len(TOWNS)} town pages ({len(pub)} published, {len(TOWNS) - len(pub)} held), hub, {n} sitemap entries -> {SITE}")
