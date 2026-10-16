# Content for the "Golf Cart Rules in [Town]" pages.
#
# History: 10 drafts written 2026-10-16 (sources read 2026-10-15); restructured 2026-10-16/17 for
# Ron's town-page rulings: FAQ headings (license, age, permits, where, golf cart vs LSV, hours and
# lights), independence line at the top, our own schematic diagram, per-town counted link /t/<slug>.
#
# Rules for editing this file:
# - Every rule comes from a source listed on the same page (official city/county/state sites and
#   PDFs only; no realtor, tourism or news sites). No agent reads Municode or LexisNexis.
# - Our own plain-language words. Short quotes only, if any.
# - No town logos or seals, and never call a page "official".
# - publish=False keeps a page out of the hub and the sitemap and keeps it noindex (Ron 2026-10-17:
#   Captiva and Gulf Breeze are HELD).

FL_316212 = ("Florida Statutes &sect; 316.212 &mdash; golf carts on roads",
             "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0316/Sections/0316.212.html")
FL_3162122 = ("Florida Statutes &sect; 316.2122 &mdash; low-speed vehicles",
              "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0316/Sections/0316.2122.html")
GA_HB877 = ("Georgia HB 877 (2014), the enacted bill that set the state&rsquo;s cart (PTV) rules &mdash; Georgia General Assembly",
            "https://www.legis.ga.gov/api/legislation/document/20132014/144917")
GA_DPS = ("Georgia Code: low-speed vehicles &mdash; Georgia Department of Public Safety",
          "https://dps.georgia.gov/georgia-code-low-speed-vehicles")

FL_LSV = ("<p>A low-speed vehicle (LSV) is different from a golf cart: it goes faster than 20 mph (up to 25), "
          "and it has to be titled, registered and insured, with a licensed driver. Under Florida law an LSV can use "
          "streets posted 35 mph or less and can cross faster roads at intersections, unless the local government "
          "has closed a road to them.</p>")

# FAQ keys, in page order, with the question each one asks. {n} is the town's short name.
FAQ_ORDER = [
    ("license", "Do you need a driver&rsquo;s license to drive a golf cart in {n}?"),
    ("age",     "How old do you have to be to drive a golf cart in {n}?"),
    ("permit",  "Does a golf cart need a permit or registration in {n}?"),
    ("where",   "Where can golf carts go in {n}?"),
    ("lsv",     "Golf cart or LSV: what&rsquo;s the difference in {n}?"),
    ("hours",   "Can you drive a golf cart at night in {n}? Hours and lights"),
]

# Map spec (drawn by build.py as an inline SVG schematic, never a copy of anyone's map):
#   area  label for the shaded area      ok    what the green streets mean
#   bars  roads closed to carts: orient h|v, pos 0..1 across the area, name, cross dots|x|None,
#         count (number of crossing marks), half (draw only from the middle to the right/bottom)
#   paths text for the dashed "no carts" path, or None
#   cross_note  legend text for the crossing marks

