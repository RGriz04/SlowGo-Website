# Florida coast town pages (scale-up 2026-10-17), in the towns.py schema.
# Source: the cart-towns database, docs/research/cart-towns/cart-towns-2026-10-16.csv on SlowGo-f20-towns
# (rows given in db_row). Only city/county/state sources; no Municode. Review fields (prio, quality,
# source_type, checked, gap, db_row) feed the review sheet and are not shown on the pages.

from towns import FL_LSV, FL_316212, FL_3162122

FL_AGE = ("<p>We didn&rsquo;t find a local age rule, so Florida&rsquo;s applies: drivers under 18 need a learner&rsquo;s permit "
          "or a driver&rsquo;s license, and drivers 18 and over need a government-issued photo ID.</p>")
FL_HOURS = ("<p>We didn&rsquo;t find local hours. Under Florida law, golf carts run from sunrise to sunset, unless the local "
            "government allows night use and the cart has headlights, brake lights, turn signals and a windshield.</p>")
FL_DAY_EQUIP = "efficient brakes, reliable steering, safe tires, a rearview mirror, and red reflectors front and rear"

PIN = "https://pinellas.gov/"
PINELLAS_ZONES = [
    ("Bardmoor North", "bardmoor-north"),
    ("Baywood Village", "baywood-village"),
    ("Crystal Beach", "crystal-beach"),
    ("Freshwater Estates&ndash;Lake Shore Estates North", "freshwater-estates-lake-shore-estates-north"),
    ("Highland Lakes", "highland-lakes"),
    ("Lake Shore Estates", "lake-shore-estates"),
    ("Ozona", "ozona"),
    ("Palm Harbor", "palm-harbor"),
    ("West Lake Village", "west-lake-village"),
]
_zone_lis = "".join(f'<li><a href="{PIN}{s}-golf-cart-zone-map/" rel="noopener">{n}</a></li>' for n, s in PINELLAS_ZONES)

