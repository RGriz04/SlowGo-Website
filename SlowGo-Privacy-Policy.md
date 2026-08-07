# SlowGo Privacy Policy

**Last updated: August 7, 2026**

This Privacy Policy describes how **BackRoad Apps LLC** ("**BackRoad Apps**," "**we**," "**us**," or "**our**") handles information in connection with the SlowGo mobile application (the "**App**") and the slowgoapp.com website (the "**Site**") (together, the "**Service**").

**The short version:** SlowGo uses your location to do its job — showing where you are, suggesting routes, and checking your local weather. Your saved ride history stays on your phone. We don't require accounts, we don't sell your information, and we don't show ads.

## 1. Information We Collect

**We do not require an account.** The App does not ask for your name, email address, phone number, or any login.

**Precise location.** With your permission (through your device's location prompt), the App collects your device's precise location while you use it, to show your position on the map, calculate and display routes, search for nearby places, and provide local weather. When you request a route or search, the relevant coordinates are transmitted to the providers that fulfill the request (see Section 3). Opening the ride postcard also looks up the general area a ride started and ended in, so the card can name those places; that lookup sends only an approximate position — rounded to about 110 metres — and never your exact start or end point. You can withdraw location permission at any time in your device settings; core features of a navigation app will not work without it.

**Ride, favorite, and settings data (stored on your device).** The App stores your ride history, favorite places, recent destinations, and settings on your device. See Section 5 for details and controls.

**Diagnostics and reliability data.** If the App crashes or encounters an error, a diagnostic report may be generated so we can find and fix the problem. Before any report is sent, the App is configured to remove location coordinates and other trip-revealing fields (see Section 4). We also process a small, fixed set of coordinate-free product metrics to keep the Service reliable — whether a route request was served, which quick-link category was tapped, and how many map tiles a session loaded. Section 4 lists them in full.

**Device and technical information.** Providers that serve the App's requests (Section 3) receive standard technical information necessary to respond, such as your IP address and basic device and app information. Our Site is a largely static website; our hosting provider may process standard server logs (such as IP address and browser type) to operate and secure the Site.

**Information you send us.** If you email hello@slowgoapp.com, we receive your email address and the contents of your message, which we use to respond and to improve the Service.

**Information you give us through the Site's forms.** The Site has a waitlist form, which asks for your email address, and a town-request form, which asks for your email address and the name of a town or community. Both are optional, and neither is part of the App. Section 3 describes what happens to what you submit.

**We do not collect** contacts, photos or videos, microphone audio, health data, biometric data, advertising identifiers, or precise location while the App is closed.

## 2. How We Use Information; Notice at Collection

We use information to: provide the Service (position, routing, place search, weather); operate the App's safety-related display features (for example, identifying higher-speed segments of a route); diagnose and fix crashes and reliability problems; secure and operate the Service; respond to your messages; write to you about the launch and plan where to build coverage next, if you asked us to through a Site form; and comply with law. The categories we process, the purposes, and our retention approach are described in this Policy and, for location and diagnostics, are surfaced in the App at the point of collection. We do **not** use your information for advertising, and we do not build advertising or tracking profiles of you.

## 3. Where Your Information Goes

To fulfill your requests, the Service sends your coordinates and related request data to the services that do the work:

| Provider | What it does | What it receives |
|---|---|---|
| BackRoad Apps routing server (Valhalla, operated by us) | Calculates cart-friendly routes, and looks up the posted speed limits along a route it has calculated | Trip start/end coordinates, route requests, and the shape of a calculated route |
| Stadia Maps | Map tiles and styles, place search (geocoding), and neighborhood names for the ride postcard | The map area you are viewing; your search text along with a nearby coordinate so results can be ranked by distance; and, when you open a ride postcard, the approximate trip start/end areas (rounded to about 110 metres) |
| OpenStreetMap community services (Overpass API) | Nearby-place search, place details, and checking whether paths on a route are cart-legal | Search-area coordinates and queries, and sample points along a calculated route |
| U.S. National Weather Service | Local weather and forecasts | Approximate area coordinates |
| Sentry | Crash and error reporting, and a small set of coordinate-free product metrics we use to keep the App healthy | Diagnostics, configured to exclude location and trip-revealing data before sending; and three app-health events — whether a route request was served, which quick-link category was tapped, and how many map tiles a session loaded (counts and fixed categories only, never coordinates or your search text) |
| Netlify | Hosts the Site and receives what you submit through its waitlist and town-request forms | The email address, and for a town request the town or community name, that you type into a Site form; plus standard server logs such as IP address and browser type |
| Apple | App distribution, and payment processing if paid features are offered | Per Apple's own terms and privacy policy |

**When you share.** Some things leave the App because you ask them to, through your device's own share sheet. What you send goes to whichever app you pick there — Messages, Mail, a notes app, anything installed — and from that point it is handled by that app and its provider, not by us. We do not receive a copy and we do not keep a record of what you shared or who you sent it to.

- **Sharing a place** sends the place's name and a standard map link containing its exact coordinates, so the person receiving it can open it in a maps app.
- **Sharing a ride postcard** sends the picture: your ride's stats, the general areas it started and ended in, and any note you wrote. It does not include a map, the shape of your route, or your exact start or end point.
- **Sharing your savings summary** sends a few lines of text about totals. It contains no locations at all.

**Routing stays with us.** Route calculations and speed-limit verification are performed on SlowGo's own servers. No third party receives your route request — your origin and destination are sent only to our own routing server. (Place search sends your search text and a nearby coordinate to the search providers listed above.) The App previously used outside routing services as a backup when our own server could not be reached; it no longer does, and no such request is made under any circumstances.

These providers process requests to deliver the Service under their own terms or public usage policies, and our agreements with them where they exist. **We do not maintain user accounts and do not intentionally build a persistent, account-linked history of where you go.** Our routing server processes route requests to answer them; our access and security logs are configured not to record route coordinates. Providers may retain request and security logs under their own policies, including where reasonably necessary for security, fraud prevention, legal compliance, or backups.

We may also disclose information if required by law, to protect the rights, safety, or property of BackRoad Apps or others, or in connection with a merger, acquisition, or sale of assets (in which case this Policy will continue to apply to previously collected information unless you are notified otherwise).

**We do not sell your personal information, and we do not share it for cross-context behavioral advertising.**

### The Site's waitlist and town-request forms

The Site has two optional forms. The **waitlist** form collects your email address. The **town-request** form collects your email address and the name of a town or community. Nothing else is asked for, and the App never uses these forms.

We use what you submit for one purpose each: to write to you when SlowGo is available where you ride, and to decide which areas to build coverage for next. Submissions are handled by **Netlify**, which hosts the Site and stores form entries for us as a service provider.

**We do not sell this information, we do not share it for advertising, and we do not use it for marketing beyond the purpose you submitted it for.** You will not receive a newsletter, a drip campaign, or promotions from us.

We keep a submission until we have sent the launch notification for your area, or until you ask us to delete it, whichever comes first. To have your entry removed at any time, email hello@slowgoapp.com from the address you submitted, or tell us the address you used, and we will delete it.

## 4. Crash and Error Reports, and Product Metrics

If SlowGo crashes or hits an error, a diagnostic report may be sent to our crash-reporting provider (Sentry) so we can fix the problem. Crash-reporting tools can otherwise capture sensitive context, so the App is configured to keep location out of them in three separate ways.

**Reports raised by the App's own code** pass through a filter before they leave the device. That filter works from a list of fields it is allowed to send — anything it does not recognise is dropped rather than forwarded — and it removes latitude and longitude, addresses, route endpoints, search text, and request bodies, URLs, or breadcrumbs that could reveal a trip or destination. Values that look like coordinates are removed outright, not blurred or rounded.

**Reports raised by a crash in the device's own layer** are assembled by the crash reporter itself and do not pass through that filter. They contain no location because there is none for them to find: the App never gives the crash reporter your position, your route, or any place data, and we switch off the reporter's own capture of network requests, which is the other way a coordinate could reach it.

**In both cases we send no personal identifiers.** There is no account, and the App does not attach a user ID, an email address, or a name to any report. We configure the provider to limit IP-address storage, minimize default data collection, and restrict retention and access. Crash reports are about the App's health, not about where you went.

The same connection also carries three product metrics, and we list them here rather than describe them in general terms: whether a route request was served or not, which quick-link category (for example "Coffee" or "Pharmacy") was tapped, and how many map tiles a session loaded. Each is a fixed category or a whole number — there are no coordinates, no addresses and no text you typed in any of them, and they pass through the same removal step described above. We use them to tell whether routing is working and to keep our map-tile usage within budget.

## 5. What Stays on Your Phone

**Your saved ride history stays on your phone.** SlowGo keeps your most recent rides (up to 100) in the App's storage on your device, and stores their start and end points at reduced precision: rounded to four decimal places, which is a grid of roughly 11 metres. That is coarser than the reading your device produces, and it is what the App keeps rather than the exact point. Favorites are stored at full precision so they take you exactly where you saved. (Separately, when you actually request a route, that route's start and end coordinates are transmitted to providers to calculate it, as described in Section 3 — this is different from the on-device history.)

