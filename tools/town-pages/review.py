#!/usr/bin/env python3
"""Write review-sheet.csv and index.html (the review sheet) for the town pages.

    python3 tools/town-pages/review.py <out_dir>     (screenshots expected in <out_dir>/screens/)
REVIEW notes below are from the 2026-10-15/16 source reads; keep them current when a town is re-checked."""
import csv, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from towns import TOWNS
from build import links_text, CHECKED as UPDATED

out = sys.argv[1]
REVIEW = {
 "st-pete-beach": dict(conf="Strong", checked="Research 2026-10-15 read Ord. 2013-17 (scanned PDF, read as images). This run 2026-10-15: re-read city Golf Carts page; ordinance PDF and map link answer 200.",
   mismatch="Town cap is 25 mph; SlowGo allows 35.",
   open="Exhibit A borders not traced. City page says 'resident-owned' carts register; whether visitors/rentals need a decal is not stated."),
 "dunedin": dict(conf="Medium", checked="Research 2026-10-15. This run 2026-10-15: re-read city Golf Carts page; GIS map answers 200. The 2024 program final report returned 403 to a plain fetch, so it is not linked.",
   mismatch="Zone + 30 mph cap; SlowGo routes any street up to 35, inside or outside the zone.",
   open="THIN: City Code secs. 74-201/74-209 not read (Municode). Page text is from the city's summary page only."),
 "mount-dora": dict(conf="Medium-strong", checked="Research 2026-10-15. This run 2026-10-15: re-read city registration page and the street usage PDF (dated 2023-05-17).",
   mismatch="Excluded-streets list not modelled.",
   open="Ordinance number not identified (page + list only). Street list is 2023: may be stale."),
 "miami-lakes": dict(conf="Strong", checked="This run 2026-10-15: read the full text of Ord. 22-293 (adopted 2022-04-12), secs. 39-50 to 39-59.",
   mismatch="NW 67th/87th Ave closed to carts; SlowGo doesn't know.",
   open="Later amendments since 2022 not checked (town code is on Municode)."),
 "pine-island": dict(conf="Strong (2013 text)", checked="This run 2026-10-15: read the full text of Lee Ord. 13-08 (adopted 2013-04-23) incl. Attachment A header.",
   mismatch="Excluded stretches + daylight-only not modelled.",
   open="2013 ordinance: later amendments (e.g., night use) not checked. No current county web page found."),
 "captiva": dict(conf="Medium (THIN road list)", checked="This run 2026-10-15: read the full text of Lee Ord. 09-22 (2009).",
   mismatch="Designated-road list not modelled (and not known to us).",
   open="THIN: which Captiva roads Lee DOT designated (traffic regulation orders) is unknown; page tells riders to follow signs. Night designation unknown. Consider holding this page until Lee DOT's list is found."),
 "jekyll-island": dict(conf="Strong", checked="This run 2026-10-15: read the full text of JIA Rules Chapter F, Art. II (file dated April 2022).",
   mismatch="Golf cart vs PTV distinction and path closures not modelled; no vehicle setting until 2.0.",
   open="Whether Chapter F was amended after April 2022. Which Jekyll roads are state highway system (PTVs barred) is not named on the page."),
 "st-simons-island": dict(conf="Medium", checked="Research 2026-10-15. This run 2026-10-15: re-read county LSV/PTV page; SSI speed map (June 2025) answers 200.",
   mismatch="County cap 25 mph; SlowGo allows 35. Bike paths closed to carts.",
   open="CONTESTED?: research lead (Brunswick News) mentions a county moratorium on a new golf cart ordinance, date unknown; ordinance ch. 2-15 art. III not read (Municode). Ask Ron whether a local should confirm before publishing."),
 "tybee-island": dict(conf="Medium", checked="Research 2026-10-15. This run 2026-10-15: re-read city cart page and the city flyer PDF (PDF metadata 2022-03-22; flyer undated).",
   mismatch="Highway 80 closure not modelled.",
   open="Code sec. 66-8 not read (Municode). Flyer says 'Tybee Island Police Department' registers carts, city page says Parking Services; page uses Parking Services. Crossing 'south of Park of 7 Flags' quoted as written (ambiguous)."),
 "gulf-breeze": dict(conf="Medium (THIN)", checked="Research 2026-10-15. This run 2026-10-15: re-read city 'Golf Carts and The Loop' page.",
   mismatch="Under-25 rule not modelled; The Loop LSV ban not modelled.",
   open="THIN: ordinance number unknown; only the city page. 'Posted under 25 mph' read literally excludes 25 mph streets: ask the city. Age rule (15+ with learner's permit) is the city's wording and may conflict with state 316.212(7). The map is hosted by a third party (Diamond Maps), so it is not linked."),
}