TOWNS = [
 dict(
  slug="pinellas-county", name="Pinellas County", st="FL", state="Florida", place="unincorporated Pinellas County, Florida",
  h1="Golf cart zones in Pinellas County, Florida", hub_name="Pinellas County golf cart zones",
  org="Pinellas County", Org="Pinellas County", publish=True,
  official=("the county&rsquo;s Golf Cart Communities page", "https://pinellas.gov/golf-cart-communities/"),
  publishes="Pinellas County publishes the golf cart rules for its unincorporated areas.",
  hub="Nine signed golf cart zones in unincorporated areas, including Crystal Beach, Ozona and Palm Harbor. Driver&rsquo;s license.",
  answer="In unincorporated Pinellas County, golf carts are street legal only inside the county&rsquo;s nine designated golf cart zones, "
         "on roads where signs are posted. Drivers need a valid driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. The county&rsquo;s page says golf cart drivers need a <strong>valid driver&rsquo;s license</strong>. "
           "That&rsquo;s stricter than Florida&rsquo;s general rule, which lets 18-year-olds drive a cart with just a photo ID.</p>",
   age="<p>The county ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>The county&rsquo;s page doesn&rsquo;t mention a county registration or sticker. The cart can&rsquo;t be able to go faster than 20 mph.</p>"
          f"<p>Equipment: {FL_DAY_EQUIP}.</p>",
   where="<p>Only inside a <strong>designated, signed golf cart zone</strong>. The county creates zones at the request of a homeowners&rsquo; "
         "association or property owners. Inside a zone, use the roads where golf cart signs are posted, obey traffic laws and yield. The zones, with the county&rsquo;s zone maps:</p>"
         f"<ul>{_zone_lis}</ul>"
         "<p>In Palm Harbor, a county search result names Palm Harbor Boulevard (Alt US 19), Omaha Street (CR 1) and Nebraska Avenue as closed to carts; check the zone map.</p>"
         "<p>Cities in the county set their own cart rules: see <a href=\"/golf-carts/dunedin\">Dunedin</a> and <a href=\"/golf-carts/st-pete-beach\">St. Pete Beach</a>.</p>",
   lsv="<p>Low-speed vehicles (LSVs, also called neighborhood electric vehicles) are street legal on Pinellas County roads posted <strong>35 mph or less</strong>. "
       "They must be registered and insured, with a VIN, federal safety equipment and a licensed driver. An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   hours="<p>From sunset to sunrise, a cart also needs headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Seat belts", "<p>Seat belts and child restraints aren&rsquo;t required in golf carts, but the county advises them. DUI laws apply.</p>"),
  ],
  sources=[
   ("Golf Cart Communities &mdash; Pinellas County", "https://pinellas.gov/golf-cart-communities/"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know where Pinellas County&rsquo;s golf cart zones begin and end yet, "
         "so a route can leave a zone. Check the zone map before you ride.",
  prio="beach", prio_note="Gulf coast communities north of Clearwater (Crystal Beach, Ozona, Palm Harbor); one page for nine zones",
  quality="medium", source_type="county web page + county zone maps", checked="2026-10-16",
  gap="County page cites no ordinance or zone resolution; the nine zone map pages were not opened; Palm Harbor closed streets come from a county search result.",
  db_row=[108, 44, 45, 55, 66, 71, 83, 102, 103, 131],
 ),
 dict(
  slug="clearwater", name="Clearwater", st="FL", state="Florida", place="Clearwater, Florida",
  org="the City of Clearwater", Org="The City of Clearwater", no_carts=True, publish=False,   # HELD (Ron 2026-10-17 afternoon, D19): "no carts" page without an affirmative official prohibition for these roads
  publishes="The City of Clearwater publishes its Clearwater Beach transportation rules, including golf carts and LSVs.",
  official=("the city&rsquo;s Alternative Transportation page for Clearwater Beach", "https://www.myclearwater.com/Visit-the-Beach/Beach-Parking/Alternative-Transportation-Clearwater-Beach"),
  hub="We haven&rsquo;t verified public-road authorization for golf carts. LSVs on streets posted 35 mph or less.",
  answer="We haven&rsquo;t verified public-road authorization for golf carts in Clearwater. Under Florida law a golf cart may use a public road only where "
         "the city or county has designated it, and the city says Clearwater Beach has no golf cart lanes. Street-legal low-speed vehicles (LSVs) can use streets posted 35 mph or less.",
  faq=dict(
   license="<p>Golf carts can&rsquo;t use Clearwater&rsquo;s public streets, so this comes down to LSVs: an LSV driver needs a valid driver&rsquo;s license.</p>",
   age="<p>There&rsquo;s no city age rule for golf carts, because they can&rsquo;t use public streets here. An LSV driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>There&rsquo;s no city golf cart registration, since the city hasn&rsquo;t designated streets for carts. LSVs are titled, registered and insured with the state.</p>",
   where="<p><strong>We haven&rsquo;t verified public-road authorization.</strong> Under Florida law, a golf cart can use a public road only where the county or city has designated it and posted signs, "
         "and we haven&rsquo;t found a Clearwater designation.</p>"
         "<p>The city&rsquo;s page says Clearwater Beach has no golf cart lanes and no dedicated public golf cart parking. "
         "Motorized vehicles aren&rsquo;t allowed on Beach Walk, except medical devices.</p>",
   lsv=FL_LSV + "<p>The city says a state-registered LSV may use any city-owned parking space, at the standard fee.</p>",
   hours="<p>Golf carts can&rsquo;t use public streets here at any hour. LSVs come with headlights and the other equipment federal safety rules require.</p>",
  ),
  extra=[],
  sources=[
   ("Alternative Transportation, Clearwater Beach &mdash; City of Clearwater", "https://www.myclearwater.com/Visit-the-Beach/Beach-Parking/Alternative-Transportation-Clearwater-Beach"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know that golf carts can&rsquo;t use Clearwater&rsquo;s streets, "
         "so it will still plan a route for one. Don&rsquo;t take that route in a golf cart. A street-legal LSV can use streets posted 35 mph or less.",
  prio="beach", prio_note="Clearwater Beach, a top Gulf beach destination (no-designation page)",
  quality="medium", source_type="city web page", checked="2026-10-16",
  gap="Absence-based: the city page (read in full) cites no ordinance and says the beach has no cart lanes; no designation found anywhere.",
  db_row=52,
 ),
 dict(
  slug="st-augustine-beach", name="St. Augustine Beach", st="FL", state="Florida", place="St. Augustine Beach, Florida",
  org="the City of St. Augustine Beach", Org="The City of St. Augustine Beach", no_carts=True, publish=False,   # HELD (Ron 2026-10-17 afternoon, D19): "no carts" page without an affirmative official prohibition for these roads
  official=("the city&rsquo;s Golf Carts/Low Speed Vehicles page", "https://www.staugbch.com/413/Golf-CartsLow-Speed-Vehicles"),
  hub="Traditional golf carts aren&rsquo;t allowed on public streets. LSVs on streets posted 35 mph or less.",
  answer="Golf carts aren&rsquo;t allowed on public streets in St. Augustine Beach: the city says traditional golf carts may not be driven on them. "
         "Street-legal low-speed vehicles (LSVs) can use streets posted 35 mph or less.",
  faq=dict(
   license="<p>Golf carts can&rsquo;t use the city&rsquo;s public streets. An LSV driver needs a valid driver&rsquo;s license.</p>",
   age="<p>There&rsquo;s no city age rule for golf carts, because they can&rsquo;t use public streets here. An LSV driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>There&rsquo;s no city golf cart permit. LSVs are registered and insured with the state.</p>",
   where="<p><strong>Not on public streets.</strong> The city&rsquo;s page says traditional golf carts may not be operated on public streets. "
         "LSVs can use streets posted 35 mph or less.</p>",
   lsv=FL_LSV,
   hours="<p>Golf carts can&rsquo;t use public streets here at any hour. LSVs come with headlights and the other equipment federal safety rules require.</p>",
  ),
  extra=[],
  sources=[
   ("Golf Carts/Low Speed Vehicles &mdash; City of St. Augustine Beach", "https://www.staugbch.com/413/Golf-CartsLow-Speed-Vehicles"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know that golf carts can&rsquo;t use St. Augustine Beach&rsquo;s streets, "
         "so it will still plan a route for one. Don&rsquo;t take that route in a golf cart. A street-legal LSV can use streets posted 35 mph or less.",
  prio="beach", prio_note="Atlantic beach town (ban page)",
  quality="medium", source_type="city page", checked="2026-10-15",
  gap="City code not read (it is on Municode); the Sheriff's golf cart flyer was not opened.",
  db_row=118,
 ),
 dict(
  slug="flagler-beach", name="Flagler Beach", st="FL", state="Florida", place="Flagler Beach, Florida",
  org="the City of Flagler Beach", Org="The City of Flagler Beach", publish=True,
  official=("the city&rsquo;s 2026 golf cart information packet (PDF)", "https://www.cityofflaglerbeach.com/DocumentCenter/View/6685/Golf-Cart-Info-Packet-2026"),
  hub="City streets, but not A1A or SR 100. Yearly registration and inspection; driver&rsquo;s license.",
  answer="Flagler Beach lets registered, inspected golf carts use city streets, but not State Road A1A or State Road 100. "
         "Drivers need a valid driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. The city&rsquo;s inspection checklist asks for a <strong>valid driver&rsquo;s license</strong>.</p>",
   age="<p>The city ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. Carts are registered every year (January 1 to December 31), with a police inspection the first time. "
          "It costs $40 to start and $30 to renew before January 31 ($40 after). Bring proof of insurance.</p>"
          "<p>Required equipment: seat belts for everyone, a full windshield, two headlights, turn signals, two brake lights, a horn, good tires, a mirror, "
          "steering, rear reflectors, and side reflectors for night.</p>",
   where="<p><strong>City streets</strong>, but not State Road A1A or State Road 100.</p>",
   lsv=FL_LSV,
   hours="<p>At night, or in fog, smoke or rain, only with headlights on.</p>",
  ),
  extra=[],
  sources=[
   ("Golf Cart Info Packet 2026 &mdash; City of Flagler Beach (PDF)", "https://www.cityofflaglerbeach.com/DocumentCenter/View/6685/Golf-Cart-Info-Packet-2026"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know that A1A and State Road 100 are closed to carts here, "
         "so if a route runs along either one, don&rsquo;t take it in a cart.",
  prio="beach", prio_note="Atlantic beach town",
  quality="medium", source_type="city registration packet", checked="2026-10-15",
  gap="Ordinance number not on the packet and the ordinance text was not read; whether carts may cross A1A or SR 100 isn't stated.",
  db_row=63,
 ),
 dict(
  slug="fort-walton-beach", name="Fort Walton Beach", st="FL", state="Florida", place="Fort Walton Beach, Florida",
  org="the City of Fort Walton Beach", Org="The City of Fort Walton Beach", publish=True,
  official=("the city&rsquo;s Alternative Transportation page", "https://www.fwb.org/556/Alternative-Transportation"),
  hub="Two golf cart zones, streets posted 30 mph or less. $25 city decal; driver&rsquo;s license.",
  answer="Fort Walton Beach has two golf cart zones: carts may drive only on city streets inside them, and only on streets posted 30 mph or less. "
         "Carts need a $25 yearly city decal, and drivers need a driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Drivers need a <strong>valid driver&rsquo;s license</strong>, in their possession.</p>",
   age="<p>The city ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. A city permit decal costs $25 a year, either for daytime only or for day and night. Carts need PIP and property damage liability insurance.</p>",
   where="<p>Only on city streets inside one of the city&rsquo;s <strong>two golf cart zones</strong>, and only on streets posted <strong>30 mph or less</strong>:</p>"
         "<ul><li>the north zone (Kenwood)</li><li>the south zone (Elliott Point, Ferry Park and the Downtown Entertainment District)</li></ul>"
         "<p>Golf carts can&rsquo;t drive on or cross state roads: US 98, Eglin Parkway, Beal Parkway, Florida Place SE and Perry Avenue SE.</p>",
   lsv="<p>Low-speed vehicles can use city streets posted 35 mph or less, but not state roads except to cross at traffic signals. They need the same $25 city decal. An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   hours="<p>The decal is either daytime only or day and night. Florida law requires headlights, brake lights, turn signals and a windshield for night driving.</p>",
  ),
  extra=[],
  sources=[
   ("Alternative Transportation &mdash; City of Fort Walton Beach", "https://www.fwb.org/556/Alternative-Transportation"),
   ("Golf cart zone map &mdash; City of Fort Walton Beach", "https://www.fwb.org/ImageRepository/Document?documentId=2924"),
   FL_316212, FL_3162122,
  ],
  street_map=("the City of Fort Walton Beach&rsquo;s golf cart zone map", "https://www.fwb.org/ImageRepository/Document?documentId=2924"),
  slowgo="It doesn&rsquo;t know Fort Walton Beach&rsquo;s two zones or its 30 mph line yet, "
         "so a route can leave a zone or use a 35 mph street. Check the zone map before you ride.",
  prio="beach", prio_note="Emerald Coast beach city",
  quality="medium", source_type="city page", checked="2026-10-16",
  gap="City code sec. 11.13.07 not read (Municode). A later ordinance (2166) reportedly adds a cart crossing of Perry Ave SE at First St SE and LSV access on part of Eglin Pkwy: seen only in news, left out.",
  db_row=65,
 ),
 dict(
  slug="mexico-beach", name="Mexico Beach", st="FL", state="Florida", place="Mexico Beach, Florida",
  org="the City of Mexico Beach", Org="The City of Mexico Beach", publish=True,
  official=("the city&rsquo;s golf cart permits page", "https://mexicobeachfl.gov/residents/golf-cart-permits/"),
  hub="City streets, sunrise to sunset. $15 yearly sticker; driver&rsquo;s license.",
  answer="Mexico Beach lets registered golf carts use city streets from sunrise to sunset. "
         "Drivers need a valid driver&rsquo;s license, and carts need a $15 yearly city sticker.",
  faq=dict(
   license="<p>Yes. Drivers need a <strong>valid driver&rsquo;s license</strong>.</p>",
   age="<p>The city ties driving to the license rather than to an age. The owner who registers the cart must be 18 or older.</p>",
   permit="<p>Yes. Carts are registered with the city every year for $15. The sticker goes on the driver&rsquo;s side rear fender. "
          "Renew in January: registrations expire January 31.</p>"
          "<p>Fines are $50, $75 and $150, and $250 for driving while a registration is revoked.</p>",
   where="<p>City streets designated under the city&rsquo;s base golf cart ordinance (Ordinance 689). We haven&rsquo;t read that ordinance, so we can&rsquo;t list the streets. "
         "US 98 is a state highway: under Florida law, carts may only cross it where crossing is allowed.</p>"
         "<p>Passengers are limited to the number of seats.</p>",
   lsv=FL_LSV,
   hours="<p><strong>Sunrise to sunset.</strong> In fog, smoke, rain or low light, carts must have headlights, brake lights, turn signals and a windshield. "
         "The city recommends reflectors or reflective tape.</p>",
  ),
  extra=[],
  sources=[
   ("Ordinance 820, golf cart hours, passengers and registration &mdash; City of Mexico Beach (PDF)", "https://mexicobeachfl.gov/uploads/2024/01/Ordinance-820-Golf-Cart-Registration_tagged.pdf"),
   ("Golf Cart Permits &mdash; City of Mexico Beach", "https://mexicobeachfl.gov/residents/golf-cart-permits/"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know Mexico Beach&rsquo;s street list or its sunrise-to-sunset rule yet, "
         "so ride in daylight and cross US 98 only where crossing is allowed.",
  prio="beach", prio_note="Gulf beach town (Forgotten Coast)",
  quality="high", source_type="ordinance PDF + city permit page", checked="2026-10-16",
  gap="Ordinance 689 (the street designation) not read; Ordinance 820's adoption day is blank on the copy read.",
  db_row=91,
 ),
 dict(
  slug="port-st-joe", name="Port St. Joe", st="FL", state="Florida", place="Port St. Joe, Florida",
  org="the City of Port St. Joe", Org="The City of Port St. Joe", publish=True,
  official=("the city&rsquo;s golf cart ordinance, Ordinance 550 (PDF)", "https://www.cityofportstjoe.com/ordinances/Golf%20Cart%20Ordinance%20550.pdf"),
  hub="City roads posted 30 mph or less. $10 yearly decal; 16+ with a license.",
  answer="Port St. Joe lets registered golf carts use city roads posted 30 mph or less, with short limits on Garrison and Long Avenues. "
         "Drivers must be 16 with a driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes, a <strong>valid driver&rsquo;s license</strong> at 16 or older. A learner&rsquo;s permit holder may drive with a licensed driver 18 or older along.</p>",
   age="<p>At least <strong>16</strong> with a license, or a learner&rsquo;s permit holder with a licensed adult. Nobody under 14 may drive.</p>",
   permit="<p>Yes. Carts are registered with the city every year for $10, with a decal and a police inspection. Owners 65 and over pay a one-time fee. "
          "Bring proof of ownership, your driver&rsquo;s license and a signed statement that the cart complies.</p>",
   where="<p><strong>All city roads posted 30 mph or less</strong>, except that on Garrison Avenue and Long Avenue a cart may only drive to the next side street, never more than two blocks.</p>"
         "<p>Not on state highways or county roads, except to cross at designated intersections to reach the next designated road. "
         "No sidewalks, bike paths, swales or trails. Carts can&rsquo;t go faster than 20 mph.</p>",
   lsv=FL_LSV,
   hours="<p>Sunrise to sunset. Equipped carts may run from sunset to midnight, and the City Commission may allow midnight to sunrise by resolution.</p>"
         "<p>Required equipment: brakes, steering, tires, mirrors, red reflectors front and rear, headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Passengers and fines",
    "<p>Riders are limited to the number of seats, and children ride in child restraints as state law requires. Alcohol laws apply. "
    "Fines: a warning, then $100, $200 and $300.</p>"),
  ],
  sources=[
   ("Ordinance 550, golf carts (June 4, 2019) &mdash; City of Port St. Joe (PDF)", "https://www.cityofportstjoe.com/ordinances/Golf%20Cart%20Ordinance%20550.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know Port St. Joe&rsquo;s 30 mph line, the Garrison and Long Avenue limits, "
         "or the hours yet, so a route can use a 35 mph road. Check the rules above before you ride.",
  prio="beach", prio_note="Gulf coast town near Cape San Blas",
  quality="high", source_type="ordinance PDF (city site)", checked="2026-10-16",
  gap="Covers the city only: Gulf County (St. Joe Beach, Cape San Blas, Indian Pass) rules not online in full.",
  db_row=111,
 ),
 dict(
  slug="key-biscayne", name="Key Biscayne", st="FL", state="Florida", place="Key Biscayne, Florida",
  org="the Village of Key Biscayne", Org="The Village of Key Biscayne", publish=True,
  official=("the village police news release on the golf cart rules (PDF)", "https://files.keybiscayne.fl.gov/Documents/Services/Police/KBPD%20Resources/KBPD%20News%20Releases/2022/NR%202022-007%20Golf%20Cart%20Ordinance%20April%2013_2022.pdf"),
  publishes="The Village of Key Biscayne publishes its golf cart rules. Here&rsquo;s a plain-English summary.",
  hub="Village roads with a village permit; Crandon Blvd only to cross. Driver&rsquo;s license.",
  answer="Key Biscayne lets golf carts use village roads with a village permit and a licensed driver. "
         "Crandon Boulevard, a county road, is only for crossing or reaching the next intersection.",
  faq=dict(
   license="<p>Yes. Drivers need a <strong>valid driver&rsquo;s license</strong>.</p>",
   age="<p>The village ties driving to the license rather than to an age: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. A village police permit, fixed to the cart.</p>",
   where="<p><strong>Village roads.</strong> On Crandon Boulevard, a county road, carts may only cross at an intersection or drive to the next intersection.</p>",
   lsv=FL_LSV,
   hours="<p>We didn&rsquo;t find hours in the village&rsquo;s release. Under Florida law, golf carts run from sunrise to sunset, unless the local government allows night use "
         "and the cart has headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Passengers and fines",
    "<p>No more passengers than the cart is built for. Fines are $75 the first time and $175 the second.</p>"),
  ],
  sources=[
   ("Golf cart rules news release, April 13, 2022 &mdash; Key Biscayne Police Department (PDF)", "https://files.keybiscayne.fl.gov/Documents/Services/Police/KBPD%20Resources/KBPD%20News%20Releases/2022/NR%202022-007%20Golf%20Cart%20Ordinance%20April%2013_2022.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know that Crandon Boulevard is for crossing only, "
         "so if a route runs along Crandon, don&rsquo;t take it in a cart.",
  prio="beach", prio_note="Island village off Miami",
  quality="medium", source_type="village police news release", checked="2026-10-15",
  gap="Village Code ch. 26, art. II (revised April 12, 2022) not read; the page rests on the police release.",
  db_row=78,
 ),
 dict(
  slug="apollo-beach", name="Apollo Beach", st="FL", state="Florida", place="Apollo Beach, Florida (Hillsborough County)",
  org="Hillsborough County", Org="Hillsborough County", publish=True,
  official=("the county&rsquo;s golf cart designation page", "https://hcfl.gov/residents/property-owners-and-renters/roads-and-sidewalks/request-golf-cart-designation"),
  publishes="Hillsborough County publishes how its roads get designated for golf carts.",
  hub="Only county roads the county has designated and signed; we haven&rsquo;t verified public-road authorization here.",
  answer="In Apollo Beach, golf carts can use only county roads that Hillsborough County has designated and signed for them. "
         "The county designates roads on request. We haven&rsquo;t verified public-road authorization for any road in Apollo Beach.",
  faq=dict(
   license="<p>We didn&rsquo;t find a county license rule, so Florida&rsquo;s applies: drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license, "
           "and drivers 18 and over need a government-issued photo ID.</p>",
   age=FL_AGE,
   permit="<p>The county&rsquo;s pages describe how roads get designated, not a cart registration. A homeowners&rsquo; association, community development district "
          "or civic association asks; the county&rsquo;s traffic engineers study speed, traffic, sight distance, the mix of vehicles and connections, which can take up to "
          "120 business days; then the county posts signs.</p>",
   where="<p>Only on roads the county has <strong>designated and signed</strong> for golf carts. The county designates only roads posted <strong>30 mph or less</strong>, "
         "and sidewalk paths at least 8 feet wide. The county doesn&rsquo;t publish a list, and we haven&rsquo;t verified public-road authorization for any road in Apollo Beach. "
         "Elsewhere, Florida law keeps golf carts off public roads.</p>",
   lsv=FL_LSV,
   hours=FL_HOURS,
  ),
  extra=[],
  sources=[
   ("Request Golf Cart Designation &mdash; Hillsborough County", "https://hcfl.gov/residents/property-owners-and-renters/roads-and-sidewalks/request-golf-cart-designation"),
   ("Golf cart designation questions and answers &mdash; Hillsborough County (PDF)", "https://assets.contentstack.io/v3/assets/blteea73b27b731f985/blt97929bd683e191e1/Golf_Cart_Designation.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know which roads Hillsborough County has designated for carts, "
         "so a route can use a road carts can&rsquo;t. Look for posted golf cart signs before you ride.",
  prio="beach", prio_note="Tampa Bay waterfront community",
  quality="medium", source_type="county web page + county FAQ PDF", checked="2026-10-16",
  gap="No public list of designated roads; the county map viewer was not opened; no ordinance number cited.",
  db_row=43,
 ),
 dict(
  slug="port-richey", name="Port Richey", st="FL", state="Florida", place="Port Richey, Florida",
  org="the City of Port Richey", Org="The City of Port Richey", publish=True,
  official=("the city police golf cart brochure (PDF)", "https://www.cityofportrichey.gov/DocumentCenter/View/1009"),
  hub="All city streets except US 19 and a list of busier roads. Yearly decal, insurance; driver&rsquo;s license.",
  answer="Port Richey lets registered golf carts use all city streets except a list of busier roads, including US 19. "
         "Every driver needs a valid driver&rsquo;s license, and carts need a yearly city decal and liability insurance.",
  faq=dict(
   license="<p>Yes. The city requires a <strong>valid driver&rsquo;s license</strong> for every driver. That&rsquo;s stricter than Florida&rsquo;s general rule.</p>",
   age="<p>The city ties driving to the license rather than to an age: every driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. A yearly city registration decal goes on the lower driver&rsquo;s side of the windshield; New Port Richey decals are accepted too. "
          "Liability insurance is required.</p>"
          "<p>Equipment: brakes, red reflectors front and back, a mirror, steering and safe tires.</p>",
   where="<p><strong>All city streets</strong>, except these (red on the brochure&rsquo;s map):</p>"
         "<ul><li>US 19 (SR 55), Ridge Road, Washington Street, Oelsner Street, Limit Drive and Leo Kidd Avenue</li>"
         "<li>Pine Hill Road east of Applesix Drive, and Old Post Road north of Koons Road</li>"
         "<li>Springer Drive, Old Ridge Road, Squib Drive, Bench Drive and Rees Street</li></ul>"
         "<p>There are no state-approved golf cart crossings of US 19 in the city. The brochure says carts may use sidewalks beside state roads only where "
         "the sidewalk is at least 8 feet wide, signed, and ridden at 15 mph or less, and beside local roads where it is at least 5 feet wide.</p>",
   lsv="<p>An LSV needs a title, a license plate and a licensed driver.</p>" + FL_LSV,
   hours=FL_HOURS,
  ),
  extra=[],
  sources=[
   ("Golf cart brochure and street map &mdash; City of Port Richey Police (PDF)", "https://www.cityofportrichey.gov/DocumentCenter/View/1009"),
   FL_316212, FL_3162122,
  ],
  street_map=("the Port Richey police golf cart brochure (includes a map)", "https://www.cityofportrichey.gov/DocumentCenter/View/1009"),
  slowgo="It doesn&rsquo;t know Port Richey&rsquo;s list of closed streets yet, "
         "so a route could use one of them. Check the list above before you ride, and don&rsquo;t cross US 19 in a cart.",
  prio="beach", prio_note="Gulf coast waterfront city (Pasco County)",
  quality="medium", source_type="city police brochure PDF", checked="2026-10-15",
  gap="City Code sec. 36-162 not read; brochure date unknown.",
  db_row=110,
 ),
 dict(
  slug="keaton-beach", name="Keaton Beach", st="FL", state="Florida", place="Keaton Beach, Florida (Taylor County)",
  org="Taylor County", Org="Taylor County", publish=True,
  official=("Taylor County Ordinance 2023-06 (PDF)", "https://www.taylorcountygov.com/2023-06%20-%20Golf%20Carts%20-%20Keaton%20Beach.pdf"),
  publishes="Taylor County publishes the golf cart rules for Keaton Beach.",
  hub="Golf carts throughout the Keaton Beach area, Saw Grass Estates to J. L. Gibson Road.",
  answer="Taylor County allows golf carts in the Keaton Beach area, from Saw Grass Estates to J. L. Gibson Road and throughout Keaton Beach. "
         "The county&rsquo;s other golf cart rules apply there too; we haven&rsquo;t read them yet.",
  faq=dict(
   license="<p>We haven&rsquo;t read the county&rsquo;s general golf cart rules (County Code section 74-4), so we fall back on Florida&rsquo;s: drivers under 18 need "
           "a learner&rsquo;s permit or a driver&rsquo;s license, and drivers 18 and over need a government-issued photo ID. The county&rsquo;s rule may be stricter.</p>",
   age=FL_AGE,
   permit="<p>We haven&rsquo;t read the county&rsquo;s general golf cart rules, so we can&rsquo;t say whether a county registration is needed. Ask Taylor County.</p>"
          f"<p>Under Florida law a cart needs {FL_DAY_EQUIP}.</p>",
   where="<p>The Keaton Beach area, <strong>from Saw Grass Estates to J. L. Gibson Road and throughout Keaton Beach</strong>, as Ordinance 2023-06 (June 20, 2023) describes it. "
         "The ordinance describes the area in words; there&rsquo;s no map.</p>",
   lsv=FL_LSV,
   hours=FL_HOURS,
  ),
  extra=[],
  sources=[
   ("Ordinance 2023-06, golf carts at Keaton Beach (June 20, 2023) &mdash; Taylor County (PDF)", "https://www.taylorcountygov.com/2023-06%20-%20Golf%20Carts%20-%20Keaton%20Beach.pdf"),
   ("Ordinances &mdash; Taylor County", "https://www.taylorcountygov.com/government/ordinances/index.php"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know where the Keaton Beach cart area ends yet, "
         "so a route can leave it. Stay within the area described above.",
  prio="beach", prio_note="Big Bend Gulf beach community",
  quality="high", source_type="ordinance PDF (county site)", checked="2026-10-15",
  gap="Base County Code sec. 74-4 (license, registration, hours, equipment) not read; Florida defaults shown instead.",
  db_row=77,
 ),
 dict(
  slug="steinhatchee", name="Steinhatchee", st="FL", state="Florida", place="Steinhatchee, Florida (Taylor County)",
  org="Taylor County", Org="Taylor County", publish=True,
  official=("Taylor County Ordinance 2023-07 (PDF)", "https://www.taylorcountygov.com/2023-07%20-%20Golf%20Carts%20Steinhatchee.pdf"),
  publishes="Taylor County publishes the golf cart rules for Steinhatchee.",
  hub="Every county-maintained road posted 25 mph or less.",
  answer="In Steinhatchee, golf carts can use every county-maintained road posted 25 mph or less. "
         "Taylor County&rsquo;s other golf cart rules still apply; we haven&rsquo;t read them yet.",
  faq=dict(
   license="<p>We haven&rsquo;t read the county&rsquo;s general golf cart rules (County Code section 74-4), so we fall back on Florida&rsquo;s: drivers under 18 need "
           "a learner&rsquo;s permit or a driver&rsquo;s license, and drivers 18 and over need a government-issued photo ID. The county&rsquo;s rule may be stricter.</p>",
   age=FL_AGE,
   permit="<p>We haven&rsquo;t read the county&rsquo;s general golf cart rules, so we can&rsquo;t say whether a county registration is needed. Ask Taylor County.</p>"
          f"<p>Under Florida law a cart needs {FL_DAY_EQUIP}.</p>",
   where="<p><strong>All county-maintained roads in Steinhatchee posted 25 mph or less</strong> (Ordinance 2023-07, June 20, 2023). "
         "The county board may change that limit by resolution.</p>",
   lsv=FL_LSV,
   hours=FL_HOURS,
  ),
  extra=[],
  sources=[
   ("Ordinance 2023-07, golf carts in Steinhatchee (June 20, 2023) &mdash; Taylor County (PDF)", "https://www.taylorcountygov.com/2023-07%20-%20Golf%20Carts%20Steinhatchee.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know Steinhatchee&rsquo;s 25 mph line yet, "
         "so a route here can include a 30 or 35 mph road that carts can&rsquo;t use.",
  prio="beach", prio_note="Big Bend Gulf fishing and scalloping town",
  quality="high", source_type="ordinance PDF (county site)", checked="2026-10-15",
  gap="Base County Code sec. 74-4 (license, registration, hours, equipment) not read; Florida defaults shown instead.",
  db_row=123,
 ),
]