**Your most recent position is also saved on your phone.** So the map can open where you left off instead of a blank screen while your first GPS reading arrives, the App keeps your **single most recent location reading at full precision**, along with what produced it (a live reading or the position your device had already cached), when it was taken, and how accurate it was. It is a single point, not a trail: each new reading overwrites the previous one, and no history of these readings is kept. It stays on your device until you delete the App. This is the most precise location the App keeps on your phone, which is why we name it here specifically.

**An in-progress ride is saved so you can resume it.** When you start navigating, the App saves that ride's **destination at full precision** (with its label), where the ride started, the shape of the route itself (rounded to roughly 11 metres), the custom starting point if you set one, and the time you started, so that if the App is closed or crashes mid-ride it can offer to pick the trip back up. The route's shape is what lets the App tell that you are still somewhere on the trip, rather than only whether you are near its destination. It is cleared as soon as you arrive, when you end the ride, when you decline the offer to resume, and automatically if it is more than 90 minutes old or you are no longer on the trip when the App next opens.

**The map's last position is saved.** The App separately stores **where the map was last looking** — a center point and zoom level — so re-opening the App restores your view instead of jumping. This is a map view, not a record of where you were; you can pan the map anywhere without going there. It is overwritten as you move the map and stays on your device until you delete the App.