NEEDS_RON = [
 "Go on one bundled deploy (counted Netlify deploy): this branch + the /t/ links in link.mjs + the _redirects rewrites below. /t/... returns home or 404 until link.mjs has the list, so the pages and the links must ship together.",
 "Layout restored to the original drafts (37c0472) per Ron 2026-10-17, with only the 7 additions; check.py fails if any other line differs from the original page.",
 "Heading 'Official sources' is back (original wording, latest ruling). An earlier ruling said no 'official' wording beyond the required sentence; the restored closing also says 'official sources above'. Confirm.",
 "St. Simons Island map line reads 'See Glynn County's speed limit map for St. Simons.' (coordinator's wording, not the 'official golf cart map' template), because it is the county's speed-limit map. Confirm.",
 "Captiva and Gulf Breeze are HELD. Their files still sit in the publish folder: noindex and unlinked, but reachable by direct URL. Say if they should move out of SlowGo-Launch before the deploy.",
 "Titles use the two-letter state (FL, GA); the visible heading is the original 'Golf carts in [Town]'. Meta description = the page's lede.",
 "Structured data is plain WebPage (name = heading, description = lede), not FAQPage: the restored pages have no question-and-answer text, so FAQ markup would not match what is visible.",
 "Town pages no longer link to /cart-rules (the original header had only 'Back to SlowGo'); the hub links to them and the sitemap lists all. A home-page or footer link is a shared-file change for the other website branch.",
 "St. Simons Island: the earlier research found a news mention of a county moratorium on a new golf cart ordinance (date unknown). Ruled into the publish set; flagging once more.",
 "slowgo-report needs a small change before the first /t/ visit (otherwise /t/dunedin shows as /f/t-dunedin).",
]
LEGAL = [
 "Each page is our own plain-words summary of published rules with a short independence line ('not affiliated with ...') and the original closing ('It isn't legal advice'). The longer 'not endorsed by' sentence was dropped by ruling. Ron's self-review: enough with no attorney spend?",
 "Pages state rules as facts (fees, ages, closed roads). If a town changes its rules, the page is wrong until we re-check; 'Rules checked October 2026', the signs box and the town-staff email are the mitigation. No re-check schedule is set.",
 "Several rules rest on sources we could not read in full (city codes on Municode, which no agent reads): Dunedin, St. Simons Island and Tybee lean on city/county summary pages.",
 "Tybee page repeats the city flyer's penalty line (fines up to $1,000 or 12 months in jail) as 'the city's flyer says'.",
]

rows = []
for t in TOWNS:
    r = REVIEW[t["slug"]]
    rows.append(dict(town=t["name"], place=t["place"], status="PUBLISH SET" if t["publish"] else "HELD (noindex, not in hub or sitemap)",
        file=f"SlowGo-Launch/golf-carts/{t['slug']}.html", path=f"/golf-carts/{t['slug']}", counted_link=f"/t/{t['slug']}" if t["publish"] else "",
        phone=f"screens/{t['slug']}-phone.png", desktop=f"screens/{t['slug']}-desktop.png",
        sources=" ; ".join(f"{html.unescape(n)} <{u}>" for n, u in t["sources"]),
        rules_checked_on_page=UPDATED, checked_detail=r["checked"], confidence=r["conf"],
        slowgo_mismatch=r["mismatch"], open_questions=r["open"]))

