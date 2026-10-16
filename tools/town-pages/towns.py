# Content for the "Golf carts in [town]" pages.
#
# The TOWNS list below is the original 2026-10-16 draft content, kept word for word (Ron 2026-10-17:
# he preferred the original drafts; restore their layout, wording and structure). The only additions
# live in EXTRAS at the bottom: publish flag, state, the official link for the short independence
# line, the town's own map (plain text link, no drawn maps), and the hub summary.
#
# Rules: every rule comes from a source listed on the same page (official city/county/state sites
# and PDFs only). No agent reads Municode or LexisNexis. No town logos or seals.
#

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

TOWNS = [
 dict(
  slug="st-pete-beach", name="St. Pete Beach", place="St. Pete Beach, Florida", jur="the City of St. Pete Beach",
  lede="St. Pete Beach lets golf carts use its quieter city streets: the ones posted 25 mph or less. "
       "Carts need a city registration and decal, and the driver needs a driver&rsquo;s license.",
  sections=[
   ("Where carts can go",
    "<p>City streets posted <strong>25 mph or less</strong>, inside the area shown on the city&rsquo;s map. "
    "Carts can&rsquo;t drive on or cross state or county roads unless the state or Pinellas County allows it at that spot. "
    "Gulf Boulevard is a state road.</p>"
    "<p>No carts on sidewalks, in parks, on beaches or on other city land.</p>"),
   ("Who can drive",
    "<p>Only people with a <strong>valid driver&rsquo;s license</strong>. That&rsquo;s stricter than Florida&rsquo;s general rule, "
    "which lets 18-year-olds drive a cart with just a photo ID.</p>"),
   ("Registration and equipment",
    "<p>Resident-owned carts are registered with the city every year ($10, paid at City Hall), and the decal goes on the back, "
    "driver&rsquo;s side. You&rsquo;ll need proof of a valid driver&rsquo;s license and a signed statement that the cart has liability insurance "
    "(a rider on a homeowner&rsquo;s policy or a separate policy). The cart can&rsquo;t be able to go faster than 20 mph.</p>"
    "<p>Daytime equipment: good brakes, reliable steering, safe tires, a horn, a rearview mirror, and red reflectors front and rear.</p>"),
   ("After dark",
    "<p>Sunrise to sunset only, unless the cart also has headlights, brake lights, turn signals and a windshield.</p>"),
   ("Low-speed vehicles", FL_LSV),
  ],
  sources=[
   ("Golf Carts &mdash; City of St. Pete Beach", "https://www.stpetebeach.org/498/Golf-Carts"),
   ("Ordinance 2013-17 (City Code ch. 82, art. VI) &mdash; City of St. Pete Beach (PDF)", "https://www.stpetebeach.org/DocumentCenter/View/1021/Golf-Cart-Ordinance-PDF"),
   ("Restricted roadways map &mdash; City of St. Pete Beach", "https://www.stpetebeach.org/ImageRepository/Document?documentID=884"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know St. Pete Beach&rsquo;s 25 mph line yet, "
         "so a route here can include a 30 or 35 mph street that carts can&rsquo;t use. Check the city&rsquo;s map before you ride.",
 ),
 dict(
  slug="dunedin", name="Dunedin", place="Dunedin, Florida", jur="the City of Dunedin",
  lede="Dunedin has a golf cart zone: designated city streets posted 30 mph or less. "
       "There&rsquo;s no city sticker or fee for carts that top out at 20 mph.",
  sections=[
   ("Where carts can go",
    "<p>Designated city streets in the cart zone, and only roads posted <strong>30 mph or less</strong>. The city&rsquo;s online map shows the zone.</p>"
    "<p>State and county roads can be crossed only at marked golf cart crossings.</p>"
    "<p>No carts on the Pinellas Trail, sidewalks, in parks or on other city property unless a spot is set aside for them. "
    "Highlander Park is one: carts stay on its shell path and park where the park&rsquo;s cart map shows.</p>"),
   ("Who can drive",
    "<p>Under 18: a learner&rsquo;s permit or a driver&rsquo;s license. 18 and over: a government-issued photo ID. (This is Florida&rsquo;s rule, which the city follows.)</p>"),
   ("Registration and equipment",
    "<p>No city registration, sticker or fee for carts that can&rsquo;t go faster than 20 mph. The Pinellas County Sheriff enforces the state&rsquo;s cart rules.</p>"
    "<p>Equipment: reliable steering, good brakes, safe tires, a rearview mirror, and red reflectors front and rear.</p>"),
   ("After dark",
    "<p>At night a cart also needs headlights, brake lights, turn signals and a windshield.</p>"),
   ("Parking",
    "<p>Use golf cart spaces where there are some. Otherwise two carts park side by side in one car space. During downtown events, carts park in vehicle spaces only.</p>"),
   ("Low-speed vehicles",
    "<p>A low-speed vehicle (LSV) needs a state license and registration, as the city&rsquo;s page notes. "
    "Under Florida law LSVs can use streets posted 35 mph or less.</p>"),
  ],
  sources=[
   ("Golf Carts &mdash; City of Dunedin", "https://www.dunedin.gov/Activities-and-Recreation/Getting-Around/Golf-Carts"),
   ("Golf cart zone map &mdash; City of Dunedin GIS", "https://gis.dunedingov.com/portal/apps/webappviewer/index.html?id=c3f6c0aacba64efb87f795bf3eb195ea"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Dunedin&rsquo;s cart zone or its 30 mph line yet, "
         "so a route can leave the zone or use a 35 mph street. Check the city&rsquo;s map before you ride.",
 ),
 dict(
  slug="mount-dora", name="Mount Dora", place="Mount Dora, Florida", jur="the City of Mount Dora",
  lede="In Mount Dora, a permitted golf cart can use every city street except a short list of busier roads, "
       "around the clock.",
  sections=[
   ("Where carts can go",
    "<p><strong>All city streets</strong>, except:</p>"
    "<ul><li>all county roads and state highways, and streets outside city limits</li>"
    "<li>US 441, SR 44, SR 46, CR 19A, Old Highway 441, Old Eustis Road, Eudora Road, Round Lake Road, Limit Avenue, Wolf Branch Road, Robie Avenue and Britt Road</li>"
    "<li>5th Avenue from Highland Avenue to Old Highway 441; Highland Avenue from 5th Avenue to the Orange County line; "
    "1st Avenue from US 441 to Highland Avenue; Donnelly Street from US 441 to Limit Avenue</li></ul>"
    "<p>Carts may cross county roads at intersections. They may <strong>not</strong> cross US 441. "
    "No bike paths or sidewalks. Private streets and gated communities set their own rules.</p>"),
   ("Who can drive",
    "<p>Drivers must be 18, unless they have a learner&rsquo;s permit or driver&rsquo;s license, and must carry a government-issued photo ID. "
    "Passengers ride seated, no more than the cart is built for.</p>"),
   ("Permit and equipment",
    "<p>A city golf cart permit is required: $25 to register, $10 a year to renew. Bring the application, the affidavit, proof of insurance "
    "and a copy of your license to the Police Department (or email them). The sticker goes on the lower driver&rsquo;s side bumper or fender. "
    "Country Club of Mount Dora and private or gated communities inside the city don&rsquo;t need it.</p>"
    "<p>Required equipment: windshield; driver&rsquo;s side mirror plus an inside or passenger-side mirror; headlights and tail lights; brakes and a parking brake; "
    "front and rear turn signals; steering; rear and side reflectors; a horn; and grab bars on rear-facing seats.</p>"),
   ("Hours",
    "<p>24 hours a day, except when the city closes a street for an event.</p>"),
   ("Low-speed vehicles",
    "<p>A cart modified to go faster than 20 mph counts as a low-speed vehicle. It must be titled, registered and insured with the state, "
    "and it can&rsquo;t use sidewalks or streets posted over 35 mph.</p>"),
  ],
  sources=[
   ("Golf Cart Registration &mdash; City of Mount Dora", "https://www.mountdora.gov/1457/Golf-Cart-Registration"),
   ("Golf Carts Street Usage list and map (May 17, 2023) &mdash; City of Mount Dora (PDF)", "https://www.mountdora.gov/DocumentCenter/View/16545"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Mount Dora&rsquo;s not-allowed list yet, "
         "so a route could use one of those roads. Check the list above before you ride.",
 ),
 dict(
  slug="miami-lakes", name="Miami Lakes", place="Miami Lakes, Florida", jur="the Town of Miami Lakes",
  lede="Miami Lakes opens all town streets to inspected, permitted golf carts, except NW 67th Avenue and NW 87th Avenue.",
  sections=[
   ("Where carts can go",
    "<p><strong>All town streets except NW 67th Avenue and NW 87th Avenue.</strong> On those two, carts may only cross, at marked intersections or traffic lights.</p>"
    "<p>No carts in parks, on bike paths, sidewalks or swales. The town permit doesn&rsquo;t cover private property: shopping-center parking lots, "
    "private roads and condo common areas are up to their owners.</p>"),
   ("Who can drive",
    "<p>Only people with a <strong>current, valid driver&rsquo;s license</strong>. No more passengers than the cart is built for, "
    "and state seat belt and child-seat rules apply.</p>"),
   ("Permit and inspection",
    "<p>Each cart is inspected by the town every year. Apply to the Town Police Department with proof of insurance and a $50 application fee; "
    "a cart that passes gets a permit with a registration number, shown where it&rsquo;s easy to see.</p>"
    "<p>Required equipment: good brakes, reliable steering, safe tires, rearview mirrors, red reflectors front and rear, brake lights, turn signals and seat belts. "
    "Carts built for speeds under 25 mph also need the orange slow-moving-vehicle triangle.</p>"),
   ("After dark",
    "<p>Between sunset and sunrise, only with headlights and a windshield.</p>"),
   ("Low-speed vehicles", FL_LSV),
  ],
  sources=[
   ("Ordinance 22-293, adopted April 12, 2022 (Town Code ch. 39, art. III) &mdash; Town of Miami Lakes (PDF)", "https://www.miamilakes-fl.gov/wp-content/uploads/2023/10/Ordinance-ORD-22293.pdf"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know that NW 67th and NW 87th Avenues are closed to carts here, "
         "so if a route runs along either one, don&rsquo;t take it in a cart.",
 ),
 dict(
  slug="pine-island", name="Pine Island", place="Pine Island, Florida (Lee County)", jur="Lee County",
  lede="Lee County lets golf carts use its roads on Pine Island in daylight, with a few busy stretches left out. "
       "Drivers need a driver&rsquo;s license.",
  sections=[
   ("Where carts can go",
    "<p>County-maintained streets on Pine Island (west of the St. James Creek Bridge), <strong>except</strong>:</p>"
    "<ul><li>Stringfellow Road from the Jug Creek Bridge in Bokeelia to St. Jude Boulevard in St. James City</li>"
    "<li>Pine Island Road east of Stringfellow Road</li></ul>"
    "<p>Lee County DOT signs the designated roads and posts golf cart crossings across Stringfellow and Pine Island Roads where it has approved them.</p>"
    "<p>No carts on bike paths, shared-use paths or sidewalks, or in the drainage and landscaped areas beside the road.</p>"),
   ("Who can drive",
    "<p>Only people with a <strong>valid driver&rsquo;s license</strong> from their home state or country. "
    "Everyone rides seated, no more than the cart has seats, and nobody stands while it moves.</p>"),
   ("Equipment",
    "<p>Good brakes, reliable steering, safe tires, a rearview mirror, and red reflectors front and rear. "
    "The county ordinance has no registration or sticker.</p>"),
   ("Hours",
    "<p><strong>Daylight only.</strong> The ordinance doesn&rsquo;t allow golf carts on public roads between sunset and sunrise.</p>"),
   ("Low-speed vehicles", FL_LSV),
  ],
  sources=[
   ("Lee County Ordinance 13-08, adopted April 23, 2013, with its Attachment A street list &mdash; Lee County (PDF)", "https://www.leegov.com/bocc/Ordinances/13-08.pdf"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Pine Island&rsquo;s left-out stretches or the daylight rule yet, "
         "so check a route against the list above, and ride before sunset.",
 ),
 dict(
  slug="captiva", name="Captiva Island", place="Captiva Island, Florida (Lee County)", jur="Lee County",
  lede="On Captiva, golf carts can use the county roads that Lee County DOT has designated and signed for them, in daylight, "
       "with a licensed driver.",
  sections=[
   ("Where carts can go",
    "<p>County roads on Captiva that the <strong>Lee County Department of Transportation has designated</strong> for golf carts. "
    "The ordinance doesn&rsquo;t list the roads; the county signs the ones that are open to carts. If you don&rsquo;t see a sign, ask Lee County DOT.</p>"),
   ("Who can drive",
    "<p>Only people with a <strong>valid driver&rsquo;s license</strong> from their home state or country. "
    "Florida&rsquo;s late-night limits for young licensed drivers also apply to carts.</p>"),
   ("Cart and equipment",
    "<p>The cart can&rsquo;t be able to go faster than 20 mph. It needs good brakes, reliable steering, safe tires, a rearview mirror, "
    "and red reflectors front and rear. The county ordinance has no registration or sticker.</p>"),
   ("After dark",
    "<p>Sunrise to sunset, unless Lee County DOT has designated a road for night use. Then the cart also needs headlights, brake lights, turn signals and a windshield.</p>"),
   ("Low-speed vehicles", FL_LSV),
  ],
  sources=[
   ("Lee County Ordinance 09-22 (2009), golf carts on designated county roads on Captiva Island &mdash; Lee County (PDF)", "https://www.leegov.com/bocc/Ordinances/09-22.pdf"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know which Captiva roads Lee County has signed for carts, "
         "so follow the signs over the route.",
 ),
 dict(
  slug="jekyll-island", name="Jekyll Island", place="Jekyll Island, Georgia", jur="the Jekyll Island Authority",
  lede="Jekyll Island is a little different. The street-legal carts most people drive count as personal transportation vehicles (PTVs) "
       "under Georgia law, and those are welcome on the island&rsquo;s streets. True golf carts, the kind built only for the golf course, are not.",
  sections=[
   ("PTV or golf cart?",
    "<p>Georgia law draws the line by speed. A <strong>PTV</strong> has at least four wheels, a top speed under 20 mph, weighs no more than 1,375 lb empty and carries up to eight people. "
    "A <strong>golf cart</strong> is built only for golf and averages under 15 mph.</p>"
    "<p>On Jekyll, golf carts are not allowed on public streets or Authority property, except to cross a street while playing golf, "
    "or at a parade, festival or other event with the sponsor&rsquo;s OK. Privately owned carts aren&rsquo;t allowed on the Authority&rsquo;s golf courses.</p>"),
   ("Where PTVs can go",
    "<p>The island&rsquo;s public streets, but <strong>not</strong> roads that are part of the state highway system. "
    "No PTVs on sidewalks, bike paths, the pedestrian-only paths in the Historic District, unimproved trails, service roads or golf-cart paths.</p>"
    "<p>Park in regular vehicle spaces.</p>"),
   ("Who can drive",
    "<p>A valid driver&rsquo;s license, and at least <strong>16</strong>.</p>"),
   ("Insurance and equipment",
    "<p>The owner needs liability insurance at Georgia&rsquo;s minimum limits, with proof kept in the PTV. "
    "No Glynn County registration is needed on Jekyll.</p>"
    "<p>Required: brakes and a parking brake, a reverse warning, a main power switch, headlights and taillights, front and rear turn signals, brake lights, "
    "reflectors, a rearview mirror, a horn, hip restraints, hand holds, a seat belt for every seat, and the orange slow-moving-vehicle triangle on the back.</p>"),
   ("On the road",
    "<p>Everyone wears a seat belt, one person per belt. Children under 8 ride in a child seat (a seat belt is fine if they weigh at least 40 lb or are over 4&prime;9&Prime;). "
    "Lights on at night, in rain, or when you can&rsquo;t see 500 feet ahead. "
    "If two or more vehicles are behind you, pull over at the first safe spot. No passing in the same lane, and no riding two abreast.</p>"),
   ("Low-speed vehicles",
    "<p>LSVs are registered and insured with the state, can use streets posted 35 mph or less, and are kept off the same paths as PTVs.</p>"),
  ],
  sources=[
   ("Jekyll Island Authority Rules, Chapter F: Streets and Rights-of-Way (April 2022) &mdash; Jekyll Island Authority (PDF)", "https://www.jekyllisland.com/wp-content/uploads/2022/04/Chapter-F-Streets-and-Rights-of-Way-042222.pdf"),
   GA_HB877, GA_DPS,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Jekyll&rsquo;s rules yet: if a route uses a path here, "
         "don&rsquo;t take it in a cart or LSV.",
 ),
 dict(
  slug="st-simons-island", name="St. Simons Island", place="St. Simons Island, Georgia (Glynn County)", jur="Glynn County",
  lede="On St. Simons, and everywhere else in unincorporated Glynn County, a registered cart (a PTV under Georgia law) "
       "can use public streets posted 25 mph or less.",
  sections=[
   ("Where carts can go",
    "<p>Public streets posted <strong>25 mph or less</strong>. The county publishes a map of St. Simons roads by speed limit. "
    "No carts on sidewalks or bike paths, at any time.</p>"),
   ("Who can drive",
    "<p>At least <strong>16</strong>, with a valid driver&rsquo;s license.</p>"),
   ("Registration",
    "<p>Register the cart with Glynn County before driving it on public streets: $15, good for five years or until the cart changes hands. "
    "The county decal goes on the driver&rsquo;s side, where it can always be seen.</p>"),
   ("On the road",
    "<p>One person per seat, and everyone wears a seat belt. Children under 8 ride in a child seat (a seat belt is fine if they weigh at least 40 lb or are over 4&prime;9&Prime;). "
    "Headlights and taillights on when it isn&rsquo;t daylight. All the usual traffic laws apply.</p>"),
   ("Low-speed vehicles",
    "<p>A low-speed vehicle (top speed over 20, up to 25 mph) is registered with the Glynn County Tax Commissioner like any other vehicle, "
    "can use streets posted 35 mph or less, and isn&rsquo;t allowed on sidewalks or bike paths.</p>"),
  ],
  sources=[
   ("Low-Speed Vehicles (LSV) and Personal Transportation Vehicles (PTV) &mdash; Glynn County", "https://www.glynncounty.org/government/departments/licensing-compliance/licenses-permits/low-speed-vehicles-lsv-personal-transportation-vehicles-ptv"),
   ("St. Simons Island roads by speed limit (June 2025) &mdash; Glynn County (PDF)", "https://content.glynncounty.org/sites/default/files/2025-06/SSI-Roads-MPH.pdf"),
   GA_HB877, GA_DPS,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Glynn County&rsquo;s 25 mph line for carts yet, "
         "so a route can include a 30 or 35 mph street. Check the county&rsquo;s speed map before you ride.",
 ),
 dict(
  slug="tybee-island", name="Tybee Island", place="Tybee Island, Georgia", jur="the City of Tybee Island",
  lede="Tybee lets registered, inspected carts use every city street except Highway 80, which carts may only cross at four places.",
  sections=[
   ("Where carts can go",
    "<p><strong>All city streets except Highway 80.</strong> Carts may cross Highway 80 only at:</p>"
    "<ul><li>Highway 80/Butler Avenue, at locations south of the Park of 7 Flags</li>"
    "<li>the traffic light at 14th Street</li>"
    "<li>the traffic light at Campbell Avenue</li>"
    "<li>the traffic light at Jones Avenue</li></ul>"
    "<p>No carts on sidewalks.</p>"),
   ("Who can drive",
    "<p>Licensed drivers <strong>16 or older</strong>.</p>"),
   ("Registration, inspection and insurance",
    "<p>Every cart is inspected each year and carries a T-number sticker on the bottom left of the windshield. The sticker is a one-time $15; "
    "renewals are free. Both are done at Parking Services, 1509 Strand Avenue (call ahead: officers are sometimes out). "
    "Tybee residents bring a vehicle registration showing Chatham County District 3.</p>"
    "<p>Insurance must meet the state minimum for cars ($25,000 per person, $50,000 per accident, $15,000 property). "
    "Homeowner&rsquo;s policies aren&rsquo;t accepted. Keep proof in the cart.</p>"
    "<p>Required equipment: headlights, tail lights, brake lights, turn signals, a top-mounted flashing amber light, a horn and seat belts. "
    "The cart can&rsquo;t be able to go faster than 20 mph.</p>"),
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
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Tybee&rsquo;s Highway 80 rule yet, "
         "so if a route runs along Highway 80, don&rsquo;t take it in a cart.",
 ),
 dict(
  slug="gulf-breeze", name="Gulf Breeze", place="Gulf Breeze, Florida", jur="the City of Gulf Breeze",
  lede="Gulf Breeze lets registered golf carts use its quiet neighborhood roads and shared-use paths, including The Loop. "
       "Low-speed vehicles get the roads but not The Loop.",
  sections=[
   ("Where carts can go",
    "<p>Designated public roads and shared-use paths posted <strong>under 25 mph</strong>, which the city describes as essentially its residential neighborhoods, "
    "and <strong>The Loop</strong>, the city&rsquo;s shared-use path for golf carts and other recreational wheels.</p>"
    "<p>Not on the Bob Sikes Bridge or the Pensacola Bay Bridge. Carts can&rsquo;t cross Gulf Breeze Parkway (US 98) at this time. Never on sidewalks.</p>"),
   ("Who can drive",
    "<p>The city&rsquo;s page says no one under 15 may drive a cart, and drivers 15 and up need at least a valid learner&rsquo;s permit.</p>"),
   ("Registration",
    "<p>Register the cart with the city (Community Services at City Hall) and put the decal on the windshield. An expired registration can get you a ticket.</p>"),
   ("After dark",
    "<p>After sunset a cart needs headlights, brake lights, turn signals and a windshield. Without them, night driving isn&rsquo;t legal.</p>"),
   ("Low-speed vehicles",
    "<p>A cart modified to go faster than 20 mph becomes a low-speed vehicle: it needs a driver&rsquo;s license, a state tag and insurance, "
    "and it can no longer use the shared-use paths. LSVs can use roads posted 35 mph or less, but <strong>not The Loop</strong>.</p>"),
  ],
  sources=[
   ("Golf Carts and The Loop &mdash; City of Gulf Breeze", "https://cityofgulfbreeze.us/golf-carts-and-the-loop/"),
   FL_316212, FL_3162122,
  ],
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Gulf Breeze&rsquo;s under-25 rule yet, "
         "so a route can include a street that carts can&rsquo;t use here. Check the city&rsquo;s page and map before you ride.",
 ),
]

# ---------- Additions (Ron 2026-10-17). Nothing above this line changes the original wording. ----------
# publish:    True = indexable, in the hub and the sitemap. False = HELD: noindex, unlinked, not in sitemap.
# official:   (label, url) for "For official rules, see <label>." in the short independence line.
# map_line:   (text before the link, link text, url) for the plain map line, or None (no town map).
# hub:        one-line summary on /cart-rules.
EXTRAS = {
 "st-pete-beach": dict(st="FL", publish=True,
   official=("the city&rsquo;s Golf Carts page", "https://www.stpetebeach.org/498/Golf-Carts"),
   map_line=("See ", "St. Pete Beach&rsquo;s official golf cart map", "https://www.stpetebeach.org/ImageRepository/Document?documentID=884"),
   hub="City streets posted 25 mph or less. City decal; driver&rsquo;s license required."),
 "dunedin": dict(st="FL", publish=True,
   official=("the city&rsquo;s Golf Carts page", "https://www.dunedin.gov/Activities-and-Recreation/Getting-Around/Golf-Carts"),
   map_line=("See ", "Dunedin&rsquo;s official golf cart map", "https://gis.dunedingov.com/portal/apps/webappviewer/index.html?id=c3f6c0aacba64efb87f795bf3eb195ea"),
   hub="A cart zone of city streets posted 30 mph or less. No city sticker for 20 mph carts."),
 "mount-dora": dict(st="FL", publish=True,
   official=("the city&rsquo;s Golf Cart Registration page", "https://www.mountdora.gov/1457/Golf-Cart-Registration"),
   map_line=("See ", "Mount Dora&rsquo;s official golf cart map", "https://www.mountdora.gov/DocumentCenter/View/16545"),
   hub="Every city street except a short list of busier roads, around the clock. City permit."),
 "miami-lakes": dict(st="FL", publish=True,
   official=("the town&rsquo;s golf cart ordinance (PDF)", "https://www.miamilakes-fl.gov/wp-content/uploads/2023/10/Ordinance-ORD-22293.pdf"),
   map_line=None,
   hub="All town streets except NW 67th and NW 87th Avenues. Yearly inspection; driver&rsquo;s license."),
 "pine-island": dict(st="FL", publish=True,
   official=("Lee County Ordinance 13-08 (PDF)", "https://www.leegov.com/bocc/Ordinances/13-08.pdf"),
   map_line=None,
   hub="Lee County roads on the island, minus a few busy stretches. Daylight only; driver&rsquo;s license."),
 "captiva": dict(st="FL", publish=False,
   official=("Lee County Ordinance 09-22 (PDF)", "https://www.leegov.com/bocc/Ordinances/09-22.pdf"),
   map_line=None,
   hub="County roads Lee County DOT has signed for carts. Daylight; driver&rsquo;s license."),
 "jekyll-island": dict(st="GA", publish=True,
   official=("the Authority&rsquo;s Chapter F rules (PDF)", "https://www.jekyllisland.com/wp-content/uploads/2022/04/Chapter-F-Streets-and-Rights-of-Way-042222.pdf"),
   map_line=None,
   hub="Street-legal PTVs on island streets (not state highways or paths). 16+ with a license."),
 "st-simons-island": dict(st="GA", publish=True,
   official=("the county&rsquo;s LSV and PTV page", "https://www.glynncounty.org/government/departments/licensing-compliance/licenses-permits/low-speed-vehicles-lsv-personal-transportation-vehicles-ptv"),
   # The county's roads-by-speed-limit map, not a map titled for carts (coordinator 2026-10-17; flag to Ron).
   map_line=("See ", "Glynn County&rsquo;s speed limit map for St. Simons", "https://content.glynncounty.org/sites/default/files/2025-06/SSI-Roads-MPH.pdf"),
   hub="Public streets posted 25 mph or less. County decal; 16+ with a license."),
 "tybee-island": dict(st="GA", publish=True,
   official=("the city&rsquo;s Motorized Cart Information page", "https://www.cityoftybee.org/464/Motorized-Cart-Information"),
   map_line=None,
   hub="Every city street except Highway 80, which carts cross at four places. Sticker; 16+ licensed."),
 "gulf-breeze": dict(st="FL", publish=False,
   official=("the city&rsquo;s Golf Carts and The Loop page", "https://cityofgulfbreeze.us/golf-carts-and-the-loop/"),
   map_line=None,
   hub="Neighborhood roads posted under 25 mph and The Loop. City decal."),
}
STATES = {"FL": "Florida", "GA": "Georgia"}
for _t in TOWNS:
    _t.update(EXTRAS[_t["slug"]])
    _t["state"] = STATES[_t["st"]]