**Your controls:** you can turn ride saving off ("Save ride history" in Settings), and you can delete all saved rides at any time ("Clear ride history" in Settings). Turning off the App's location permission stops new position readings from being taken or saved. Deleting the App removes all of its on-device data, including the three items above — which, apart from the in-progress ride clearing itself as described, is how they are removed.

**Device protections and backups:** on-device data is stored using standard iOS app storage and is protected by your device's own protections (such as your passcode and the operating system's safeguards). Your device backups (for example, iCloud or computer backups) may include the App's data. We do not separately encrypt this data beyond the protections your device provides.

## 6. Data Retention

Ride history, favorites, recents, and settings remain on your device until you delete them or delete the App. For information we or our infrastructure process: our access and security logs are retained no more than 14 days and are configured not to include route coordinates; reliability telemetry and Sentry crash events are retained approximately 90 days; emails you send us are retained approximately 24 months, or longer if needed for a legal matter; waitlist and town-request submissions are kept until the launch notification for that area has been sent or you ask us to delete them, whichever comes first; and routine Site server logs are retained approximately 30 days. If we introduce paid features, transaction and tax records may be retained up to 7 years as required by law. Third-party providers retain request data under their own policies. These periods are targets we configure and may adjust as reasonably necessary for security, legal, or operational reasons.

## 7. Security

Requests between the App and service providers are transmitted using industry-standard encryption in transit (HTTPS/TLS). On-device data is protected by your device's safeguards as described in Section 5. No method of transmission or storage is completely secure, and we cannot guarantee absolute security.

## 8. Your Choices

- **Location:** manage the App's location permission in your device settings.
- **Ride history:** toggle saving off, or clear it, in the App's Settings.
- **Crash reporting and reliability data:** these are limited and configured to exclude trip data; deleting the App stops all collection.
- **Waitlist and town requests:** email hello@slowgoapp.com to have your submission deleted.
- **Do Not Track / Global Privacy Control:** the Service does not track you across other companies' apps or websites, so there is nothing for these signals to opt out of.

## 9. Your Privacy Rights

### United States state privacy rights

Depending on where you live (for example, California, Colorado, Connecticut, Texas, Utah, Virginia, and other states with comprehensive privacy laws), you may have rights to know, access, correct, delete, or obtain a copy of personal information, to opt out of sale, sharing, or targeted advertising, and to withdraw consent to processing of sensitive data such as precise location. **Our practices make most of this simple:** we do not sell or share personal information for advertising, we do not profile you, precise location is used only to provide the Service, and the personal information the Service keeps (your rides, favorites, and settings) lives on your device under your direct control — you can access it in the App and delete it yourself at any time (Section 5).

For anything else — including questions, or access or deletion requests concerning emails you have sent us or anything you submitted through a Site form — contact us at hello@slowgoapp.com and tell us the state where you reside. We will verify and respond as required by applicable law, we will not discriminate against you for exercising your rights, and if we deny a request you may appeal by replying to our response. You may use an authorized agent where applicable law allows.

**California notice:** in the preceding 12 months, we have collected the categories described in Section 1 (identifiers such as IP address, and the email address and town you may submit through a Site form; precise geolocation; internet/electronic activity and diagnostic information; and communications you send us), for the purposes in Section 2, disclosed to the service providers in Section 3, and retained per Section 6. We do not sell or share personal information as those terms are defined by California law, and we have no actual knowledge of selling or sharing personal information of consumers under 16. California residents may exercise the rights described above.

### Outside the United States

The Service is intended for use in the United States, and information is processed in the United States. If you access the Service from outside the United States, you do so on your own initiative and are responsible for compliance with local law.

## 10. Children

The Service is intended only for users who are at least 18 years old, and we do not knowingly collect personal information from anyone under 18. If you believe someone under 18 has provided us personal information, contact us at hello@slowgoapp.com and we will investigate and delete it where appropriate.

## 11. Changes to This Policy

We may update this Privacy Policy from time to time. We will post the updated version at slowgoapp.com/privacy and update the "Last updated" date, and for material changes we will provide additional notice through the App or the Site. Your continued use of the Service after changes take effect constitutes acceptance of the updated Policy.

## 12. Contact Us

**BackRoad Apps LLC**
4498 Main St, Ste 4 #5690
Amherst, NY 14226, USA
Email: hello@slowgoapp.com
Telephone: (716) 235-3699
Web: slowgoapp.com