TOWNS = [
 dict(
  slug="st-pete-beach", name="St. Pete Beach", st="FL", state="Florida", place="St. Pete Beach, Florida",
  org="the City of St. Pete Beach", Org="The City of St. Pete Beach", publish=True,
  official=("the city&rsquo;s Golf Carts page", "https://www.stpetebeach.org/498/Golf-Carts"),
  hub="City streets posted 25 mph or less. City decal; driver&rsquo;s license required.",
  answer="St. Pete Beach lets golf carts use its quieter city streets: the ones posted 25 mph or less. "
         "Carts need a city registration and decal, and the driver needs a driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Only people with a <strong>valid driver&rsquo;s license</strong> may drive a cart on city streets. "
           "That&rsquo;s stricter than Florida&rsquo;s general rule, which lets 18-year-olds drive a cart with just a photo ID.</p>",
   age="<p>The city ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. Resident-owned carts are registered with the city every year ($10, paid at City Hall), and the decal goes on the back, "
          "driver&rsquo;s side. You&rsquo;ll need proof of a valid driver&rsquo;s license and a signed statement that the cart has liability insurance "
          "(a rider on a homeowner&rsquo;s policy or a separate policy). The cart can&rsquo;t be able to go faster than 20 mph.</p>"
          "<p>Daytime equipment: good brakes, reliable steering, safe tires, a horn, a rearview mirror, and red reflectors front and rear.</p>",
   where="<p>City streets posted <strong>25 mph or less</strong>, inside the area shown on the city&rsquo;s map. "
         "Carts can&rsquo;t drive on or cross state or county roads unless the state or Pinellas County allows it at that spot. "
         "Gulf Boulevard is a state road.</p>"
         "<p>No carts on sidewalks, in parks, on beaches or on other city land.</p>",
   lsv=FL_LSV,
   hours="<p>Sunrise to sunset only, unless the cart also has headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[],
  sources=[
   ("Golf Carts &mdash; City of St. Pete Beach", "https://www.stpetebeach.org/498/Golf-Carts"),
   ("Ordinance 2013-17 (City Code ch. 82, art. VI) &mdash; City of St. Pete Beach (PDF)", "https://www.stpetebeach.org/DocumentCenter/View/1021/Golf-Cart-Ordinance-PDF"),
   ("Restricted roadways map &mdash; City of St. Pete Beach", "https://www.stpetebeach.org/ImageRepository/Document?documentID=884"),
   FL_316212, FL_3162122,
  ],
  street_map=("the city&rsquo;s restricted roadways map", "https://www.stpetebeach.org/ImageRepository/Document?documentID=884"),
  map=dict(area="St. Pete Beach (city limits)", ok="City streets posted 25 mph or less",
           bars=[dict(orient="h", pos=.42, name="Gulf Blvd (state road)", cross="dots", count=2),
                 dict(orient="v", pos=.72, name="Streets over 25 mph", cross=None)],
           cross_note="Crossing only where the state or county allows it",
           paths="Sidewalks, parks, beaches: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know St. Pete Beach&rsquo;s 25 mph line yet, "
         "so a route here can include a 30 or 35 mph street that carts can&rsquo;t use. Check the city&rsquo;s map before you ride.",
 ),
 dict(
  slug="dunedin", name="Dunedin", st="FL", state="Florida", place="Dunedin, Florida",
  org="the City of Dunedin", Org="The City of Dunedin", publish=True,
  official=("the city&rsquo;s Golf Carts page", "https://www.dunedin.gov/Activities-and-Recreation/Getting-Around/Golf-Carts"),
  hub="A cart zone of city streets posted 30 mph or less. No city sticker for 20 mph carts.",
  answer="Dunedin has a golf cart zone: designated city streets posted 30 mph or less. "
         "There&rsquo;s no city sticker or fee for carts that top out at 20 mph.",
  faq=dict(
   license="<p>Not always. Under 18, the driver needs a learner&rsquo;s permit or a driver&rsquo;s license. "
           "At 18 and over, a government-issued photo ID is enough. (This is Florida&rsquo;s rule, which the city follows.)</p>",
   age="<p>The city follows Florida&rsquo;s rule: drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license, "
       "and drivers 18 and over need a government-issued photo ID.</p>",
   permit="<p>No city registration, sticker or fee for carts that can&rsquo;t go faster than 20 mph. The Pinellas County Sheriff enforces the state&rsquo;s cart rules.</p>"
          "<p>Equipment: reliable steering, good brakes, safe tires, a rearview mirror, and red reflectors front and rear.</p>",
   where="<p>Designated city streets in the cart zone, and only roads posted <strong>30 mph or less</strong>. The city&rsquo;s online map shows the zone.</p>"
         "<p>State and county roads can be crossed only at marked golf cart crossings.</p>"
         "<p>No carts on the Pinellas Trail, sidewalks, in parks or on other city property unless a spot is set aside for them. "
         "Highlander Park is one: carts stay on its shell path and park where the park&rsquo;s cart map shows.</p>",
   lsv="<p>A low-speed vehicle (LSV) goes faster than a golf cart (over 20 mph, up to 25) and needs a state license and registration, as the city&rsquo;s page notes. "
       "Under Florida law LSVs can use streets posted 35 mph or less.</p>",
   hours="<p>At night a cart also needs headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Parking",
    "<p>Use golf cart spaces where there are some. Otherwise two carts park side by side in one car space. During downtown events, carts park in vehicle spaces only.</p>"),
  ],
  sources=[
   ("Golf Carts &mdash; City of Dunedin", "https://www.dunedin.gov/Activities-and-Recreation/Getting-Around/Golf-Carts"),
   ("Golf cart zone map &mdash; City of Dunedin GIS", "https://gis.dunedingov.com/portal/apps/webappviewer/index.html?id=c3f6c0aacba64efb87f795bf3eb195ea"),
   FL_316212, FL_3162122,
  ],
  street_map=("the city&rsquo;s cart zone map", "https://gis.dunedingov.com/portal/apps/webappviewer/index.html?id=c3f6c0aacba64efb87f795bf3eb195ea"),
  map=dict(area="Dunedin golf cart zone", ok="Designated streets in the zone, posted 30 mph or less",
           bars=[dict(orient="h", pos=.42, name="State or county road", cross="dots", count=2),
                 dict(orient="v", pos=.72, name="Streets over 30 mph", cross=None)],
           cross_note="Marked golf cart crossing",
           paths="Pinellas Trail, sidewalks: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Dunedin&rsquo;s cart zone or its 30 mph line yet, "
         "so a route can leave the zone or use a 35 mph street. Check the city&rsquo;s map before you ride.",
 ),
 dict(
  slug="mount-dora", name="Mount Dora", st="FL", state="Florida", place="Mount Dora, Florida",
  org="the City of Mount Dora", Org="The City of Mount Dora", publish=True,
  official=("the city&rsquo;s Golf Cart Registration page", "https://www.mountdora.gov/1457/Golf-Cart-Registration"),
  hub="Every city street except a short list of busier roads, around the clock. City permit.",
  answer="In Mount Dora, a permitted golf cart can use every city street except a short list of busier roads, "
         "around the clock. Carts need a city permit, and drivers under 18 need a learner&rsquo;s permit or license.",
  faq=dict(
   license="<p>Not at 18 and over: every driver carries a government-issued photo ID, and drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license.</p>",
   age="<p>Drivers must be 18, unless they have a learner&rsquo;s permit or driver&rsquo;s license.</p>",
   permit="<p>Yes. A city golf cart permit is required: $25 to register, $10 a year to renew. Bring the application, the affidavit, proof of insurance "
          "and a copy of your license to the Police Department (or email them). The sticker goes on the lower driver&rsquo;s side bumper or fender. "
          "Country Club of Mount Dora and private or gated communities inside the city don&rsquo;t need it.</p>"
          "<p>Required equipment: windshield; driver&rsquo;s side mirror plus an inside or passenger-side mirror; headlights and tail lights; brakes and a parking brake; "
          "front and rear turn signals; steering; rear and side reflectors; a horn; and grab bars on rear-facing seats.</p>",
   where="<p><strong>All city streets</strong>, except:</p>"
         "<ul><li>all county roads and state highways, and streets outside city limits</li>"
         "<li>US 441, SR 44, SR 46, CR 19A, Old Highway 441, Old Eustis Road, Eudora Road, Round Lake Road, Limit Avenue, Wolf Branch Road, Robie Avenue and Britt Road</li>"
         "<li>5th Avenue from Highland Avenue to Old Highway 441; Highland Avenue from 5th Avenue to the Orange County line; "
         "1st Avenue from US 441 to Highland Avenue; Donnelly Street from US 441 to Limit Avenue</li></ul>"
         "<p>Carts may cross county roads at intersections. They may <strong>not</strong> cross US 441. "
         "No bike paths or sidewalks. Private streets and gated communities set their own rules.</p>",
   lsv="<p>A cart modified to go faster than 20 mph counts as a low-speed vehicle. It must be titled, registered and insured with the state, "
       "and it can&rsquo;t use sidewalks or streets posted over 35 mph.</p>",
   hours="<p>24 hours a day, except when the city closes a street for an event. Every permitted cart has headlights and tail lights (see the equipment list).</p>",
  ),
  extra=[
   ("Passengers", "<p>Passengers ride seated, no more than the cart is built for.</p>"),
  ],
  sources=[
   ("Golf Cart Registration &mdash; City of Mount Dora", "https://www.mountdora.gov/1457/Golf-Cart-Registration"),
   ("Golf Carts Street Usage list and map (May 17, 2023) &mdash; City of Mount Dora (PDF)", "https://www.mountdora.gov/DocumentCenter/View/16545"),
   FL_316212, FL_3162122,
  ],
  street_map=("the city&rsquo;s street usage list and map", "https://www.mountdora.gov/DocumentCenter/View/16545"),
  map=dict(area="Mount Dora (city limits)", ok="All other city streets",
           bars=[dict(orient="h", pos=.30, name="US 441", cross="x", count=3),
                 dict(orient="v", pos=.72, name="County road", cross="dots", count=2),
                 dict(orient="h", pos=.72, name="Listed streets", cross=None, half=True)],
           cross_note="Cross at intersections (county roads)", x_note="No crossing (US 441)",
           paths="Bike paths, sidewalks: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Mount Dora&rsquo;s not-allowed list yet, "
         "so a route could use one of those roads. Check the list above before you ride.",
 ),
 dict(
  slug="miami-lakes", name="Miami Lakes", st="FL", state="Florida", place="Miami Lakes, Florida",
  org="the Town of Miami Lakes", Org="The Town of Miami Lakes", publish=True,
  official=("the town&rsquo;s golf cart ordinance (PDF)", "https://www.miamilakes-fl.gov/wp-content/uploads/2023/10/Ordinance-ORD-22293.pdf"),
  hub="All town streets except NW 67th and NW 87th Avenues. Yearly inspection; driver&rsquo;s license.",
  answer="Miami Lakes opens all town streets to inspected, permitted golf carts, except NW 67th Avenue and NW 87th Avenue. "
         "Drivers need a valid driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Only people with a <strong>current, valid driver&rsquo;s license</strong> may drive a cart on town streets.</p>",
   age="<p>The town ties driving to the license rather than to an age: the driver needs a current, valid driver&rsquo;s license.</p>",
   permit="<p>Yes. Each cart is inspected by the town every year. Apply to the Town Police Department with proof of insurance and a $50 application fee; "
          "a cart that passes gets a permit with a registration number, shown where it&rsquo;s easy to see.</p>"
          "<p>Required equipment: good brakes, reliable steering, safe tires, rearview mirrors, red reflectors front and rear, brake lights, turn signals and seat belts. "
          "Carts built for speeds under 25 mph also need the orange slow-moving-vehicle triangle.</p>",
   where="<p><strong>All town streets except NW 67th Avenue and NW 87th Avenue.</strong> On those two, carts may only cross, at marked intersections or traffic lights.</p>"
         "<p>No carts in parks, on bike paths, sidewalks or swales. The town permit doesn&rsquo;t cover private property: shopping-center parking lots, "
         "private roads and condo common areas are up to their owners.</p>",
   lsv=FL_LSV,
   hours="<p>Between sunset and sunrise, only with headlights and a windshield.</p>",
  ),
  extra=[
   ("Passengers", "<p>No more passengers than the cart is built for, and state seat belt and child-seat rules apply.</p>"),
  ],
  sources=[
   ("Ordinance 22-293, adopted April 12, 2022 (Town Code ch. 39, art. III) &mdash; Town of Miami Lakes (PDF)", "https://www.miamilakes-fl.gov/wp-content/uploads/2023/10/Ordinance-ORD-22293.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  map=dict(area="Miami Lakes (town limits)", ok="All town streets",
           bars=[dict(orient="v", pos=.25, name="NW 87th Ave", cross="dots", count=2),
                 dict(orient="v", pos=.75, name="NW 67th Ave", cross="dots", count=2)],
           cross_note="Cross only at marked intersections or traffic lights",
           paths="Parks, bike paths, sidewalks, swales: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know that NW 67th and NW 87th Avenues are closed to carts here, "
         "so if a route runs along either one, don&rsquo;t take it in a cart.",
 ),
 dict(
  slug="pine-island", name="Pine Island", st="FL", state="Florida", place="Pine Island, Florida (Lee County)",
  org="Lee County", Org="Lee County", publish=True,
  official=("Lee County Ordinance 13-08 (PDF)", "https://www.leegov.com/bocc/Ordinances/13-08.pdf"),
  publishes="Lee County publishes the golf cart rules for Pine Island.",
  hub="Lee County roads on the island, minus a few busy stretches. Daylight only; driver&rsquo;s license.",
  answer="Lee County lets golf carts use its roads on Pine Island in daylight, with a few busy stretches left out. "
         "Drivers need a driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Only people with a <strong>valid driver&rsquo;s license</strong> from their home state or country may drive a cart on these roads.</p>",
   age="<p>The county ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>The county ordinance has no registration or sticker.</p>"
          "<p>Equipment: good brakes, reliable steering, safe tires, a rearview mirror, and red reflectors front and rear.</p>",
   where="<p>County-maintained streets on Pine Island (west of the St. James Creek Bridge), <strong>except</strong>:</p>"
         "<ul><li>Stringfellow Road from the Jug Creek Bridge in Bokeelia to St. Jude Boulevard in St. James City</li>"
         "<li>Pine Island Road east of Stringfellow Road</li></ul>"
         "<p>Lee County DOT signs the designated roads and posts golf cart crossings across Stringfellow and Pine Island Roads where it has approved them.</p>"
         "<p>No carts on bike paths, shared-use paths or sidewalks, or in the drainage and landscaped areas beside the road.</p>",
   lsv=FL_LSV,
   hours="<p><strong>Daylight only.</strong> The ordinance doesn&rsquo;t allow golf carts on public roads between sunset and sunrise.</p>",
  ),
  extra=[
   ("Passengers", "<p>Everyone rides seated, no more than the cart has seats, and nobody stands while it moves.</p>"),
  ],
  sources=[
   ("Lee County Ordinance 13-08, adopted April 23, 2013, with its Attachment A street list &mdash; Lee County (PDF)", "https://www.leegov.com/bocc/Ordinances/13-08.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  map=dict(area="Pine Island (Lee County roads)", ok="Other county streets on the island",
           bars=[dict(orient="v", pos=.45, name="Stringfellow Rd", cross="dots", count=2),
                 dict(orient="h", pos=.55, name="Pine Island Rd, east", cross=None, half=True)],
           cross_note="Golf cart crossing, where the county has posted one",
           paths="Bike paths, shared-use paths, sidewalks: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Pine Island&rsquo;s left-out stretches or the daylight rule yet, "
         "so check a route against the list above, and ride before sunset.",
 ),
 dict(
  slug="captiva", name="Captiva Island", st="FL", state="Florida", place="Captiva Island, Florida (Lee County)",
  org="Lee County", Org="Lee County", publish=False,
  official=("Lee County Ordinance 09-22 (PDF)", "https://www.leegov.com/bocc/Ordinances/09-22.pdf"),
  publishes="Lee County publishes the golf cart rules for Captiva Island.",
  hub="County roads Lee County DOT has signed for carts. Daylight; driver&rsquo;s license.",
  answer="On Captiva, golf carts can use the county roads that Lee County DOT has designated and signed for them, in daylight, "
         "with a licensed driver.",
  faq=dict(
   license="<p>Yes. Only people with a <strong>valid driver&rsquo;s license</strong> from their home state or country. "
           "Florida&rsquo;s late-night limits for young licensed drivers also apply to carts.</p>",
   age="<p>The county ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>The county ordinance has no registration or sticker. The cart can&rsquo;t be able to go faster than 20 mph. It needs good brakes, reliable steering, "
          "safe tires, a rearview mirror, and red reflectors front and rear.</p>",
   where="<p>County roads on Captiva that the <strong>Lee County Department of Transportation has designated</strong> for golf carts. "
         "The ordinance doesn&rsquo;t list the roads; the county signs the ones that are open to carts. If you don&rsquo;t see a sign, ask Lee County DOT.</p>",
   lsv=FL_LSV,
   hours="<p>Sunrise to sunset, unless Lee County DOT has designated a road for night use. Then the cart also needs headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[],
  sources=[
   ("Lee County Ordinance 09-22 (2009), golf carts on designated county roads on Captiva Island &mdash; Lee County (PDF)", "https://www.leegov.com/bocc/Ordinances/09-22.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  map=dict(area="Captiva Island (county roads)", ok="County roads signed for carts",
           bars=[dict(orient="h", pos=.5, name="Roads without a cart sign", cross=None)],
           cross_note=None, paths=None),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know which Captiva roads Lee County has signed for carts, "
         "so follow the signs over the route.",
 ),
 dict(
  slug="jekyll-island", name="Jekyll Island", st="GA", state="Georgia", place="Jekyll Island, Georgia",
  org="the Jekyll Island Authority", Org="The Jekyll Island Authority", publish=True,
  official=("the Authority&rsquo;s Chapter F rules (PDF)", "https://www.jekyllisland.com/wp-content/uploads/2022/04/Chapter-F-Streets-and-Rights-of-Way-042222.pdf"),
  publishes="The Jekyll Island Authority publishes its rules for golf carts and PTVs. Here&rsquo;s a plain-English summary.",
  hub="Street-legal PTVs on island streets (not state highways or paths). 16+ with a license.",
  answer="Jekyll Island is a little different. The street-legal carts most people drive count as personal transportation vehicles (PTVs) "
         "under Georgia law, and those are welcome on the island&rsquo;s streets. True golf carts, the kind built only for the golf course, are not.",
  faq=dict(
   license="<p>Yes. PTV drivers need a valid driver&rsquo;s license.</p>",
   age="<p>At least <strong>16</strong>, with a valid driver&rsquo;s license.</p>",
   permit="<p>No Glynn County registration is needed on Jekyll. The owner needs liability insurance at Georgia&rsquo;s minimum limits, with proof kept in the PTV.</p>"
          "<p>Required: brakes and a parking brake, a reverse warning, a main power switch, headlights and taillights, front and rear turn signals, brake lights, "
          "reflectors, a rearview mirror, a horn, hip restraints, hand holds, a seat belt for every seat, and the orange slow-moving-vehicle triangle on the back.</p>",
   where="<p>PTVs can use the island&rsquo;s public streets, but <strong>not</strong> roads that are part of the state highway system. "
         "No PTVs on sidewalks, bike paths, the pedestrian-only paths in the Historic District, unimproved trails, service roads or golf-cart paths.</p>"
         "<p>Park in regular vehicle spaces.</p>",
   lsv="<p>Georgia law draws the line by speed. A <strong>PTV</strong> has at least four wheels, a top speed under 20 mph, weighs no more than 1,375 lb empty and carries up to eight people. "
       "A <strong>golf cart</strong> is built only for golf and averages under 15 mph.</p>"
       "<p>On Jekyll, golf carts are not allowed on public streets or Authority property, except to cross a street while playing golf, "
       "or at a parade, festival or other event with the sponsor&rsquo;s OK. Privately owned carts aren&rsquo;t allowed on the Authority&rsquo;s golf courses.</p>"
       "<p>LSVs (low-speed vehicles) are registered and insured with the state, can use streets posted 35 mph or less, and are kept off the same paths as PTVs.</p>",
   hours="<p>Yes, with lights: PTV lights go on at night, in rain, or when you can&rsquo;t see 500 feet ahead.</p>",
  ),
  extra=[
   ("On the road",
    "<p>Everyone wears a seat belt, one person per belt. Children under 8 ride in a child seat (a seat belt is fine if they weigh at least 40 lb or are over 4&prime;9&Prime;). "
    "If two or more vehicles are behind you, pull over at the first safe spot. No passing in the same lane, and no riding two abreast.</p>"),
  ],
  sources=[
   ("Jekyll Island Authority Rules, Chapter F: Streets and Rights-of-Way (April 2022) &mdash; Jekyll Island Authority (PDF)", "https://www.jekyllisland.com/wp-content/uploads/2022/04/Chapter-F-Streets-and-Rights-of-Way-042222.pdf"),
   GA_HB877, GA_DPS,
  ],
  street_map=None,
  map=dict(area="Jekyll Island", ok="Island streets (PTVs)",
           bars=[dict(orient="h", pos=.4, name="State highway roads", cross=None)],
           cross_note=None,
           paths="Sidewalks, bike paths, trails, cart paths: no PTVs"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Jekyll&rsquo;s rules yet: if a route uses a path here, "
         "don&rsquo;t take it in a cart or LSV.",
 ),
 dict(
  slug="st-simons-island", name="St. Simons Island", st="GA", state="Georgia", place="St. Simons Island, Georgia (Glynn County)",
  org="Glynn County", Org="Glynn County", publish=True,
  official=("the county&rsquo;s LSV and PTV page", "https://www.glynncounty.org/government/departments/licensing-compliance/licenses-permits/low-speed-vehicles-lsv-personal-transportation-vehicles-ptv"),
  publishes="Glynn County publishes the golf cart rules for St. Simons Island.",
  hub="Public streets posted 25 mph or less. County decal; 16+ with a license.",
  answer="On St. Simons, and everywhere else in unincorporated Glynn County, a registered cart (a PTV under Georgia law) "
         "can use public streets posted 25 mph or less. Drivers must be 16 or older with a driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Drivers need a valid driver&rsquo;s license.</p>",
   age="<p>At least <strong>16</strong>, with a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. Register the cart with Glynn County before driving it on public streets: $15, good for five years or until the cart changes hands. "
          "The county decal goes on the driver&rsquo;s side, where it can always be seen.</p>",
   where="<p>Public streets posted <strong>25 mph or less</strong>. The county publishes a map of St. Simons roads by speed limit. "
         "No carts on sidewalks or bike paths, at any time.</p>",
   lsv="<p>A low-speed vehicle (top speed over 20, up to 25 mph) is registered with the Glynn County Tax Commissioner like any other vehicle, "
       "can use streets posted 35 mph or less, and isn&rsquo;t allowed on sidewalks or bike paths.</p>",
   hours="<p>Headlights and taillights go on whenever it isn&rsquo;t daylight.</p>",
  ),
  extra=[
   ("On the road",
    "<p>One person per seat, and everyone wears a seat belt. Children under 8 ride in a child seat (a seat belt is fine if they weigh at least 40 lb or are over 4&prime;9&Prime;). "
    "All the usual traffic laws apply.</p>"),
  ],
  sources=[
   ("Low-Speed Vehicles (LSV) and Personal Transportation Vehicles (PTV) &mdash; Glynn County", "https://www.glynncounty.org/government/departments/licensing-compliance/licenses-permits/low-speed-vehicles-lsv-personal-transportation-vehicles-ptv"),
   ("St. Simons Island roads by speed limit (June 2025) &mdash; Glynn County (PDF)", "https://content.glynncounty.org/sites/default/files/2025-06/SSI-Roads-MPH.pdf"),
   GA_HB877, GA_DPS,
  ],
  street_map=("the county&rsquo;s map of St. Simons roads by speed limit", "https://content.glynncounty.org/sites/default/files/2025-06/SSI-Roads-MPH.pdf"),
  map=dict(area="St. Simons Island", ok="Public streets posted 25 mph or less",
           bars=[dict(orient="h", pos=.42, name="Streets over 25 mph", cross=None),
                 dict(orient="v", pos=.70, name="Streets over 25 mph", cross=None)],
           cross_note=None,
           paths="Sidewalks, bike paths: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Glynn County&rsquo;s 25 mph line for carts yet, "
         "so a route can include a 30 or 35 mph street. Check the county&rsquo;s speed map before you ride.",
 ),
 dict(
  slug="tybee-island", name="Tybee Island", st="GA", state="Georgia", place="Tybee Island, Georgia",
  org="the City of Tybee Island", Org="The City of Tybee Island", publish=True,
  official=("the city&rsquo;s Motorized Cart Information page", "https://www.cityoftybee.org/464/Motorized-Cart-Information"),
  hub="Every city street except Highway 80, which carts cross at four places. Sticker; 16+ licensed.",
  answer="Tybee lets registered, inspected carts use every city street except Highway 80, which carts may only cross at four places. "
         "Drivers must be licensed and 16 or older.",
  faq=dict(
   license="<p>Yes. Carts are for licensed drivers.</p>",
   age="<p>Licensed drivers <strong>16 or older</strong>.</p>",
   permit="<p>Yes. Every cart is inspected each year and carries a T-number sticker on the bottom left of the windshield. The sticker is a one-time $15; "
          "renewals are free. Both are done at Parking Services, 1509 Strand Avenue (call ahead: officers are sometimes out). "
          "Tybee residents bring a vehicle registration showing Chatham County District 3.</p>"
          "<p>Insurance must meet the state minimum for cars ($25,000 per person, $50,000 per accident, $15,000 property). "
          "Homeowner&rsquo;s policies aren&rsquo;t accepted. Keep proof in the cart.</p>"
          "<p>Required equipment: headlights, tail lights, brake lights, turn signals, a top-mounted flashing amber light, a horn and seat belts. "
          "The cart can&rsquo;t be able to go faster than 20 mph.</p>",
   where="<p><strong>All city streets except Highway 80.</strong> Carts may cross Highway 80 only at:</p>"
         "<ul><li>Highway 80/Butler Avenue, at locations south of the Park of 7 Flags</li>"
         "<li>the traffic light at 14th Street</li>"
         "<li>the traffic light at Campbell Avenue</li>"
         "<li>the traffic light at Jones Avenue</li></ul>"
         "<p>No carts on sidewalks.</p>",
   lsv="<p>Tybee&rsquo;s cart rules are written for carts that can&rsquo;t go faster than 20 mph. Under Georgia law, a low-speed vehicle (LSV) is a separate class: "
       "a four-wheeled electric vehicle with a top speed over 20 mph and not over 25 mph. We didn&rsquo;t find LSV rules on the city&rsquo;s cart page, "
       "so ask the city before you drive an LSV here.</p>",
   hours="<p>We didn&rsquo;t find cart hours in the city&rsquo;s rules. Every cart must have headlights, tail lights, brake lights, turn signals "
         "and a top-mounted flashing amber light.</p>",
  ),
  extra=[
   ("Parking",
    "<p>Cart parking is paid like any other: meter, the ParkTYB app or a decal. Rental carts may already have a pass.</p>"),
   ("Fines",
    "<p>The city&rsquo;s flyer says violations can bring fines up to $1,000 or up to 12 months in jail.</p>"),
  ],
  sources=[
   ("Motorized Cart Information &mdash; City of Tybee Island", "https://www.cityoftybee.org/464/Motorized-Cart-Information"),
   ("Golf Cart Safety Rules &amp; Regulations flyer &mdash; City of Tybee Island (PDF)", "https://www.cityoftybee.org/DocumentCenter/View/3286"),
   GA_HB877, GA_DPS,
  ],
  street_map=None,
  map=dict(area="Tybee Island (city streets)", ok="All city streets",
           bars=[dict(orient="v", pos=.55, name="Highway 80", cross="dots", count=4)],
           cross_note="The four places carts may cross (listed above; positions not to scale)",
           paths="Sidewalks: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Tybee&rsquo;s Highway 80 rule yet, "
         "so if a route runs along Highway 80, don&rsquo;t take it in a cart.",
 ),
 dict(
  slug="gulf-breeze", name="Gulf Breeze", st="FL", state="Florida", place="Gulf Breeze, Florida",
  org="the City of Gulf Breeze", Org="The City of Gulf Breeze", publish=False,
  official=("the city&rsquo;s Golf Carts and The Loop page", "https://cityofgulfbreeze.us/golf-carts-and-the-loop/"),
  hub="Neighborhood roads posted under 25 mph and The Loop. City decal.",
  answer="Gulf Breeze lets registered golf carts use its quiet neighborhood roads and shared-use paths, including The Loop. "
         "Low-speed vehicles get the roads but not The Loop.",
  faq=dict(
   license="<p>The city&rsquo;s page says drivers 15 and up need at least a valid learner&rsquo;s permit.</p>",
   age="<p>The city&rsquo;s page says no one under 15 may drive a cart.</p>",
   permit="<p>Yes. Register the cart with the city (Community Services at City Hall) and put the decal on the windshield. An expired registration can get you a ticket.</p>",
   where="<p>Designated public roads and shared-use paths posted <strong>under 25 mph</strong>, which the city describes as essentially its residential neighborhoods, "
         "and <strong>The Loop</strong>, the city&rsquo;s shared-use path for golf carts and other recreational wheels.</p>"
         "<p>Not on the Bob Sikes Bridge or the Pensacola Bay Bridge. Carts can&rsquo;t cross Gulf Breeze Parkway (US 98) at this time. Never on sidewalks.</p>",
   lsv="<p>A cart modified to go faster than 20 mph becomes a low-speed vehicle: it needs a driver&rsquo;s license, a state tag and insurance, "
       "and it can no longer use the shared-use paths. LSVs can use roads posted 35 mph or less, but <strong>not The Loop</strong>.</p>",
   hours="<p>After sunset a cart needs headlights, brake lights, turn signals and a windshield. Without them, night driving isn&rsquo;t legal.</p>",
  ),
  extra=[],
  sources=[
   ("Golf Carts and The Loop &mdash; City of Gulf Breeze", "https://cityofgulfbreeze.us/golf-carts-and-the-loop/"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  map=dict(area="Gulf Breeze (city)", ok="Neighborhood roads posted under 25 mph, and The Loop",
           bars=[dict(orient="h", pos=.45, name="Gulf Breeze Pkwy (US 98)", cross="x", count=3)],
           cross_note=None, x_note="No crossing at this time (US 98)", paths="Sidewalks: no carts"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Gulf Breeze&rsquo;s under-25 rule yet, "
         "so a route can include a street that carts can&rsquo;t use here. Check the city&rsquo;s page and map before you ride.",
 ),
]