with open(os.path.join(out, "review-sheet.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

e = html.escape
trs = "\n".join(
  f"<tr><td><strong>{e(r['town'])}</strong><br><small>{e(r['place'])}</small><br><code>{e(r['path'])}</code>"
  f"{'<br><code>' + e(r['counted_link']) + '</code>' if r['counted_link'] else ''}</td>"
  f"<td>{e(r['status'])}</td><td><a href='{r['phone']}'>phone</a> &middot; <a href='{r['desktop']}'>desktop</a></td>"
  f"<td>{e(r['confidence'])}</td><td><ul>{''.join(f'<li><a href={chr(39)}{u}{chr(39)}>{n}</a></li>' for n, u in t['sources'])}</ul></td>"
  f"<td>{e(r['checked_detail'])}</td><td>{e(r['slowgo_mismatch'])}</td><td>{e(r['open_questions'])}</td></tr>"
  for r, t in zip(rows, TOWNS))
li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Town pages review</title>
<style>
:root{{--bg:#FBF7EF;--fg:#1E3A2B;--mut:#5B7A5F;--line:#d8cfbf;--acc:#C8853A}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0B1F15;--fg:#F4EDE0;--mut:#A09484;--line:#2b4034;--acc:#E0A969}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 -apple-system,system-ui,sans-serif;margin:0;padding:24px 16px}}
h1,h2{{font-family:Georgia,serif;font-weight:500}} a{{color:inherit;text-decoration-color:var(--acc)}}
.wrap{{max-width:1400px;margin:0 auto}} .scroll{{overflow-x:auto}} pre{{overflow-x:auto;font-size:12.5px;border:1px solid var(--line);padding:12px}}
table{{border-collapse:collapse;width:100%;min-width:1100px}} th,td{{border-top:1px solid var(--line);padding:10px 8px;vertical-align:top;text-align:left}}
th{{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut)}} td ul{{margin:0;padding-left:1.1em}} small{{color:var(--mut)}}
.thumbs{{display:flex;gap:12px;overflow-x:auto}} .thumbs a{{flex:0 0 auto;text-align:center;font-size:12px}} .thumbs img{{width:140px;display:block;border:1px solid var(--line)}}
</style></head><body><div class="wrap">
<h1>Golf carts in [town]: 8 pages + hub, original layout restored (2026-10-17)</h1>
<p>Website repo, local branch <code>drafts/town-pages-2026-10-16</code> (worktree ~/dev/SlowGo-Website-drafts), not pushed, not deployed.
Generator: <code>tools/town-pages/</code> (towns.py = content, build.py = pages + hub + sitemap, check.py = rulings checklist incl. a line-by-line diff against the original drafts 37c0472, review.py = this sheet).
The 8 published pages and the hub have no noindex and are in sitemap.xml on the branch; nothing is live until Ron's go on a bundled deploy.
Screenshots: headless Chrome at 375 px (phone, 2x) and 1280 px (desktop), full page; no horizontal scroll at 375 px on any page.</p>
<h2>Hub</h2><p><code>/cart-rules</code> &middot; <a href="screens/cart-rules-phone.png">phone</a> &middot; <a href="screens/cart-rules-desktop.png">desktop</a></p>
<div class="thumbs">{''.join(f"<a href='screens/{s}-phone.png'><img src='screens/{s}-phone.png' alt=''>{s}</a>" for s in ['cart-rules'] + [t['slug'] for t in TOWNS])}</div>
<h2>Pages</h2>
<div class="scroll"><table><thead><tr><th>Town / path</th><th>Status</th><th>Screens</th><th>Sourcing</th><th>Sources (on the page)</th><th>Checked</th><th>SlowGo mismatch</th><th>Open questions</th></tr></thead>
<tbody>{trs}</tbody></table></div>
<h2>Links and redirects the deploy needs (the other website branch adds them)</h2>
<pre>{e(links_text([t for t in TOWNS if t['publish']]))}</pre>
<h2>Needs Ron</h2><ul>{li(NEEDS_RON)}</ul>
<h2>LEGAL</h2><ul>{li(LEGAL)}</ul>
</div></body></html>"""
with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
    f.write(page)
print("wrote", out)
