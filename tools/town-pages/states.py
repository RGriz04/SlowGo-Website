# State pages (scale-up, 2026-10-17): "Golf Cart Laws in [State]". Same schema as towns.py, plus
# kind="state", title, h1, eyebrow, hub_name. build.py adds a "Towns we've checked" list of the
# state's published town pages. Sources: legislature and state agency sites only.
#   Florida: F.S. 316.212, 316.2122, 316.2125, 320.01 (leg.state.fl.us), read 2026-10-15 (cart-towns row 40).
#   Georgia: the enacted bills on legis.ga.gov (HB 877 2014, SB 169 2015, HB 877 2020) + GA DPS,
#            per docs/research/georgia-cart-code-2026-10-16.md ("from enacted bills", not the compiled code).
#   Arizona: A.R.S. 28-101, 28-721, 28-966, 28-2153 (azleg.gov), cart-towns row 6.
#   New York: HELD for good (Ron 2026-10-17): never published, never linked, no /t/ link.

def _fl(sec, path):
    return (f"Florida Statutes &sect; {sec}",
            f"https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/{path}")


TOWNS = [
 dict(
  kind="state", slug="florida", name="Florida", st="FL", state="Florida", place="Florida",
  org="the State of Florida", Org="The State of Florida", publish=True, counted=True,
  title="Golf Cart Laws in Florida (Updated October 2026)", h1="Golf cart laws in Florida", eyebrow="State cart laws",
  hub_name="Golf cart laws in Florida", hub="The state rules every Florida town and county builds on.",
  official=("Florida Statutes &sect; 316.212", "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0316/Sections/0316.212.html"),
  publishes="Florida&rsquo;s golf cart and LSV rules are in state law, which the Florida Legislature publishes. Here&rsquo;s a plain-English summary.",
  answer="In Florida, golf carts can use only the public roads that a county or city has opened to them and signed. "
         "Low-speed vehicles (LSVs) are a separate class: they&rsquo;re titled, registered and insured, and can use streets posted 35 mph or less.",
  faq=dict(
   license="<p>Not always, for golf carts. Drivers under 18 need a learner&rsquo;s permit or a driver&rsquo;s license; drivers 18 and over need a "
           "government-issued photo ID. Many towns are stricter and require a driver&rsquo;s license. LSV drivers always need a valid driver&rsquo;s license.</p>",
   age="<p>Florida doesn&rsquo;t set a minimum age number for golf carts. Under 18, the driver needs a learner&rsquo;s permit or a driver&rsquo;s license; "
       "18 and over, a government-issued photo ID (&sect; 316.212(7)). A town can add its own rules.</p>",
   permit="<p>The state doesn&rsquo;t register golf carts. Many towns and counties run their own registration or decal, so check the local page. "
          "LSVs must be titled, registered and insured with the state.</p>",
   where="<p>Only on roads a <strong>county or city has designated</strong> for golf carts, after deciding carts can use them safely, and where it has "
         "posted signs. Without a designation, golf carts aren&rsquo;t allowed on public roads.</p>"
         "<ul><li>State highways: only to cross, where a designated road meets the highway and the state Department of Transportation has approved the crossing.</li>"
         "<li>State park roads posted 35 mph or less, where the park system allows it.</li>"
         "<li>Inside a self-contained retirement community, carts may be driven reasonably unless the county, city or state has prohibited it (&sect; 316.2125).</li></ul>"
         "<p>Local governments can be stricter than the state, and they can allow carts on sidewalks next to designated streets at 15 mph or less.</p>",
   lsv="<p>A <strong>golf cart</strong> is built for the golf course and can&rsquo;t go faster than 20 mph. A <strong>low-speed vehicle</strong> has four wheels "
       "and a top speed over 20 mph and up to 25 (&sect; 320.01).</p>"
       "<p>An LSV can use streets posted 35 mph or less, unless the county or city has closed a road to LSVs. An LSV can&rsquo;t travel along roads posted over 35; "
       "lawful crossings are separately regulated. It must be titled, registered and insured, with a licensed driver (&sect; 316.2122).</p>"
       "<p>The 35 mph rule is for LSVs only. It doesn&rsquo;t open any road to golf carts.</p>",
   hours="<p>Golf carts: sunrise to sunset. Night use is allowed only where the local government permits it and the cart has headlights, brake lights, "
         "turn signals and a windshield (&sect; 316.212(5)).</p>",
  ),
  extra=[
   ("Crossing roads",
    "<p>Golf carts may cross a state highway only where a designated county road or city street meets it and the state has approved the crossing. "
    "A cart may also cross a road in the middle of a block between two parts of a golf course, and cross streets in a mobile home park at approved points.</p>"),
   ("Equipment",
    "<p>Every golf cart on a road needs efficient brakes, reliable steering, safe tires, a rearview mirror, and red reflectors on the front and rear "
    "(&sect; 316.212(6)). Night use adds headlights, brake lights, turn signals and a windshield.</p>"),
  ],
  sources=[
   ("Florida Statutes &sect; 316.212 &mdash; golf carts on roads", "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0316/Sections/0316.212.html"),
   ("Florida Statutes &sect; 316.2122 &mdash; low-speed vehicles", "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0316/Sections/0316.2122.html"),
   ("Florida Statutes &sect; 316.2125 &mdash; golf carts in retirement communities", "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0316/Sections/0316.2125.html"),
   ("Florida Statutes &sect; 320.01 &mdash; definitions (golf cart, low-speed vehicle)", "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0320/Sections/0320.01.html"),
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know which roads each county or city has opened "
         "to golf carts yet, so a route can use a street that carts can&rsquo;t use. Check the town pages above before you ride.",
  prio="state", prio_note="State page: covers every Florida town, including towns without their own page", quality="high",
  source_type="state statute (leg.state.fl.us)", checked="2026-10-15",
  gap="316.2126 (golf carts and LSVs used by local governments and universities) is government use only, so it's not summarised. 320.01 definitions cited from the statute's known text (not re-fetched this run). FLHSMV's '30 mph' figure is not in the statute and is not used.",
  db_row=40,
 ),
 dict(
  kind="state", slug="georgia", name="Georgia", st="GA", state="Georgia", place="Georgia",
  org="the State of Georgia", Org="The State of Georgia", publish=True, counted=True,
  title="Golf Cart Laws in Georgia (Updated October 2026)", h1="Golf cart laws in Georgia", eyebrow="State cart laws",
  hub_name="Golf cart laws in Georgia", hub="The state rules: carts are PTVs, and towns decide which streets they can use.",
  official=("Georgia HB 877 (2014), as enacted", "https://www.legis.ga.gov/api/legislation/document/20132014/144917"),
  publishes="Georgia&rsquo;s golf cart and LSV rules are in state law, which the Georgia General Assembly publishes. Here&rsquo;s a plain-English summary.",
  answer="In Georgia, a street cart usually counts as a personal transportation vehicle (PTV), and it can use only the streets and paths "
         "a city or county has designated for it. Low-speed vehicles (LSVs) are a separate, registered class that can use roads posted 35 mph or less.",
  faq=dict(
   license="<p>Usually. A PTV driver needs a valid driver&rsquo;s license, unless the town&rsquo;s cart ordinance allowed unlicensed drivers before 2012. "
           "No license is needed on a PTV-only path or at a designated crossing where the town allows unlicensed drivers. LSVs are motor vehicles: "
           "the state&rsquo;s Department of Public Safety says they need a licensed driver.</p>",
   age="<p>State law doesn&rsquo;t set an age for PTVs; each town&rsquo;s ordinance does. Many towns say 16 with a license.</p>",
   permit="<p>There&rsquo;s no state registration or title for PTVs. A town may register them, at least every five years, for up to $15. "
          "LSVs are registered and insured with the state.</p>",
   where="<p>Only on streets and paths a <strong>city or county has designated by ordinance</strong>. Without that, a PTV has no place on a public road. "
         "The ordinance takes effect once the town posts warning signs where state highways enter it.</p>"
         "<p>Towns that set PTV rules after 2011 must keep shared streets at <strong>25 mph or less</strong>. Towns with a cart ordinance from before 2012 "
         "aren&rsquo;t bound by that limit; their own ordinance decides. (That&rsquo;s our reading of the law, not legal advice.)</p>",
   lsv="<p>Georgia has three kinds of small vehicle:</p>"
       "<ul><li>a <strong>golf car</strong> is for playing golf and averages under 15 mph; it has no street rules of its own;</li>"
       "<li>a <strong>PTV</strong> (the main modern category) has at least four wheels, a top speed under 20 mph, weighs no more than 1,375 lb empty and seats up to eight; "
       "this is what town cart rules cover. An older category covers carts with three or more wheels, up to 1,300 lb and 20 mph, that a town approved before 2012;</li>"
       "<li>an <strong>LSV</strong> has four wheels and a top speed over 20 mph and up to 25, built or converted to the federal LSV standard.</li></ul>"
       "<p>LSVs can use roads posted 35 mph or less. An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   hours="<p>The state sets no hours for PTVs; towns may. PTVs need head lamps and tail lamps, except daylight-only carts under a pre-2012 ordinance.</p>",
  ),
  extra=[
   ("Crossing roads",
    "<p>A PTV may cross a state highway only at a crossing the state Department of Transportation has designated, built as an active crossing and marked "
    "with the golf cart crossing sign. On city and county roads, it may cross only where the town or county has designated a crossing.</p>"),
   ("Equipment",
    "<p>PTVs need brakes with a parking brake, a reverse warning, a main power switch, head lamps, reflectors, tail lamps, a horn, a rearview mirror, "
    "safety labels, and hip restraints or hand holds.</p>"),
   ("How we read Georgia&rsquo;s law",
    "<p>We read these rules from the bills as the General Assembly passed them (2014, 2015 and 2020) on its own website, not from the compiled code.</p>"),
  ],
  sources=[
   ("Georgia HB 877 (2014), the enacted bill that set the state&rsquo;s cart (PTV) rules &mdash; Georgia General Assembly", "https://www.legis.ga.gov/api/legislation/document/20132014/144917"),
   ("Georgia SB 169 (2015), as enacted &mdash; Georgia General Assembly", "https://www.legis.ga.gov/api/legislation/document/20152016/154037"),
   ("Georgia HB 877 (2020), the enacted bill that rewrote the LSV definition &mdash; Georgia General Assembly", "https://www.legis.ga.gov/api/legislation/document/20192020/194849"),
   ("Georgia Code: low-speed vehicles &mdash; Georgia Department of Public Safety", "https://dps.georgia.gov/georgia-code-low-speed-vehicles"),
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know which streets each town has designated for carts, "
         "its 25 mph lines, or which crossings are signed for carts, so a route can use a road or crossing that carts can&rsquo;t. Check the town pages above before you ride.",
  prio="state", prio_note="State page: covers every Georgia town", quality="high",
  source_type="state legislature (enacted bills on legis.ga.gov) + GA DPS", checked="2026-10-15",
  gap="Read from enacted bills, not the compiled O.C.G.A. (LexisNexis, off-limits); stated on the page. The pre-2012 / 25 mph reading is an interpretation (labelled on the page). LSV license/registration rest on GA DPS, not re-read statute. 'Many towns say 16 with a license' summarises the town rows (St. Simons, Tybee, Port Wentworth, Jekyll).",
  db_row=134,
 ),
 dict(
  kind="state", slug="arizona", name="Arizona", st="AZ", state="Arizona", place="Arizona",
  org="the State of Arizona", Org="The State of Arizona", publish=True, counted=True,
  title="Golf Cart Laws in Arizona (Updated October 2026)", h1="Golf cart laws in Arizona", eyebrow="State cart laws",
  hub_name="Golf cart laws in Arizona", hub="No statewide cart road law: road carts need MVD registration. NEVs (low-speed vehicles) can&rsquo;t travel along roads posted over 35.",
  official=("Arizona Revised Statutes &sect; 28-101", "https://www.azleg.gov/ars/28/00101.htm"),
  publishes="Arizona&rsquo;s golf cart and NEV rules are in state law, which the Arizona Legislature publishes. Here&rsquo;s a plain-English summary.",
  answer="Arizona has no statewide law that opens roads to golf carts. A golf cart driven on public roads is treated as a motor vehicle, "
         "so it needs MVD registration and insurance. Neighborhood electric vehicles (NEVs), a separate class, can use roads posted 35 mph or less.",
  faq=dict(
   license="<p>Yes, on public roads. A golf cart used on the road is a motor vehicle under Arizona law, so the usual driver&rsquo;s license rules apply.</p>",
   age="<p>The statutes we read set no cart-specific age. The normal driver&rsquo;s license rules apply.</p>",
   permit="<p>Yes, for road use. A golf cart is exempt from registration only when it&rsquo;s used on a golf course or is only incidentally on a highway "
          "(&sect; 28-2153). Regular street use means MVD registration and liability insurance.</p>",
   where="<p>Arizona has <strong>no statewide golf cart road rule</strong> and no scheme for towns to designate cart streets. A registered, insured cart "
         "follows the normal road rules. Some towns publish their own guidance.</p>"
         "<p>One special rule: in an age-restricted community in an unincorporated area of a county with more than three million people, a cart or NEV may "
         "use the paved shoulder, or keep as close as it can to the right edge where there&rsquo;s no shoulder (&sect; 28-721). That rule is about where on the "
         "road to drive. It doesn&rsquo;t open any road to carts, and it doesn&rsquo;t let an NEV travel along a road posted over 35 mph.</p>",
   lsv="<p>Arizona defines a <strong>golf cart</strong> as a vehicle designed to be driven at no more than 25 mph, under 1,800 lb, carrying four people "
       "or fewer (&sect; 28-101).</p>"
       "<p>Arizona&rsquo;s street-legal low-speed vehicle is the <strong>neighborhood electric vehicle</strong> (NEV): electric, emission-free and built to "
       "the federal LSV standard. An NEV tops out at 25 mph and must carry a notice of its limits. Under &sect; 28-966, an NEV "
       "can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated. We didn&rsquo;t find a road rule for gas-powered LSVs.</p>",
   hours="<p>The statutes we read set no hours or lights list just for golf carts.</p>",
  ),
  extra=[
   ("Crossing roads",
    "<p>&sect; 28-966 says its 35 mph limit doesn&rsquo;t stop an NEV from crossing a road posted over 35 at an intersection. We didn&rsquo;t find a separate crossing rule for golf carts.</p>"),
  ],
  sources=[
   ("Arizona Revised Statutes &sect; 28-101 &mdash; definitions (golf cart, neighborhood electric vehicle)", "https://www.azleg.gov/ars/28/00101.htm"),
   ("Arizona Revised Statutes &sect; 28-721 &mdash; driving on the right; shoulder use in age-restricted communities", "https://www.azleg.gov/ars/28/00721.htm"),
   ("Arizona Revised Statutes &sect; 28-966 &mdash; neighborhood electric vehicles", "https://www.azleg.gov/ars/28/00966.htm"),
   ("Arizona Revised Statutes &sect; 28-2153 &mdash; registration exemptions", "https://www.azleg.gov/ars/28/02153.htm"),
  ],
  street_map=None,
  slowgo="It doesn&rsquo;t know local cart rules or community roads&rsquo; "
         "own rules, and it doesn&rsquo;t check whether your cart is registered for the road. Check local rules before you ride.",
  prio="state", prio_note="State page: covers Arizona's retirement communities (Sun City, Green Valley, SaddleBrooke...)", quality="high",
  source_type="state statute (azleg.gov)", checked="2026-10-15",
  gap="A3 (2026-10-16): 28-721(C) and 28-966 re-read on azleg.gov. 28-721(C) is shoulder placement only; 28-966(B) still bars NEVs from roads posted over 35 (crossing at intersections allowed); the 45 mph exception in 28-966(D)-(E) is for neighborhood OCCUPANTLESS electric vehicles only. Named examples (Sun City, Sun City West) removed: whether they are 'age restricted communities' under the statute is our interpretation. Gas LSVs: no rule found. Insurance limits (25/50/15) left off the page.",
  db_row=6,
 ),
 dict(
  kind="state", slug="new-york", name="New York", st="NY", state="New York", place="New York",
  org="the State of New York", Org="The State of New York", publish=False, counted=False, never_publish=True,
  held_note="\n<!-- HELD: Ron ruling 2026-10-17, never name New York in public copy. Never published: noindex, not in the hub or sitemap, no /t/ link, linked from no other page. -->",
  title="Golf Cart Laws in New York (Updated October 2026)", h1="Golf cart laws in New York", eyebrow="State cart laws",
  hub_name="Golf cart laws in New York", hub="",
  official=("Vehicle and Traffic Law &sect; 2262", "https://www.nysenate.gov/legislation/laws/VAT/2262"),
  publishes="New York&rsquo;s low-speed vehicle rules are in state law, which the State Senate publishes online. Here&rsquo;s a plain-English summary.",
  answer="Golf carts can&rsquo;t be registered or driven on public streets in New York. Low-speed vehicles (LSVs) that meet the federal standard "
         "can be registered and driven on roads posted 35 mph or less.",
  faq=dict(
   license="<p>Golf carts can&rsquo;t be driven on public streets at all. LSVs are registered vehicles, so the normal driver&rsquo;s license rules apply.</p>",
   age="<p>Golf carts aren&rsquo;t allowed on public streets. To register an LSV, the applicant must be at least 16 (&sect; 2261).</p>",
   permit="<p>A golf cart can&rsquo;t be registered, so it can&rsquo;t be used on public roads. An LSV must be registered (&sect; 2261), and it must pass "
          "inspection and be insured (&sect; 2265).</p>",
   where="<p>Golf carts: not on streets, highways, parking lots or sidewalks open to public traffic, according to the state Department of Motor Vehicles. "
         "No state law authorizes them.</p>"
         "<p>LSVs: public roads posted <strong>35 mph or less</strong>, except roads a local authority or the state Department of Transportation has closed "
         "to LSVs (&sect; 2262). An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   lsv="<p>An LSV is a limited-use vehicle with a top speed over 20 mph and up to 25 that meets the federal LSV standard (&sect; 121-f). To be registered, it "
       "must have a speed certified by the maker and appear on the state&rsquo;s list of approved limited-use vehicles. "
       "An LSV can&rsquo;t travel along roads posted over 35; lawful crossings are separately regulated.</p>",
   hours="<p>We didn&rsquo;t find separate hours for LSVs in the sections we read.</p>",
  ),
  extra=[
   ("Crossing roads",
    "<p>An LSV may cross a road posted over 35 mph where it meets a road posted 35 mph or less (&sect; 2262).</p>"),
  ],
  sources=[
   ("Vehicle and Traffic Law &sect; 2262 &mdash; LSV operation", "https://www.nysenate.gov/legislation/laws/VAT/2262"),
   ("Vehicle and Traffic Law &sect; 121-f &mdash; LSV definition", "https://www.nysenate.gov/legislation/laws/VAT/121-F"),
   ("Vehicle and Traffic Law &sect; 2261 &mdash; LSV registration", "https://www.nysenate.gov/legislation/laws/VAT/2261"),
   ("Vehicle and Traffic Law &sect; 2265 &mdash; LSV inspection and insurance", "https://www.nysenate.gov/legislation/laws/VAT/2265"),
   ("Electric scooters, bicycles and other unregistered vehicles &mdash; state Department of Motor Vehicles", "https://dmv.ny.gov/registration/electric-scooters-and-bicycles-and-other-unregistered-vehicles"),
  ],
  street_map=None,
  slowgo_full=True,
  slowgo="SlowGo doesn&rsquo;t start turn-by-turn routes in this state yet. It doesn&rsquo;t know which roads local authorities have closed to LSVs.",
  prio="state", prio_note="HELD: Ron ruling 2026-10-17, never name New York in public copy", quality="high",
  source_type="state statute (nysenate.gov) + DMV page", checked="2026-10-05 (statute); 2026-10-16 (DMV page)",
  gap="HELD: Ron ruling 2026-10-17, never name New York in public copy. Draft only: noindex, not in hub or sitemap, no /t/ link, linked from no page.",
  db_row=None,
 ),
]
