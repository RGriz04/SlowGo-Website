# SlowGo Privacy Policy

**Last updated: October 16, 2026** *(DRAFT, not live: re-date to the publication day)*

**What changed (October 16, 2026):** We checked this Policy against what each version of the App actually sends, and corrected it where it said too little or claimed too much. In short: on iPhone, crash reports and product metrics carry a device identifier, so they are not anonymous (Section 4); version 1.3 sends sample points along the off-path parts of a route to the Overpass service, and every version sends a place's coordinates there when you open its card or arrive at it (Section 3); tapping the map sends that point to Stadia Maps (Section 3); we now name our infrastructure providers by category, and some providers operate outside the United States (Sections 3 and 9); the Site's business inquiry forms are described (Section 3); and changes that arrive with version 1.5 are marked where they apply.

This Privacy Policy describes how **BackRoad Apps LLC** ("**BackRoad Apps**," "**we**," "**us**," or "**our**") handles information in connection with the SlowGo mobile application (the "**App**") and the slowgoapp.com website (the "**Site**") (together, the "**Service**"). Where versions of the App behave differently, this Policy says which version does what. You can see your version in the App's Settings.

**The short version:** SlowGo uses your location to do its job — showing where you are, suggesting routes, finding places, and checking your local weather — and sends what each request needs to the services listed in Section 3. Your saved ride history stays on your phone. We don't require accounts, we don't sell your information, and we don't show ads. Crash reports and a few product metrics go to our crash-reporting provider; on iPhone they carry a device identifier (Section 4).

## 1. Information We Collect

**We do not require an account.** The App does not ask for your name, email address, phone number, or any login.

