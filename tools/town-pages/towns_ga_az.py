# Georgia and Arizona town pages (scale-up, 2026-10-17). Same schema as towns.py.
# Content only from the cart-towns database (cart-towns-2026-10-16.csv, rows cited in db_row) and the
# sources listed on each page. Georgia state law per docs/research/georgia-cart-code-2026-10-16.md
# (read from the enacted bills on legis.ga.gov, not the compiled code). No Municode, no LexisNexis.
from towns import GA_HB877, GA_DPS

GA_LSV = ("<p>A low-speed vehicle (LSV) is a separate class under Georgia law: four wheels, a top speed over 20 mph and up to 25, "
          "built or converted to the federal LSV standard. LSVs are registered and insured like other vehicles and can use roads "
          "posted 35 mph or less. An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>")

TOWNS = [
 dict(
  slug="peachtree-city", name="Peachtree City", st="GA", state="Georgia", place="Peachtree City, Georgia",
  org="the City of Peachtree City", Org="The City of Peachtree City", publish=True,
  official=("the city&rsquo;s Paths and Golf Carts page", "https://peachtree-city.org/216/Paths-Golf-Carts"),
  hub="100+ miles of shared-use paths. City decal; non-residents pay a path fee.",
  answer="Peachtree City is built around more than 100 miles of shared-use paths that carts share with walkers and bikes. "
         "Carts must be registered with the city, and non-residents also pay a yearly path user fee.",
  faq=dict(
   license="<p>The city pages we read don&rsquo;t state a license rule for cart drivers. Under Georgia law, a cart driver (a PTV driver) needs a valid "
           "driver&rsquo;s license unless the town&rsquo;s ordinance allowed unlicensed drivers before 2012. Peachtree City&rsquo;s own code sets its rules; "
           "we haven&rsquo;t read it, so check with the city.</p>",
   age="<p>The owner must be 18 or older to register a cart. Driver ages aren&rsquo;t on the city pages we read.</p>",
   permit="<p>Yes. Register the cart with the city within 10 days of buying it. Owners must be 18 or older. The fee is $15 a year; residents pay three years "
          "at once ($45 for 2026&ndash;2028). Non-residents also pay a $235 path user fee. From 2026 the decal goes on the front and the rear. "
          "Handicap stickers are free with registration.</p>"
          "<p>To be registered, a cart must weigh under 1,300 lb, be no wider than 50 inches, and not be able to go faster than 20 mph.</p>",
   where="<p>The city&rsquo;s <strong>shared-use path system</strong>: more than 100 miles of paths, with tunnels and bridges. Carts don&rsquo;t have the "
         "right of way on paths, roads or crosswalks.</p>"
         "<p>The rules for carts on city streets are in the city code, which we haven&rsquo;t read. Under Georgia law, a cart may cross a state highway "
         "such as GA 54 or GA 74 only at a crossing the state has designated and signed for carts.</p>",
   lsv="<p>LSVs may use the shared-use paths only if they&rsquo;re limited to 20 mph. They must be registered and insured with the state, tagged through "
       "Fayette County, driven by a licensed driver, and carry an amber strobe light.</p>" + GA_LSV,
   hours="<p>The city pages we read don&rsquo;t set cart hours. Georgia law requires head lamps and tail lamps on carts used under a town&rsquo;s cart rules.</p>",
  ),
  extra=[],
  sources=[
   ("Paths &amp; Golf Carts &mdash; City of Peachtree City", "https://peachtree-city.org/216/Paths-Golf-Carts"),
   ("Shared-Use Path System &mdash; City of Peachtree City", "https://peachtree-city.org/1187/Shared-Use-Path-System"),
   GA_HB877, GA_DPS,
  ],
  street_map=("Peachtree City&rsquo;s multi-use path system map (2022 master plan update, as of March 2022)", "https://peachtree-city.org/DocumentCenter/View/19957",
              "It shows existing and proposed paths, not which streets carts may use."),
  slowgo="It also uses cart paths it knows about. It doesn&rsquo;t know Peachtree City&rsquo;s street rules "
         "or which crossings of GA 54 and GA 74 are signed for carts, so cross those roads only at a signed cart crossing.",
  prio="cart-friendly", prio_note="Georgia's best-known golf cart town (path system)", quality="medium",
  source_type="city website", checked="2026-10-15",
  gap="Street rules, driver ages and crossing rules are in the city code (Municode, not read); pages read cover paths, registration and LSV path use. Map PDF (DocumentCenter/View/19957) opened 2026-10-16: 'Multi-Use Path System 2022 Master Plan Update, as of March 2022', legend Complete/Existing/Proposed/Removed with project numbers; a planning map, labelled as such.",
  db_row=147,
 ),
 dict(
  slug="port-wentworth", name="Port Wentworth", st="GA", state="Georgia", place="Port Wentworth, Georgia",
  org="the City of Port Wentworth", Org="The City of Port Wentworth", publish=True,
  official=("the city&rsquo;s cart and LSV ordinance (PDF)", "https://portwentworthga.gov/wp-content/uploads/2024/04/Ordinance-No-20-04.pdf"),
  hub="City roads posted 25 mph or less, minus a list of busy roads. Yearly police registration; 16+ licensed.",
  answer="Port Wentworth lets registered carts (PTVs) and low-speed vehicles use city roads posted 25 mph or less and signed recreation paths, "
         "except a list of busier roads. Drivers must be 16 or older with a driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Drivers need a valid driver&rsquo;s license. A learner&rsquo;s permit holder may drive with a licensed driver 18 or older in the front seat.</p>",
   age="<p>At least <strong>16</strong>, with a valid driver&rsquo;s license (or a learner&rsquo;s permit with a licensed adult 18+ in the front seat).</p>",
   permit="<p>Yes. Register every year with the Port Wentworth Police Department: $15 ($20 late; renew by February 1). The person registering must be 18 or older "
          "and bring a copy of the insurance. The cart is inspected, and the decal goes on the front left. Liability insurance is required.</p>"
          "<p>Equipment includes brakes, a reverse warning device, head lamps, tail lamps, reflectors and a horn.</p>",
   where="<p>City public roads posted <strong>25 mph or less</strong>, other roads the City Council approves, and signed recreation paths. "
         "Use a path instead of a road that runs alongside it. No sidewalks, except the Highway 25 Viaduct.</p>"
         "<p>Not allowed, except to cross at the listed places: US 21, GA 25, GA 30, Grange Road, Crossgate Road (GA 25 to US 21), "
         "Bonnybridge Road (GA 25 to US 21), Meinhard Road, Monteith Road, Henderson Boulevard and Benton Boulevard.</p>",
   lsv="<p>Port Wentworth treats low-speed vehicles the same as carts: the same roads, registration and license rules. "
       "(Under Georgia law in general, an LSV has a top speed over 20 mph and up to 25, and can use roads posted 35 mph or less.) An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   hours="<p>We didn&rsquo;t find cart hours in the ordinance. Carts must have head lamps and tail lamps.</p>",
  ),
  extra=[
   ("Crossings",
    "<p>Carts may cross only at:</p>"
    "<ul><li>GA 25 at Phillips Avenue/Coleraine Drive, Armadale Road, Barnsley Road, Dorset Road and Appleby Road</li>"
    "<li>Crossgate Road at Cantyre Street and Falkirk Street</li>"
    "<li>Benton Boulevard at Red Robin Court</li>"
    "<li>either side of the Highway 25 Viaduct (Dorset Road to Appleby Road), with traffic</li></ul>"),
   ("On the road",
    "<p>One person per seat. Keep to the right. Don&rsquo;t park on streets posted over 25 mph. ATVs aren&rsquo;t allowed.</p>"),
  ],
  sources=[
   ("Ordinance 20-04, Personal Transportation and Low Speed Vehicle Ordinance &mdash; City of Port Wentworth (PDF)", "https://portwentworthga.gov/wp-content/uploads/2024/04/Ordinance-No-20-04.pdf"),
   GA_HB877, GA_DPS,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know Port Wentworth&rsquo;s 25 mph line or its crossing list yet, "
         "so a route can use a 30 or 35 mph road or cross where carts can&rsquo;t. Check the lists above before you ride.",
  prio="cart-friendly", prio_note="Coastal Georgia (Savannah area) cart town with a full ordinance", quality="high",
  source_type="ordinance PDF (city site)", checked="2026-10-16",
  gap="Ordinance read in full; the CSV row has no hours rule, so the page has no hours section beyond equipment (FAQ hours answer says so).",
  db_row=148,
 ),
 dict(
  slug="rome", name="Rome", st="GA", state="Georgia", place="Rome, Georgia",
  org="the City of Rome", Org="The City of Rome", publish=True,
  official=("the city&rsquo;s Personal Transportation Vehicle page", "https://www.romega.us/585/Personal-Transportation-Vehicle-PTV"),
  hub="Designated 25 mph zones only. Police inspection and registration; 18+.",
  answer="In Rome, carts (PTVs under Georgia law) must be inspected and registered with the Rome Police Department, "
         "and they may be used only in designated 25 mph zones.",
  faq=dict(
   license="<p>The city&rsquo;s page sets an age of 18. Under Georgia law, a cart driver also needs a valid driver&rsquo;s license unless a town&rsquo;s "
           "ordinance allowed unlicensed drivers before 2012.</p>",
   age="<p>At least <strong>18</strong>, according to the city&rsquo;s page.</p>",
   permit="<p>Yes. Have the cart inspected and registered at the Rome Police Department: $15 (a replacement decal is $15). The decal goes on the rear, "
          "driver&rsquo;s side. Proof of liability insurance is required.</p>"
          "<p>The cart must weigh under 1,375 lb, go no faster than 20 mph and carry no more than eight people.</p>",
   where="<p>Only in the city&rsquo;s <strong>designated 25 mph zones</strong>. The pages we read don&rsquo;t list the zones; ask the city.</p>",
   lsv=GA_LSV,
   hours="<p>The city&rsquo;s page doesn&rsquo;t set cart hours or list equipment. Georgia law requires head lamps and tail lamps on carts used under a "
         "town&rsquo;s cart rules.</p>",
  ),
  extra=[],
  sources=[
   ("Personal Transportation Vehicle (PTV) &mdash; City of Rome", "https://www.romega.us/585/Personal-Transportation-Vehicle-PTV"),
   ("PTV Registration Form (2024) &mdash; City of Rome (PDF)", "https://www.romega.us/DocumentCenter/View/3196/PTV-Registration-Form-2024"),
   GA_HB877, GA_DPS,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know where Rome&rsquo;s 25 mph cart zones are yet, "
         "so a route can leave them. Ask the city where the zones are before you ride.",
  prio="cart-friendly", prio_note="Georgia city with a PTV registration program", quality="medium",
  source_type="city page + registration form", checked="2026-10-16",
  gap="Zone locations, hours and equipment list not on the pages read; code secs. 12-380 to 12-387 not read (ordinance date unknown).",
  db_row=149,
 ),
 dict(
  slug="woodstock", name="Woodstock", st="GA", state="Georgia", place="Woodstock, Georgia",
  org="the City of Woodstock", Org="The City of Woodstock", publish=True,
  official=("the city&rsquo;s PTV registration page", "https://www.woodstockga.gov/your_government/departments/community_development/ptv_registration.php"),
  hub="Registered PTVs on city streets posted 25 mph or less. $15 decal; licensed drivers.",
  answer="Woodstock lets registered personal transportation vehicles (PTVs, also called modified golf carts) use city streets posted 25 mph or less, "
         "with a licensed driver. Plain golf carts that top out around 15 mph aren&rsquo;t allowed on any road.",
  faq=dict(
   license="<p>Yes. Only licensed drivers may drive a PTV on city streets.</p>",
   age="<p>The city ties driving to the license: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. Register the PTV with the city: $15, with a decal on the driver&rsquo;s side rear fender.</p>"
          "<p>Equipment: brakes including a parking brake, a reverse warning device, a main power switch, head lamps, tail lamps, reflectors, a horn, "
          "a mirror, warning labels, hip restraints or hand holds, and lap belts for riders 15 and under.</p>",
   where="<p>City streets posted <strong>25 mph or less</strong>. Park only in marked spaces.</p>",
   lsv="<p>Woodstock separates PTVs from plain golf carts: a golf cart built for about 15 mph may not be driven on any road. A PTV goes up to 20 mph.</p>" + GA_LSV,
   hours="<p>The city&rsquo;s page doesn&rsquo;t set hours. Every PTV must have head lamps and tail lamps.</p>",
  ),
  extra=[
   ("On the road", "<p>Everyone rides seated, with no one on laps. Riders 15 and under wear lap belts.</p>"),
  ],
  sources=[
   ("PTV Registration &mdash; City of Woodstock", "https://www.woodstockga.gov/your_government/departments/community_development/ptv_registration.php"),
   GA_HB877, GA_DPS,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know Woodstock&rsquo;s 25 mph line yet, "
         "so a route can include a 30 or 35 mph street that PTVs can&rsquo;t use.",
  prio="cart-friendly", prio_note="Metro Atlanta city with a PTV program", quality="medium",
  source_type="city website (read directly)", checked="2026-10-16",
  gap="Code ch. 42, art. V (Municode) not read; city's ArcGIS map exists but its content wasn't described, so no map line.",
  db_row=160,
 ),
 dict(
  slug="marana", name="Marana", st="AZ", state="Arizona", place="Marana, Arizona",
  org="the Town of Marana", Org="The Town of Marana", publish=True,
  official=("the town&rsquo;s &ldquo;Is Your Golf Cart Street Legal?&rdquo; notice", "https://www.maranaaz.gov/Newsroom-Entries/2025/Is-Your-Golf-Cart-Street-Legal"),
  publishes="The Town of Marana&rsquo;s police department publishes guidance on golf carts. Here&rsquo;s a plain-English summary.",
  hub="Road carts need MVD registration, insurance and a licensed driver. Not on sidewalks or paths.",
  answer="In Marana, a golf cart on a public road must be registered with the Arizona MVD, insured, equipped for the road and driven by a licensed driver. "
         "Carts aren&rsquo;t allowed on sidewalks or multi-use paths.",
  faq=dict(
   license="<p>Yes. The town police say carts on public roads must be driven by a licensed driver.</p>",
   age="<p>The rule is tied to the license: the driver must be licensed.</p>",
   permit="<p>Yes. A cart used on public roads must be registered with the Arizona MVD and insured. That follows state law: a golf cart is exempt from "
          "registration only on a golf course or when it&rsquo;s only incidentally on a highway.</p>",
   where="<p>The town police say carts may use only public streets posted <strong>35 mph or less</strong>. That 35 mph line is the police notice&rsquo;s "
         "wording; we didn&rsquo;t find it in Arizona&rsquo;s statutes, which set 35 mph only for neighborhood electric vehicles.</p>"
         "<p>No carts on sidewalks or multi-use paths.</p>",
   lsv="<p>Arizona law calls street-legal electric low-speed vehicles neighborhood electric vehicles (NEVs). An NEV tops out at 25 mph and must carry a notice "
       "of its limits. Under &sect; 28-966, an NEV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   hours="<p>The police notice doesn&rsquo;t set hours. It says a cart must be properly equipped for road use.</p>",
  ),
  extra=[],
  sources=[
   ("Is Your Golf Cart Street Legal? (December 17, 2025) &mdash; Town of Marana", "https://www.maranaaz.gov/Newsroom-Entries/2025/Is-Your-Golf-Cart-Street-Legal"),
   ("Arizona Revised Statutes &sect; 28-2153 &mdash; registration exemptions", "https://www.azleg.gov/ars/28/02153.htm"),
   ("Arizona Revised Statutes &sect; 28-966 &mdash; neighborhood electric vehicles", "https://www.azleg.gov/ars/28/00966.htm"),
  ],
  street_map=None,
  slowgo="It also uses cart paths it knows about. It doesn&rsquo;t know that Marana keeps carts off "
         "multi-use paths, so if a route uses a path here, don&rsquo;t take it in a cart.",
  prio="retirement", prio_note="Tucson-area town with active-adult communities; the only Arizona town row with a town source", quality="medium",
  source_type="town police news post", checked="2026-10-15",
  gap="Only source is a police news post; the 35 mph line is the police's wording, not found in statute (flagged on the page). No town ordinance found.",
  db_row=15,
 ),
]
