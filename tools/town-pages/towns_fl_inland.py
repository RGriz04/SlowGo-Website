# Florida inland and suburban town pages (scale-up, 2026-10-17).
# Every rule comes from the row in the cart-towns database (cart-towns-2026-10-16.csv, row index in
# db_row) and the city/county/state source it cites. No Municode links. Schema as in towns.py, plus the
# review fields prio, prio_note, quality, source_type, checked, gap, db_row.

from towns import FL_LSV, FL_316212, FL_3162122

FL_AGE = ("<p>Florida law: drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license, "
          "and drivers 18 and over need a government-issued photo ID.</p>")
FL_HOURS_DEFAULT = ("<p>We didn&rsquo;t find a local hours rule. Under Florida law, golf carts may use roads only from sunrise to sunset, "
                    "unless the local government allows night use and the cart has headlights, brake lights, turn signals and a windshield.</p>")
FL_EQUIP = "good brakes, reliable steering, safe tires, a rearview mirror, and red reflectors front and rear"

TOWNS = [
 dict(
  slug="north-port", name="North Port", st="FL", state="Florida", place="North Port, Florida",
  org="the City of North Port", Org="The City of North Port", publish=True,
  official=("the police department&rsquo;s Golf Cart Requirements page", "https://www.northportfl.gov/City-Services-and-Safety/Emergency-Services/Police/Golf-Cart-Requirements"),
  hub="Only signed roads in Holiday Park, Lakeside Plantation and Plantation Blvd, posted 30 mph or less.",
  answer="In North Port, golf carts can use only the signed roads the city has designated: the city roads in the Holiday Park Recreational District "
         "and Lakeside Plantation, plus Plantation Boulevard, all posted 30 mph or less. There&rsquo;s no city registration for carts.",
  faq=dict(
   license="<p>Not always. The city follows Florida law: drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license, "
           "and drivers 18 and over need a government-issued photo ID.</p>",
   age=FL_AGE,
   permit="<p>No. The police department&rsquo;s page says golf carts don&rsquo;t need a title, registration or insurance.</p>",
   where="<p>Only the designated, signed roads, all posted <strong>30 mph or less</strong>:</p>"
         "<ul><li>all city roads in the Holiday Park Recreational District</li>"
         "<li>all city roads in the Lakeside Plantation community</li>"
         "<li>Plantation Boulevard</li></ul>"
         "<p>A cart may cross a county road where it meets an approved cart road, a golf course or a mobile home park.</p>",
   lsv="<p>A low-speed vehicle (LSV) is different from a golf cart: it goes faster than 20 mph (up to 25), and it must be titled, registered and insured, "
       "with a licensed driver. LSVs can use roads posted 35 mph or less, but North Port bans them, whatever the speed limit, on "
       "Atwater Drive, Biscayne Drive, Chamberlain Boulevard, Cranberry Boulevard, Haberland Boulevard, Pan American Boulevard, Panacea Boulevard, "
       "Price Boulevard, Salford Boulevard, San Mateo Drive, Sumter Boulevard and Toledo Blade Boulevard.</p>",
   hours=FL_HOURS_DEFAULT,
  ),
  extra=[],
  sources=[
   ("Golf Cart Requirements &mdash; North Port Police Department", "https://www.northportfl.gov/City-Services-and-Safety/Emergency-Services/Police/Golf-Cart-Requirements"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know North Port&rsquo;s designated cart roads or its LSV bans yet, "
         "so a route can leave Holiday Park, Lakeside Plantation or Plantation Boulevard, or use a boulevard closed to LSVs. Check the list above before you ride.",
  prio="retirement", prio_note="Holiday Park and Lakeside Plantation communities; large retiree city",
  quality="medium", source_type="official city police page", checked="2026-10-15",
  gap="City code sec. 74-152(b) not read; content from the police department's page only. Hours and equipment rules not on that page (state default shown).",
  db_row=98,
 ),
 dict(
  slug="oldsmar", name="Oldsmar", st="FL", state="Florida", place="Oldsmar, Florida",
  org="the City of Oldsmar", Org="The City of Oldsmar", publish=True,
  official=("the city&rsquo;s Golf Cart Ordinance page", "https://oldsmarfl.gov/1032/Golf-Cart-Ordinance"),
  hub="City streets posted 25 mph or less, except the two industrial parks. Insurance required.",
  answer="Oldsmar lets golf carts use city streets posted 25 mph or less, except the streets in its two industrial parks. "
         "Carts must have liability insurance; city registration is optional.",
  faq=dict(
   license="<p>The city&rsquo;s ordinance page doesn&rsquo;t set its own license rule. Florida law applies: drivers under 18 need a learner&rsquo;s permit "
           "or a driver&rsquo;s license, and drivers 18 and over need a government-issued photo ID.</p>",
   age=FL_AGE,
   permit="<p>Liability insurance is required. Registration with the city is optional: a registered cart is inspected and gets a decal, "
          "with a yearly fee set by the city. The cart can&rsquo;t be able to go faster than 20 mph.</p>"
          f"<p>Required equipment: {FL_EQUIP}, plus a horn.</p>",
   where="<p><strong>City streets</strong>, on the paved part only, except:</p>"
         "<ul><li>streets posted over 25 mph, including Commerce Boulevard, Douglas Road east of Commerce, Pine Avenue from Forest Road to Forest Lakes Boulevard, "
         "and St. Petersburg Drive from SR 580 to East Dartmouth</li>"
         "<li>the streets of the Cypress Lakes Industrial Park: Brooker Creek Boulevard, Burbank Road, Commerce Boulevard, Douglas Road east of Commerce, "
         "Dunbar Avenue, Dunbar Court, Roberts Road, Stevens Avenue, Tower Drive and Vollmer Avenue</li>"
         "<li>the streets of the Mears Industrial Park: Avon Street, Bayview Boulevard from Tampa Road to SR 580, Derek Lane, Marlborough Street, Mears Boulevard, "
         "Mt. Vernon Street, Myrtle Lane, Pinckney Street, Pine Avenue from Marlborough to Tampa Road, Scarlet Boulevard and Sellers Lane</li></ul>"
         "<p>Park roads and the parking areas set aside in parks are fine. The Oldsmar Trail is not. "
         "No driving on or across state or county roads, except at crossings the state or county allows.</p>",
   lsv=FL_LSV,
   hours="<p>Yes, from sunset to sunrise, if the cart also has headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Passengers and parking",
    "<p>No more riders than seats, nobody standing, and don&rsquo;t hold up traffic. In public parking spaces, carts may park side by side.</p>"),
  ],
  sources=[
   ("Golf Cart Ordinance (City Code ch. 66, art. IV), adopted April 4, 2023 &mdash; City of Oldsmar", "https://oldsmarfl.gov/1032/Golf-Cart-Ordinance"),
   ("Golf cart exclusion map &mdash; City of Oldsmar", "https://oldsmarfl.gov/ImageRepository/Document?documentId=10716"),
   FL_316212, FL_3162122,
  ],
  street_map=("the city&rsquo;s golf cart exclusion map", "https://oldsmarfl.gov/ImageRepository/Document?documentId=10716"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Oldsmar&rsquo;s 25 mph line or its industrial-park exclusions yet, "
         "so a route can use a 30 or 35 mph street, or a street carts can&rsquo;t use here. Check the city&rsquo;s map before you ride.",
  prio="cart-friendly", prio_note="Pinellas cart town with a full ordinance",
  quality="high", source_type="official city page reproducing ordinance text", checked="2026-10-16",
  gap="Ordinance number not printed on the city page; the city's FAQ (age details) not read.",
  db_row=99,
 ),
 dict(
  slug="winter-garden", name="Winter Garden", st="FL", state="Florida", place="Winter Garden, Florida",
  org="the City of Winter Garden", Org="The City of Winter Garden", publish=True,
  official=("the city&rsquo;s golf cart ordinance (PDF)", "https://www.cwgdn.com/DocumentCenter/View/2352/Ordinance-09-53---Golf-Cart-Operation"),
  hub="Only golf cart communities and streets approved by resolution, including the Downtown Golf Cart District.",
  answer="In Winter Garden, golf carts may use only the communities and streets the city has approved by resolution, such as the Downtown Golf Cart District. "
         "Everywhere else, public streets are closed to carts.",
  faq=dict(
   license="<p>The city&rsquo;s ordinance lets drivers without a license use a cart only if they&rsquo;re 18 or older and carry proof of a city-approved safety course. "
           "Florida law also applies: drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license.</p>",
   age="<p>Drivers without a license must be at least 18. Under Florida law, drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license.</p>",
   permit="<p>We didn&rsquo;t find a registration requirement in what we read. Carts need Florida&rsquo;s standard equipment: "
          f"{FL_EQUIP}.</p>",
   where="<p>Only <strong>golf cart communities and streets approved by city resolution</strong>, such as the Downtown Golf Cart District. "
         "Under the ordinance:</p>"
         "<ul><li>no roads posted over 25 mph, unless the resolution allows it</li>"
         "<li>a cart may cross a street posted over 25 and up to 35 mph only at a four-way stop or a traffic signal, to keep going along a 25 mph street</li>"
         "<li>no city arterial or collector roads, unless the resolution allows it</li>"
         "<li>no state highways</li></ul>"
         "<p>The district may have changed since those resolutions. We haven&rsquo;t read the current district resolution or map, "
         "and a resolution can allow a higher speed limit than 25, so check the city&rsquo;s current district map.</p>",
   lsv=FL_LSV,
   hours="<p>Sunrise to sunset. Where the resolution allows night use, carts may run from 5:00 a.m. to 10:00 p.m. if they have headlights, brake lights, "
         "turn signals, a windshield, and side reflectors or reflective tape.</p>",
  ),
  extra=[
   ("Communities",
    "<p>The city commission can take back a community&rsquo;s or a street&rsquo;s approval. Homeowners&rsquo; associations enforce their own rules.</p>"),
  ],
  sources=[
   ("Ordinance 09-53, Golf Cart Operation (City Code sec. 74-4) &mdash; City of Winter Garden (PDF)", "https://www.cwgdn.com/DocumentCenter/View/2352/Ordinance-09-53---Golf-Cart-Operation"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Winter Garden&rsquo;s approved cart streets or the downtown district&rsquo;s edges yet, "
         "so a route can use a street that isn&rsquo;t approved for carts. Check the city&rsquo;s district map before you ride.",
  prio="cart-friendly", prio_note="Downtown Golf Cart District, expanded 2026",
  quality="high", source_type="ordinance PDF (city site)", checked="2026-10-16",
  gap="Only the 2009 ordinance read. Resolutions 18-05 and 21-05 and the January 2026 district expansion (street list, map, possible 30 mph cap) not read.",
  db_row=133,
 ),
 dict(
  slug="oviedo", name="Oviedo", st="FL", state="Florida", place="Oviedo, Florida",
  org="the City of Oviedo", Org="The City of Oviedo", publish=True,
  official=("the city&rsquo;s Golf Cart Registration and Information page", "https://www.cityofoviedo.net/1259/Golf-Cart-Registration-and-Information"),
  hub="City roads posted 30 mph or less, minus a list of busy roads. $30 yearly registration.",
  answer="Oviedo lets registered, insured golf carts use city roads posted 30 mph or less, except a list of busier roads. "
         "Carts never go on state or county roads, and cross them only at signed traffic lights.",
  faq=dict(
   license="<p>Yes: a valid driver&rsquo;s license, or a learner&rsquo;s permit with a licensed driver 21 or older in the front seat.</p>",
   age="<p>The city ties driving to the license: a valid driver&rsquo;s license, or a learner&rsquo;s permit with a licensed driver 21 or older in the front seat.</p>",
   permit="<p>Yes. Register the cart with the city every year ($30, in person) with proof of insurance; the sticker goes on the rear. "
          "The cart can&rsquo;t be able to go faster than 20 mph.</p>"
          "<p>Required equipment: brakes, steering, tires, a rearview mirror, a horn, red reflectors, a windshield, turn signals, taillights, headlights and seat belts.</p>",
   where="<p>City roads posted <strong>30 mph or less</strong>, except:</p>"
         "<ul><li>Alafaya Trail (SR 434) and Central Avenue N/S (SR 434)</li>"
         "<li>Aloma Avenue (SR 426) and W Broadway Street (SR 426)</li>"
         "<li>E Broadway Street (CR 419) and CR 419 east of Lockwood Boulevard</li>"
         "<li>W Chapman Road, Oviedo Mall Boulevard, Lockwood Boulevard and Mitchell Hammock Road E/W</li>"
         "<li>Geneva Drive from the roundabout north to the city limits</li></ul>"
         "<p>Never on state or county roads. Carts may cross them only at signed traffic lights, where Seminole County or FDOT has approved it. "
         "No sidewalks, bike paths, swales or trails. The city council can add roads by resolution.</p>",
   lsv="<p>The city&rsquo;s page says a plated cart is treated as a low-speed vehicle (LSV) and doesn&rsquo;t need city registration. "
       "Under Florida law an LSV goes faster than 20 mph (up to 25), is titled, registered and insured, has a licensed driver, "
       "and can use streets posted 35 mph or less.</p>",
   hours="<p>From 6:00 a.m. to 2:00 a.m.</p>",
  ),
  extra=[
   ("Passengers", "<p>No more riders than the cart has seats.</p>"),
  ],
  sources=[
   ("Golf Cart Registration and Information &mdash; City of Oviedo", "https://www.cityofoviedo.net/1259/Golf-Cart-Registration-and-Information"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Oviedo&rsquo;s 30 mph line or its closed roads yet, "
         "so a route can use a 35 mph street or one of the roads above. Check the list before you ride.",
  prio="cart-friendly", prio_note="City-wide cart registration program",
  quality="medium", source_type="official city page (read directly)", checked="2026-10-16",
  gap="Ordinance number not on the city page; code text not read.",
  db_row=101,
 ),
 dict(
  slug="clermont", name="Clermont", st="FL", state="Florida", place="Clermont, Florida",
  org="the City of Clermont", Org="The City of Clermont", publish=True,
  official=("the city&rsquo;s 2026 golf cart registration form (PDF)", "https://www.clermontfl.gov/DocumentCenter/View/3787/Golf-Cart-Registration-2026"),
  hub="A pilot program: city roads west of US 27 and north of SR 50. $20 registration.",
  answer="Clermont is running a three-year golf cart pilot: registered carts may use city roads west of US 27 and north of SR 50. "
         "The pilot may end February 10, 2029.",
  faq=dict(
   license="<p>Not always. The city&rsquo;s form asks for a valid license (a learner&rsquo;s permit counts), or for drivers 18 and over, a government-issued photo ID.</p>",
   age="<p>Under 18, a learner&rsquo;s permit or a driver&rsquo;s license. 18 and over, a government-issued photo ID.</p>",
   permit="<p>Yes. Register the cart with the city ($20); the sticker goes on the driver&rsquo;s side. The form includes a notarized hold-harmless statement.</p>"
          "<p>Required equipment: brakes, tires, a mirror, and red reflectors front and rear.</p>",
   where="<p>City of Clermont roads <strong>west of US 27 and north of SR 50</strong>, under Ordinance 2026-002. "
         "Not on the South Lake Trail. Normal traffic laws apply.</p>",
   lsv=FL_LSV,
   hours="<p>At night, only with headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("A pilot program",
    "<p>The pilot runs for three years and may end February 10, 2029. The city&rsquo;s older regulations page said carts weren&rsquo;t allowed on city roads; "
    "the 2026 pilot replaced that.</p>"),
  ],
  sources=[
   ("Golf Cart Registration 2026 (Ordinance 2026-002), with map &mdash; City of Clermont (PDF)", "https://www.clermontfl.gov/DocumentCenter/View/3787/Golf-Cart-Registration-2026"),
   FL_316212, FL_3162122,
  ],
  street_map=None,   # the map is attached to the registration form (a source below); no separate map page, so no map line
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Clermont&rsquo;s pilot area yet, "
         "so a route can go east of US 27 or south of SR 50, where carts can&rsquo;t ride. Check the map before you ride.",
  prio="cart-friendly", prio_note="New 2026 pilot near Lake County retirement communities",
  quality="medium", source_type="official city registration form", checked="2026-10-16",
  gap="The ordinance's operative section not read (form only); the map was not located separately from the form.",
  db_row=53,
 ),
 dict(
  slug="st-cloud", name="St. Cloud", st="FL", state="Florida", place="St. Cloud, Florida",
  org="the City of St. Cloud", Org="The City of St. Cloud", publish=True,
  official=("the city&rsquo;s Golf Cart Registration page", "https://www.stcloudfl.gov/2193/Golf-Cart-Registration"),
  hub="A downtown zone between US 192 and Lakeshore Blvd. $25 yearly registration and inspection.",
  answer="St. Cloud lets registered, inspected golf carts use the city streets north of US 192 (13th Street) to Lakeshore Boulevard, "
         "between Columbia Avenue and Eastern Avenue. The owner drives, with a license and insurance.",
  faq=dict(
   license="<p>Yes. The city&rsquo;s page says the driver needs a valid driver&rsquo;s license and must be the cart&rsquo;s lawful owner.</p>",
   age="<p>The city ties driving to the license: a licensed owner-operator.</p>",
   permit="<p>Yes. Register the cart every year ($25, or $6.25 a quarter), with a yearly inspection and liability insurance.</p>"
          f"<p>Required equipment: {FL_EQUIP}, plus a horn.</p>",
   where="<p>City streets in the zone <strong>north of US 192 (13th Street) to Lakeshore Boulevard, from Columbia Avenue on the west to Eastern Avenue on the east</strong>, "
         "except where the city prohibits them. Keep right, stay off sidewalks, yield to pedestrians, and never go over the posted limit.</p>",
   lsv=FL_LSV,
   hours="<p>At night, only with headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Tickets", "<p>The city&rsquo;s page lists a $25 citation, plus $15 if paid late.</p>"),
  ],
  sources=[
   ("Golf Cart Registration &mdash; City of St. Cloud", "https://www.stcloudfl.gov/2193/Golf-Cart-Registration"),
   ("Golf cart boundary map &mdash; City of St. Cloud", "https://www.stcloudfl.gov/DocumentCenter/View/32845/Golf-Cart-BoundaryPNG"),
   FL_316212, FL_3162122,
  ],
  street_map=("the city&rsquo;s golf cart boundary map", "https://www.stcloudfl.gov/DocumentCenter/View/32845/Golf-Cart-BoundaryPNG"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know St. Cloud&rsquo;s cart zone yet, "
         "so a route can leave the zone. Check the city&rsquo;s map before you ride.",
  prio="cart-friendly", prio_note="Downtown cart zone",
  quality="medium", source_type="official city page", checked="2026-10-16",
  gap="No ordinance number or code section on the city page or form. The page's 'maximum attainable speed of 30 mph' wording looks like an error and is not repeated.",
  db_row=119,
 ),
 dict(
  slug="celebration", name="Celebration", st="FL", state="Florida", place="Celebration, Florida (Osceola County)",
  org="Osceola County", Org="Osceola County", publish=True,
  official=("the county&rsquo;s golf cart policy (PDF)", "https://osceolacofl.prelive.opencities.com/files/assets/county/v/1/services/transportation-and-transit-dept-services/documents/golf-cart-policy-and-application.pdf"),
  publishes="Osceola County publishes the golf cart rules that cover Celebration. Here&rsquo;s a plain-English summary.",
  hub="Golf carts aren&rsquo;t allowed on county roads here; LSVs follow state law.",
  answer="Golf carts aren&rsquo;t allowed on Osceola County roads in Celebration: the county keeps carts off its roads unless it passes an ordinance for a community, "
         "and we found none for Celebration. Low-speed vehicles (LSVs) can use streets posted 35 mph or less under Florida law.",
  faq=dict(
   license="<p>Golf carts aren&rsquo;t allowed on Celebration&rsquo;s county roads, as far as we found. An LSV driver needs a valid driver&rsquo;s license.</p>",
   age="<p>The county&rsquo;s policy doesn&rsquo;t set an age for Celebration, since carts aren&rsquo;t allowed there. Where carts are allowed in Florida, "
       "drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license, and drivers 18 and over need a government-issued photo ID.</p>",
   permit="<p>There&rsquo;s no cart permit for Celebration. A community can ask the county to open its roads: a homeowner or HOA application, a petition signed by 51% of owners, "
          "a county traffic study (the fee can be up to $6,500), and a county ordinance, with the applicant paying for the signs.</p>",
   where="<p><strong>Not on Osceola County roads or sidewalks.</strong> The county prohibits golf carts on or along its roads and sidewalks unless an engineering study supports it "
         "and the county board adopts an ordinance for that community. The county has done that for Harmony and Pine Grove; we found no such ordinance for Celebration.</p>"
         "<p>Some Celebration streets may belong to a community district or be private. Their owners set the rules there.</p>",
   lsv=FL_LSV,
   hours="<p>For golf carts, the question doesn&rsquo;t come up on county roads here. LSVs follow Florida law.</p>",
  ),
  extra=[],
  sources=[
   ("Golf Cart Policy and Application &mdash; Osceola County (PDF)", "https://osceolacofl.prelive.opencities.com/files/assets/county/v/1/services/transportation-and-transit-dept-services/documents/golf-cart-policy-and-application.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know that golf carts are barred from Celebration&rsquo;s county roads, "
         "so it will still plan a route for a golf cart here. Don&rsquo;t take that route in a golf cart; an LSV can use it.",
  prio="cart-friendly", prio_note="Well-known planned community people search for carts in; no-designation page",
  quality="medium", source_type="county policy PDF (county site)", checked="2026-10-16",
  gap="Absence-based: no Celebration ordinance found (only Harmony and Pine Grove, Ord. 2019-54, not opened). The policy PDF sits on the county's 'prelive' web host. Which Celebration streets are district or private wasn't checked.",
  db_row=51,
 ),
 dict(
  slug="lynn-haven", name="Lynn Haven", st="FL", state="Florida", place="Lynn Haven, Florida",
  org="the City of Lynn Haven", Org="The City of Lynn Haven", publish=True,
  official=("the city&rsquo;s City Golf Cart Information page", "https://www.cityoflynnhaven.gov/280/City-Golf-Cart-Information"),
  hub="City streets in designated subdivisions, posted 25 mph or less.",
  answer="Lynn Haven limits golf carts to city streets inside the subdivisions the city commission has designated, and only streets posted 25 mph or less. "
         "Carts can&rsquo;t use or cross state highways or county roads without Bay County or FDOT approval.",
  faq=dict(
   license="<p>Not always. Drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license; drivers 18 and over need a government-issued photo ID.</p>",
   age="<p>Under 18, a learner&rsquo;s permit or a driver&rsquo;s license. 18 and over, a government-issued photo ID.</p>",
   permit="<p>The city&rsquo;s summary of the ordinance doesn&rsquo;t mention a registration.</p>"
          f"<p>Daytime equipment: {FL_EQUIP}.</p>",
   where="<p>City streets <strong>inside the limited-access subdivisions</strong> the city commission has designated by resolution, "
         "and only streets posted <strong>25 mph or less</strong>. Not along or across any state highway or county road unless Bay County or FDOT allows it.</p>",
   lsv=FL_LSV,
   hours="<p>In daylight. At night, only with built-in headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("The ordinance", "<p>Ordinance 1156, adopted June 27, 2023 and in effect since October 1, 2023, sets these rules. "
                     "A violation is a noncriminal traffic infraction.</p>"),
  ],
  sources=[
   ("City Golf Cart Information &mdash; City of Lynn Haven", "https://www.cityoflynnhaven.gov/280/City-Golf-Cart-Information"),
   ("Lynn Haven Living, September 2023 (summary of Ordinance 1156) &mdash; City of Lynn Haven (PDF)", "https://www.cityoflynnhaven.com/DocumentCenter/View/2681/Lynn-Haven-Living---September-Issue"),
   ("Golf cart map (updated May 28, 2020) &mdash; City of Lynn Haven (PDF)", "https://www.cityoflynnhaven.gov/DocumentCenter/View/986/Golf-Cart-Map-updated-05-28-20-PDF"),
   FL_316212, FL_3162122,
  ],
  street_map=("the city&rsquo;s golf cart map", "https://www.cityoflynnhaven.gov/DocumentCenter/View/986/Golf-Cart-Map-updated-05-28-20-PDF"),
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Lynn Haven&rsquo;s designated subdivisions or its 25 mph line yet, "
         "so a route can leave them or use a faster street. Check the city&rsquo;s map before you ride.",
  prio="cart-friendly", prio_note="Bay County cart town near Panama City",
  quality="medium", source_type="official city page + official city newsletter summary of Ord. 1156", checked="2026-10-16",
  gap="Ordinance 1156 text not read (summary in the city newsletter only). The map dates from 2020, before the 2023 ordinance.",
  db_row=87,
 ),
 dict(
  slug="cutler-bay", name="Cutler Bay", st="FL", state="Florida", place="Cutler Bay, Florida",
  org="the Town of Cutler Bay", Org="The Town of Cutler Bay", publish=True,
  official=("the town&rsquo;s golf cart page", "https://www.cutlerbay-fl.gov/node/2551"),
  hub="All town streets except US-1, the Turnpike and a short list of busy stretches. One-time $60 permit.",
  answer="Cutler Bay opens its town streets to permitted golf carts, except US-1, the Florida Turnpike and a short list of busier stretches. "
         "Drivers need a valid driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. The town&rsquo;s registration rules call for a valid driver&rsquo;s license.</p>",
   age="<p>The town ties driving to the license: the driver needs a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. A one-time $60 permit (no renewal), shown on the rear fender, with a notarized affidavit and proof of insurance. "
          "Driving an unregistered cart can bring a $150 fine. A Cutler Bay permit also works on local roads in Palmetto Bay.</p>"
          "<p>Equipment: what Florida law requires (the affidavit says so).</p>",
   where="<p><strong>All town streets</strong>, except:</p>"
         "<ul><li>US-1 and the Florida Turnpike</li>"
         "<li>Caribbean Boulevard from US-1 to SW 107 Avenue</li>"
         "<li>Marlin Road from US-1 to Sterling Drive</li>"
         "<li>SW 97 Avenue from SW 212 to SW 216 Street</li>"
         "<li>SW 211 Street from SW 112 to SW 107 Avenue</li>"
         "<li>SW 216 Street from Old Cutler Road to SW 87 Avenue</li></ul>",
   lsv=FL_LSV,
   hours=FL_HOURS_DEFAULT,
  ),
  extra=[],
  sources=[
   ("Golf carts &mdash; Town of Cutler Bay (Ordinances 10-03 and 15-08, Town Code sec. 30-422)", "https://www.cutlerbay-fl.gov/node/2551"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Cutler Bay&rsquo;s closed streets yet, "
         "so a route can use one of the roads above. Check the list before you ride.",
  prio="cart-friendly", prio_note="Miami-Dade town-wide cart permit",
  quality="medium", source_type="official town page", checked="2026-10-15",
  gap="The town's golf cart rules PDF (2016) not read; hours not found (state default shown).",
  db_row=56,
 ),
 dict(
  slug="palmetto-bay", name="Palmetto Bay", st="FL", state="Florida", place="Palmetto Bay, Florida",
  org="the Village of Palmetto Bay", Org="The Village of Palmetto Bay", publish=True,
  official=("the village&rsquo;s Golf Cart Registration page", "https://www.palmettobay-fl.gov/757/Golf-Cart-Registration"),
  hub="All village streets except Old Cutler Rd, US 1 and eight busy avenues and streets. Village permit.",
  answer="Palmetto Bay lets permitted golf carts use village streets, except Old Cutler Road, US 1 and eight busier avenues and streets. "
         "Drivers need a valid driver&rsquo;s license.",
  faq=dict(
   license="<p>Yes. Only licensed drivers.</p>",
   age="<p>The village ties driving to the license. The owner who registers the cart must be 18 or older.</p>",
   permit="<p>Yes. A village permit (or one from a neighboring town) is required: $50 the first time, $10 to renew, "
          "with a notarized affidavit and yearly proof of homeowner liability and property damage coverage. Driving without one can bring a $150 citation.</p>"
          "<p>Required equipment: locking brakes, steering, tires, mirrors, red reflectors, headlights, tail and brake lights, turn signals, seat belts, "
          "a reverse warning, a horn, safety labels, a serial plate and a windshield.</p>",
   where="<p><strong>All village streets</strong>, except:</p>"
         "<ul><li>Old Cutler Road and US 1 (Palmetto Bay Parkway)</li>"
         "<li>SW 136, SW 152, SW 168 and SW 184 Streets</li>"
         "<li>SW 67, SW 77, SW 87 and SW 97 Avenues</li></ul>"
         "<p>Old Cutler Road may be crossed only at marked or signalized intersections, where Miami-Dade County allows it. "
         "No sidewalks, swales or parks.</p>",
   lsv=FL_LSV,
   hours="<p>The village&rsquo;s form doesn&rsquo;t set hours, but every cart must have headlights, tail lights and brake lights.</p>",
  ),
  extra=[],
  sources=[
   ("Golf Cart Registration &mdash; Village of Palmetto Bay", "https://www.palmettobay-fl.gov/757/Golf-Cart-Registration"),
   ("Golf cart registration form (Village Code ch. 28) &mdash; Village of Palmetto Bay (PDF)", "https://www.palmettobay-fl.gov/DocumentCenter/View/3388"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know Palmetto Bay&rsquo;s closed streets yet, "
         "so a route can run along one of them. Check the list above before you ride.",
  prio="cart-friendly", prio_note="Miami-Dade village-wide cart permit",
  quality="medium", source_type="official village registration form quoting code", checked="2026-10-15",
  gap="The registration form mirrors the village code but isn't the codified text.",
  db_row=104,
 ),
 dict(
  slug="tequesta", name="Tequesta", st="FL", state="Florida", place="Tequesta, Florida",
  org="the Village of Tequesta", Org="The Village of Tequesta", publish=True,
  official=("the village&rsquo;s golf cart ordinance", "https://www.tequesta.org/DocumentView.asp?DID=31"),
  hub="Designated, signed village streets in the Country Club area. Yearly police registration.",
  answer="Tequesta allows golf carts only on the village streets it has designated and signed, in the Tequesta Country Club area. "
         "Carts are registered with the police every year, and drivers must be 16 with a license.",
  faq=dict(
   license="<p>Yes. A valid U.S. driver&rsquo;s license and a photo ID.</p>",
   age="<p>At least <strong>16</strong>, with a valid driver&rsquo;s license.</p>",
   permit="<p>Yes. Register the cart with the Tequesta Police Department every year: a fee, an inspection, a decal, and proof of liability insurance. "
          "The cart can&rsquo;t be able to go faster than 20 mph.</p>"
          f"<p>Required equipment: {FL_EQUIP}.</p>",
   where="<p>Only the village streets designated for carts and <strong>signed by the police</strong>, in the Tequesta Country Club area. "
         "The 2006 ordinance doesn&rsquo;t list the streets, so follow the signs.</p>",
   lsv="<p>Low-speed vehicles (LSVs) are registered with the state (FLHSMV). Under Florida law an LSV goes faster than 20 mph (up to 25), "
       "is titled, registered and insured, has a licensed driver, and can use streets posted 35 mph or less.</p>",
   hours="<p>From sunset to sunrise, only with headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[
   ("Passengers", "<p>No more riders than seats, and nobody standing.</p>"),
  ],
  sources=[
   ("Ordinance 606 (Village Code sec. 46-2), adopted August 17, 2006 &mdash; Village of Tequesta", "https://www.tequesta.org/DocumentView.asp?DID=31"),
   ("News and Events &mdash; Village of Tequesta", "https://www.tequesta.org/845/News-and-Events"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know which Tequesta streets are signed for carts, "
         "so a route can leave them. Follow the signs over the route.",
  prio="cart-friendly", prio_note="Country club community on the Palm Beach coast",
  quality="high", source_type="village ordinance text (Ord. 606) on village host", checked="2026-10-16",
  gap="2006 ordinance; later amendments not checked (current code not read). Street list not in the ordinance; Country Club area per the village page.",
  db_row=126,
 ),
 dict(
  slug="nassau-county", name="Nassau County", st="FL", state="Florida", place="Nassau County, Florida (unincorporated)",
  org="Nassau County", Org="Nassau County", publish=True,
  official=("the county&rsquo;s golf cart ordinance amendment (agenda copy)", "https://nassaucounty.novusagenda.com/AgendaPublic/AttachmentViewer.ashx?AttachmentID=23747&ItemID=11094"),
  publishes="Nassau County publishes its golf cart rules for the unincorporated county. Here&rsquo;s a plain-English summary.",
  hub="Only county roads designated by resolution, in daylight. County registration.",
  answer="In unincorporated Nassau County, golf carts may use only the county roads the county has designated, and only in daylight. "
         "Carts are registered with the county.",
  faq=dict(
   license="<p>Not always. Drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license; drivers 18 and over need a government-issued photo ID.</p>",
   age="<p>Under 18, a learner&rsquo;s permit or a driver&rsquo;s license. 18 and over, a government-issued photo ID. (The 2008 text said 16; the 2023 text follows state law.)</p>",
   permit="<p>Yes. Register the cart with the county&rsquo;s Development Services department. The fee is set by county resolution "
          "(it was $15 in 2008).</p>"
          f"<p>Required equipment: {FL_EQUIP}.</p>",
   where="<p>Only <strong>county roads designated for golf carts</strong>. Since the 2023 amendment, the county designates roads by resolution, "
         "after a petition signed by 51% of owners (or a request from an HOA, POA or community district) and an engineering review. "
         "The amendment dropped the old named list (Edwards Road, Randy Road and its connectors, Easy Street and Royal Palm Drive). "
         "We didn&rsquo;t find a current list of designated roads, so look for signs.</p>"
         "<p>Roads maintained by an HOA, POA or community district are up to that association.</p>",
   lsv=FL_LSV,
   hours="<p>No. Golf carts may use county roads only from sunrise to sunset.</p>",
  ),
  extra=[
   ("Fine print", "<p>The driver takes on the risk and holds the county harmless. A violation is a noncriminal traffic infraction.</p>"),
  ],
  sources=[
   ("Golf cart ordinance amendment (County Code sec. 18-10), 2023 agenda copy &mdash; Nassau County", "https://nassaucounty.novusagenda.com/AgendaPublic/AttachmentViewer.ashx?AttachmentID=23747&ItemID=11094"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know which Nassau County roads are designated for carts, or the daylight rule, "
         "so a route can use a road carts can&rsquo;t. Follow the signs, and ride before sunset.",
  prio="cart-friendly", prio_note="Northeast Florida county with a cart designation process",
  quality="high", source_type="county agenda packet ordinance text (strike-through draft)", checked="2026-10-16",
  gap="Read the 2023 amendment as an agenda draft (number blank); adopted number 2023-43 and the current fee seen only in a search snippet of the county form. No published list of designated roads.",
  db_row=95,
 ),
 dict(
  slug="st-johns-county", name="St. Johns County", st="FL", state="Florida", place="St. Johns County, Florida (unincorporated)",
  org="St. Johns County", Org="St. Johns County", publish=True,
  official=("the county&rsquo;s golf cart ordinance (PDF copy)", "https://riversedgecdd.com/wp-content/uploads/2019/06/sjc-golf-cart-operation-ordinance.pdf"),
  publishes="St. Johns County publishes its golf cart rules for the unincorporated county. Here&rsquo;s a plain-English summary.",
  hub="Only designated county roads posted 25 mph or less, and designated multi-use paths.",
  answer="In unincorporated St. Johns County, golf carts may use only the county roads the County Engineer has designated (all posted 25 mph or less) "
         "and designated multi-use paths. Low-speed vehicles can use county roads posted 35 mph or less.",
  faq=dict(
   license="<p>The county&rsquo;s 2018 ordinance lets some unlicensed drivers ride, with hour limits (see the age question). "
           "Florida law changed in 2023: drivers under 18 now need a learner&rsquo;s permit or a driver&rsquo;s license, and drivers 18 and over need a government-issued photo ID.</p>",
   age="<p>The 2018 ordinance sets 14 as the minimum. Unlicensed drivers under 17 may not drive from 11 p.m. to 6 a.m., and unlicensed 17-year-olds not from 1 to 5 a.m. "
       "Florida&rsquo;s 2023 rule (a learner&rsquo;s permit or license under 18) also applies.</p>",
   permit="<p>We didn&rsquo;t find a cart registration in what we read. Roads are designated when a homeowners&rsquo; association applies, "
          "and the applicant pays for the signs.</p>",
   where="<p>Only <strong>Designated County Roads</strong>, which the County Engineer approves on an HOA&rsquo;s application and which must be posted "
         "<strong>25 mph or less</strong>, and sidewalks designated as <strong>multi-use paths</strong> (15 mph top speed; yield to people walking and cycling). "
         "Roads designated under the 2010 ordinance stay designated. Community-owned roads (district or private) can apply if they have a traffic enforcement agreement with the Sheriff.</p>"
         "<p>The ordinance doesn&rsquo;t list the designated roads.</p>",
   lsv="<p>Low-speed vehicles (LSVs) and mini trucks can use county roads posted 35 mph or less, unless the county has made a road a Prohibited County Road, "
       "and may cross a faster road at an intersection. LSVs must be registered, insured and equipped under state law.</p>",
   hours="<p>Sunrise to sunset, unless the county allows night use on that road and the cart has headlights, brake lights, turn signals and a windshield.</p>",
  ),
  extra=[],
  sources=[
   ("Ordinance 2018-42, golf carts, low-speed vehicles and mini trucks on county roads and sidewalks &mdash; St. Johns County (PDF copy hosted by Rivers Edge CDD)", "https://riversedgecdd.com/wp-content/uploads/2019/06/sjc-golf-cart-operation-ordinance.pdf"),
   ("Ordinance 2018-42 &mdash; St. Johns County Clerk&rsquo;s copy (PDF)", "https://stjohnsclerk.com/minrec/OrdinanceBooks/2018/ORD2018-42.pdf"),
   FL_316212, FL_3162122,
  ],
  street_map=None,
  slowgo="SlowGo plans routes on roads posted 35 mph and under. It doesn&rsquo;t know which St. Johns County roads are designated for carts, its 25 mph line, "
         "or its night rule, so a route can use roads a golf cart can&rsquo;t. Follow the signs, and ride in daylight.",
  prio="cart-friendly", prio_note="Fast-growing county with many cart communities",
  quality="high", source_type="county ordinance PDF (copy on Rivers Edge CDD site; clerk copy seen in search)", checked="2026-10-16",
  gap="Read the copy on a community district's site; the Clerk's copy was seen in search only. No list of designated roads. Applies to the unincorporated county only.",
  db_row=120,
 ),
]