**Precise location.** With your permission (through your device's location prompt), the App collects your device's precise location while you use it, to show your position on the map, calculate and display routes, search for nearby places, and provide local weather. **Location continues during a ride you start, including on the lock screen and in the background.** During a ride you have started, the App keeps reading your position while your phone is locked or the App is in the background, so guidance continues; on Android, a notification is shown for as long as this happens. This stops when the ride ends. When you request a route or search, the relevant coordinates are transmitted to the providers that fulfill the request (see Section 3). Opening the ride postcard also looks up the general area a ride started and ended in, so the card can name those places; that lookup sends only an approximate position — rounded to about 110 metres — and never your exact start or end point. Your phone's operating system works out your position; Apple or Google handles that under its own privacy policy. You can withdraw location permission at any time in your device settings; core features of a navigation app will not work without it.

**Ride, favorite, and settings data (stored on your device).** The App stores your ride history, favorite places, recent destinations, and settings on your device. See Section 5 for details and controls.

**Diagnostics and reliability data.** If the App crashes or encounters an error, a diagnostic report may be generated so we can find and fix the problem. Before a report raised by the App's own code is sent, the App removes location coordinates and other trip-revealing fields (see Section 4). We also collect a small, fixed set of coordinate-free product metrics, such as whether a route request was served, how a reroute turned out, which quick-link category was tapped, and how many map tiles a session loaded. Reports and metrics include technical details about your phone and, on iPhone, a device identifier. Section 4 lists all of it.

**Device and technical information.** Providers that serve the App's requests (Section 3) receive standard technical information necessary to respond, such as your IP address and basic device and app information. Our Site is a largely static website; our hosting provider may process standard server logs (such as IP address and browser type) to operate and secure the Site.

**Information you send us.** If you email hello@slowgoapp.com, we receive your email address, any name in your email, and the contents of your message, which we use to respond and to improve the Service. If you email us to opt out of arbitration under the Terms of Service, we keep that message as a record of your choice (Section 6).

**Information you give us through the Site's forms.** The Site has a waitlist form, which asks for your email address; a town-request form, which asks for your email address and the name of a town or community; and business inquiry forms, described in Section 3 under "Business inquiries." All are optional, and none is part of the App. Section 3 describes what happens to what you submit.

**Your acceptance of the Terms.** When you agree to the Terms of Service in the App, the App saves a record on your phone: which versions you agreed to, when, the App and operating-system versions, your language setting, and a random acceptance identifier. It stays on your phone and is not sent to us, unless you choose to include the identifier in an email to us.

**We do not collect** contacts, photos or videos, microphone audio, health data, biometric data, advertising identifiers, or location in the background other than during a ride you have started.

## 2. How We Use Information; Notice at Collection

We use information to: provide the Service (position, routing, place search, weather); operate the App's safety-related display features (for example, identifying higher-speed segments of a route); diagnose and fix crashes and reliability problems; understand, in aggregate, how the App is used (for example, roughly how many phones use it each week and in which cities); secure and operate the Service; respond to your messages and business inquiries; write to you about the launch and plan where to build coverage next, if you asked us to through a Site form; keep records of legal choices such as arbitration opt-outs; and comply with law. The categories we process, the purposes, and our retention approach are described in this Policy and, for location and diagnostics, are surfaced in the App at the point of collection. We do **not** use your information for advertising, and we do not build advertising or tracking profiles of you.

## 3. Where Your Information Goes

To fulfill your requests, the Service sends your coordinates and related request data to the services that do the work:

| Provider | What it does | What it receives |
|---|---|---|
| BackRoad Apps servers (operated by us, on rented cloud servers) | Calculates cart-friendly routes and looks up the posted speed limits along a route it has calculated. From version 1.5, also answers nearby-place searches (the quick links, Loops and stop pickers) and relays weather requests to the National Weather Service | Trip start/end coordinates, route requests, and the shape of a calculated route. From version 1.5: for nearby-place searches, the kind of place and your position rounded to about 1 kilometre; for weather, your position rounded to about 1 kilometre, including about every 10 minutes during a ride so the App can warn you about storms |
| Stadia Maps | Map tiles and styles, place search (geocoding), naming a point you tap on the map, and neighborhood names for the ride postcard | The map area you are viewing (as the map follows you during a ride, this traces the areas you pass through); your search text along with a nearby coordinate (your position, your chosen start, or the map's center) so results can be ranked by distance; the exact point when you tap the map or drop a pin; and, when you open a ride postcard, the approximate trip start/end areas (rounded to about 110 metres) |
| OpenStreetMap community services (public Overpass servers, run by volunteer organizations in Germany and Austria) | Place details such as opening hours and phone number. Before version 1.5, also nearby-place search. In version 1.3, also checking whether paths on a route are marked for carts | The exact coordinates of a place when you open its card, and of your destination when you arrive, so the App can show its hours. Before version 1.5: the search area around your position, chosen start, or map view, for nearby-place search. Version 1.3 only: up to 14 sample points along the parts of a route that use paths rather than roads, when a route with such parts is planned or re-planned |
| U.S. National Weather Service | Local weather, forecasts, and (from version 1.5) storm warnings | Your position rounded to about 1 kilometre. Before version 1.5, the App sends it directly, so the Weather Service also receives your IP address. From version 1.5, it comes from our server, never from your phone, so the Weather Service doesn't receive your IP address |
| Sentry | Crash and error reporting, and a small set of coordinate-free product metrics | Diagnostics and product metrics as described in Section 4, including technical details about your phone, your IP address (which Sentry uses to estimate a city and does not store), and on iPhone a device identifier |
| Netlify | Hosts the Site and receives what you submit through its forms; also answers the App's connectivity check, a request with no content about once a minute while the App is running, so the App can tell whether you're online. When you open a SlowGo link such as slowgoapp.com/go or /card, the Site counts the visit by link and day (totals only) and sends you on to the right store; it doesn't keep your IP address or anything about your device in that count. | What you type into a Site form; plus standard server logs such as IP address and browser type. For the connectivity check: your IP address and basic device and app information — no location, no identifiers, nothing you type |
| Apple | App distribution, and payment processing if paid features are offered | Per Apple's own terms and privacy policy |
| Google | App distribution on Android (Google Play) | Per Google's own terms and privacy policy |

**Infrastructure we use.** Besides the providers named above, we rely on these kinds of companies to run the Service. A **cloud hosting provider** in the United States runs the rented servers our routing, place-search and weather relay software runs on; its systems carry and store that traffic, and it may keep its own network and security records, but we do not send it your requests for its own use. Our **email provider** stores email you send to hello@slowgoapp.com and the notifications we receive when someone submits a Site form. Our **domain name and website host** is Netlify (above). Site pages load their fonts from the Site itself.

**When you share or open something elsewhere.** Some things leave the App because you ask them to. What you send through your device's own share sheet goes to whichever app you pick there — Messages, Mail, a notes app, anything installed — and from that point it is handled by that app and its provider, not by us. We do not receive a copy and we do not keep a record of what you shared or who you sent it to.

- **Sharing a place** sends the place's name and a standard map link containing its exact coordinates, so the person receiving it can open it in a maps app.
- **Sharing a ride postcard** sends the picture: your ride's stats, the general areas it started and ended in, and any note you wrote. It does not include a map, the shape of your route, or your exact start or end point.
- **Sharing your savings summary** sends a few lines of text about totals. It contains no locations at all.
- **Walking directions to where you parked** (version 1.5) opens your phone's Maps app (Apple Maps or Google Maps) with the parked spot as the destination; Apple or Google then handles it under its own privacy policy.
- **Website, Menu, and Photos & reviews on a place card** (version 1.5) open only when you tap them. Website and Menu open the place's own site in your phone's built-in browser window, which receives an ordinary visit from your phone. Photos & reviews opens Google Maps or Yelp, whichever you pick, searching for the place's name and street address; the App adds no location of yours. Once the other site or app is open, its own privacy policy applies.

**Routing stays with us.** Route calculations and speed-limit checks are performed on our own servers. No third party receives your route request — your origin and destination are sent for routing only to our own routing server. From version 1.4, checking whether paths along a route are marked for carts happens on your device, using a list built into the App from our own copy of the map, and no points along your route are sent to anyone for it; version 1.3 sends sample points from the path portions of a route to the Overpass service, as the table above says. Other features send single points as the table describes: a place's coordinates (including your destination's, when you arrive) to the Overpass service, the point you tap on the map to Stadia Maps, and a nearby coordinate with place searches. The App previously used outside routing services as a backup when our own server could not be reached; it no longer does.

These providers process requests to deliver the Service under their own terms or public usage policies, and our agreements with them where they exist. The Overpass servers and the National Weather Service are public services we have no contract with. **We do not maintain user accounts and do not intentionally build a persistent, account-linked history of where you go.** Our servers process requests to answer them; our access and security logs are configured not to record route coordinates. Providers may retain request and security logs under their own policies, including where reasonably necessary for security, fraud prevention, legal compliance, or backups.

We may also disclose information if required by law, to protect the rights, safety, or property of BackRoad Apps or others, or in connection with a merger, acquisition, or sale of assets (in which case this Policy will continue to apply to previously collected information unless you are notified otherwise).

**We do not sell your personal information, and we do not share it for cross-context behavioral advertising.**

### The Site's waitlist and town-request forms

The **waitlist** form collects your email address. The **town-request** form collects your email address and the name of a town or community. Nothing else is asked for, and the App never uses these forms.

We use what you submit for one purpose each: to write to you when SlowGo is available where you ride, and to decide which areas to build coverage for next. Submissions are handled by **Netlify**, which hosts the Site and stores form entries for us as a service provider, and a copy reaches our email provider as a notification.

**We do not sell this information, we do not share it for advertising, and we do not use it for marketing beyond the purpose you submitted it for.** You will not receive a newsletter, a drip campaign, or promotions from us.

We keep a submission until we have sent the launch notification for your area, or until you ask us to delete it, whichever comes first. To have your entry removed at any time, email hello@slowgoapp.com from the address you submitted, or tell us the address you used, and we will delete it.

### Business inquiries

The Site's page for businesses (slowgoapp.com/business) has inquiry forms for rental shops, dealers, communities, towns, tourism boards, and other organizations. They ask for your **business or organization name, a contact email, the town you serve, and your inquiry**. You may also give a **contact name, a phone number, and a rough fleet size** (a range, not an exact count); these are optional. Please don't include renters' personal information or any payment details.

We use what you send to answer your inquiry and to discuss whether SlowGo can work for your business. We don't add you to a mailing list or send you promotions unless you separately ask us to, and we do not sell this information or share it for advertising. An inquiry is not an agreement to anything. Submissions are stored by **Netlify**, our website host, as our service provider, and a copy reaches our email provider as a notification. If a public body sends us an inquiry, it may be subject to public-records laws we don't control.

We delete an inquiry, and our emails about it, **12 months after our last exchange with you** if nothing further has come of it, or sooner if you ask. If your business goes on to work with us, the details needed for that relationship are kept for as long as it lasts and for up to 12 months after it ends, apart from records the law requires us to keep longer (such as tax records). To have your inquiry deleted, email hello@slowgoapp.com.

## 4. Crash and Error Reports, and Product Metrics

If SlowGo crashes or hits an error, a diagnostic report may be sent to our crash-reporting provider (Sentry) so we can fix the problem. Crash-reporting tools can otherwise capture sensitive context, so the App is configured to keep location out of them in three separate ways.

**Reports raised by the App's own code** pass through a filter before they leave the device. That filter works from a list of fields it is allowed to send — anything it does not recognise is dropped rather than forwarded — and it removes latitude and longitude, addresses, route endpoints, search text, and request bodies, URLs, or breadcrumbs that could reveal a trip or destination. Values that look like coordinates are removed outright, not blurred or rounded.

**Reports raised by a crash in the device's own layer** — including, on Android, reports that the App stopped responding, and on iPhone, reports that the App froze or was shut down by the system — are assembled by the crash reporter itself and do not pass through that filter. They contain no location from your device because there is none for them to find: the App never gives the crash reporter your position, your route, or any place data, and we switch off the reporter's own capture of network requests, which is the other way a coordinate could reach it.

**What a report contains.** Besides the error itself, every report and metric includes technical details about your phone and the App: the App version, device model, operating-system version, language setting, screen size, memory and storage, battery level and charging state, orientation, connection type and, on Android, time zone and the App's permissions. It also includes a short trail of recent App events (up to 20 "breadcrumbs"): for example, which screen was showing, that a button or text field was touched (never what you typed), the App moving to the background, connectivity changes, and earlier metrics. We switch off session tracking, screenshots, screen recordings, and performance tracing.

**Identifiers — reports are not anonymous.** There is no account, and the App does not attach your name, an email address, or an advertising identifier to any report. But on iPhone, Sentry's software adds a **device identifier** to every report and metric. It is computed from the identifier Apple gives each developer for your phone, together with the phone's model and the App's ID. It stays the same when the App restarts or updates, and changes only if you delete the App and install it again. It lets us and Sentry tell that several reports came from the same phone; we use it to find problems that keep affecting one phone and to estimate roughly how many phones use SlowGo each week. In rare cases on iPhone (when the system shuts the App down without warning), a report can also carry a random installation number that Sentry keeps in the App's cache folder; it is deleted when you delete the App. On Android, the App removes Sentry's installation identifier, any user field, and the device's boot time from every report before it is sent, including native crash and "stopped responding" reports, so Android reports carry no persistent identifier.

**Location estimated from your IP address.** Our crash-reporting provider uses your connection's IP address to estimate the city and state a report came from, and we count reports by city to see where SlowGo is used; that estimate is never more precise than a city, and we configure the provider not to store the IP address itself. We also configure it to minimize default data collection and to restrict retention and access. Crash reports are about the App's health, not about where you went.

**The product metrics**, listed here rather than described in general terms:

- whether a route request was served or not (from version 1.5, also whether it was asked for on the phone or on a car screen);
- when a ride leaves its route, whether the replacement route was accepted, refused for its speed limits, could not be checked, or could not be fetched (from version 1.5, also whether that was because the phone had no connection, our routing service didn't answer in time, or it answered with an error, and which attempt it was), and roughly how long that took;
- which quick-link category (for example "Coffee" or "Pharmacy") was tapped;
- how many map tiles a session loaded;
- that the map's display stopped working and had to restart, and a fixed reason;
- on iPhone, that you finished sharing a ride postcard — a count only, never the postcard, what it says, where the ride went, or who or which app you sent it to;
- from version 1.5, when a ride you started ends: how it ended (arrived, ended near the destination, ended early, or left unfinished), what kind of ride it was (a route, a loop, or a ride with stops), its length in one of four broad bands, and whether it was rerouted — no destination, place, time of day, or distance.

When SlowGo is connected to a car display (CarPlay on iPhone), the App also records that the connection started and ended, whether the car's start screen and map screen appeared and roughly how long they took, and the car screen's size. Some of these are recorded only on a sample of phones.

Each metric is a fixed category or a number — there are no coordinates, no addresses and no text you typed in any of them, and they pass through the same removal step described above, alongside the device details and identifier described in this Section. We use them to tell whether routing and the car display are working, to keep our map-tile usage within budget, to see whether features such as postcards are worth keeping, and to estimate how many phones use the App.

## 5. What Stays on Your Phone

**Your saved ride history stays on your phone.** SlowGo keeps your most recent rides (up to 100) in the App's storage on your device, and stores their start and end points at reduced precision: rounded to four decimal places, which is a grid of roughly 11 metres. That is coarser than the reading your device produces, and it is what the App keeps rather than the exact point, but it can still be precise enough to point to a single home. Favorites are stored at full precision so they take you exactly where you saved. (Separately, when you actually request a route, that route's start and end coordinates are transmitted to providers to calculate it, as described in Section 3 — this is different from the on-device history.)

**Your most recent position is also saved on your phone.** So the map can open where you left off instead of a blank screen while your first GPS reading arrives, the App keeps your **single most recent location reading at full precision**, along with what produced it (a live reading or the position your device had already cached), when it was taken, and how accurate it was. It is a single point, not a trail: each new reading overwrites the previous one, and no history of these readings is kept. It stays on your device until you delete the App. This is the most precise location the App keeps on your phone, which is why we name it here specifically.

**An in-progress ride is saved so you can resume it.** When you start navigating, the App saves that ride's **destination at full precision** (with its label), where the ride started, the shape of the route itself (rounded to roughly 11 metres), the custom starting point if you set one, and the time you started, so that if the App is closed or crashes mid-ride it can offer to pick the trip back up. The route's shape is what lets the App tell that you are still somewhere on the trip, rather than only whether you are near its destination. It is cleared as soon as you arrive, when you end the ride, when you decline the offer to resume, and automatically if it is more than 90 minutes old or you are no longer on the trip when the App next opens.

**Where you parked (version 1.5).** When a ride ends, SlowGo keeps the spot where your cart stopped, on your phone only, so "Where'd I park?" can show it to you. It's kept only when your phone has a precise location reading (to within about 30 metres); otherwise nothing is kept. It is never sent to us or anyone else, unless you tap **Walking directions** (Section 3). It's replaced the next time a ride ends, and deleted after 7 days or when you tap "I've got my cart."

**The map's last position is saved.** The App separately stores **where the map was last looking** — a center point and zoom level — so re-opening the App restores your view instead of jumping. This is a map view, not a record of where you were; you can pan the map anywhere without going there. It is overwritten as you move the map and stays on your device until you delete the App.

**The lock screen (version 1.5).** During a ride, the App can show your next turn and where you're going on the lock screen, where anyone holding your phone can read them. You can turn this off in Settings ("Show turns on the lock screen").

**Your controls:** you can turn ride saving off ("Save ride history" in Settings), and you can delete all saved rides at any time ("Clear ride history" in Settings); turning saving off stops new rides being saved but does not erase rides already saved. Turning off the App's location permission stops new position readings from being taken or saved. Deleting the App removes its storage from your phone, including the items above — which, apart from the in-progress ride and the parked spot clearing themselves as described, is how they are removed. On iPhone, "offloading" the App (rather than deleting it) keeps its data on the phone until you reinstall or delete it.

**Device protections and backups:** on-device data is stored using your phone's standard app storage and is protected by your device's own protections (such as your passcode and the operating system's safeguards). We do not separately encrypt this data beyond the protections your device provides. The App marks its storage to be left out of iCloud and computer backups on iPhone, and out of Google backups and transfers to a new phone on Android. A backup tool you choose, or a copy made by other software on your phone, may behave differently, and deleting the App does not reach into backups or copies that already exist; use that tool's own controls to delete them.

## 6. Data Retention

Ride history, favorites, recents, the parked spot, your Terms acceptance record, and settings remain on your device until you delete them or delete the App (the parked spot is deleted after 7 days, or sooner as described in Section 5). For information we or our infrastructure process: our servers' access and security logs are retained no more than 14 days and are configured not to include route coordinates; crash reports and product metrics are retained by Sentry for no more than 90 days (currently about 30 days); emails you send us are retained approximately 24 months, or longer if needed for a legal matter; arbitration opt-out messages are kept for as long as we offer the App and 7 years after, because an opt-out can matter in any later dispute; waitlist and town-request submissions are kept until the launch notification for that area has been sent or you ask us to delete them, whichever comes first; business inquiries are kept as described in Section 3; and routine Site server logs are retained approximately 30 days. If we introduce paid features, transaction and tax records may be retained up to 7 years as required by law. Third-party providers retain request data under their own policies. We may keep information longer only where the law requires it, or to deal with an actual or reasonably expected legal claim, and only for as long as that lasts.

## 7. Security

Requests between the App and service providers are transmitted using industry-standard encryption in transit (HTTPS/TLS). On-device data is protected by your device's safeguards as described in Section 5. No method of transmission or storage is completely secure, and we cannot guarantee absolute security.

## 8. Your Choices

- **Location:** manage the App's location permission in your device settings.
- **Ride history:** toggle saving off, or clear it, in the App's Settings.
- **Lock screen (version 1.5):** turn off "Show turns on the lock screen" in Settings.
- **Crash reporting and reliability data:** these are limited and configured to exclude trip data; deleting the App stops all collection. On iPhone, deleting and reinstalling the App changes the device identifier described in Section 4.
- **Waitlist, town requests, and business inquiries:** email hello@slowgoapp.com to have your submission deleted.
- **Do Not Track / Global Privacy Control:** the Service does not track you across other companies' apps or websites, so there is nothing for these signals to opt out of.

## 9. Your Privacy Rights

### United States state privacy rights

Depending on where you live (for example, California, Colorado, Connecticut, Texas, Utah, Virginia, and other states with comprehensive privacy laws), you may have rights to know, access, correct, delete, or obtain a copy of personal information, to opt out of sale, sharing, or targeted advertising, and to withdraw consent to processing of sensitive data such as precise location. **Our practices make most of this simple:** we do not sell or share personal information for advertising, we do not profile you, and precise location is used only to provide the Service. Your rides, favorites, and settings stay on your device under your direct control — you can access them in the App and delete them yourself at any time (Section 5). Other information is held by us or our providers: crash reports and metrics (Section 4), the emails you send us, and anything you submit through a Site form. Crash reports aren't tied to a name or account, so we usually can't find the ones from your phone; we will tell you if that's the case.

For anything else — including questions, or access or deletion requests concerning emails you have sent us or anything you submitted through a Site form — contact us at hello@slowgoapp.com and tell us the state where you reside. We will verify and respond as required by applicable law, asking only for what we need to verify your request, we will not discriminate against you for exercising your rights, and if we deny a request you may appeal by replying to our response. You may use an authorized agent where applicable law allows.

**California notice:** in the preceding 12 months, we have collected the categories described in Section 1 (identifiers such as IP address and, on iPhone, a device identifier, and the contact details you may submit through a Site form; precise geolocation; internet/electronic activity and diagnostic information; and communications you send us), for the purposes in Section 2, disclosed to the service providers in Section 3, and retained per Section 6. We do not sell or share personal information as those terms are defined by California law, and we have no actual knowledge of selling or sharing personal information of consumers under 16. California residents may exercise the rights described above.

### Outside the United States

The Service is intended for use in the United States. Most information is processed in the United States, but some providers process requests elsewhere: for example, the public Overpass servers are in Germany and Austria. If you access the Service from outside the United States, you do so on your own initiative and are responsible for compliance with local law.

## 10. Children

The Service is intended only for users who are at least 18 years old, and we do not knowingly collect personal information from anyone under 18. If you believe someone under 18 has provided us personal information, contact us at hello@slowgoapp.com and we will investigate and delete it where appropriate.

## 11. Changes to This Policy

We may update this Privacy Policy from time to time. We will post the updated version at slowgoapp.com/privacy and update the "Last updated" date, and for material changes we will provide additional notice through the App or the Site. When a change describes something a new version of the App will do, we say which version, so the Policy is accurate for every version in use. Your continued use of the Service after changes take effect constitutes acceptance of the updated Policy.

## 12. Contact Us

**BackRoad Apps LLC**
4498 Main St, Ste 4 #5690
Amherst, NY 14226, USA
Email: hello@slowgoapp.com
Telephone: (716) 235-3699
Web: slowgoapp.com
