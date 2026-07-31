# SlowGo Privacy Policy

**Last updated: July 31, 2026**

This Privacy Policy describes how **BackRoad Apps LLC** ("**BackRoad Apps**," "**we**," "**us**," or "**our**") handles information in connection with the SlowGo mobile application (the "**App**") and the slowgoapp.com website (the "**Site**") (together, the "**Service**").

**The short version:** SlowGo uses your location to do its job — showing where you are, suggesting routes, and checking your local weather. Your saved ride history stays on your phone. We don't require accounts, we don't sell your information, and we don't show ads.

## 1. Information We Collect

**We do not require an account.** The App does not ask for your name, email address, phone number, or any login.

**Precise location.** With your permission (through your device's location prompt), the App collects your device's precise location while you use it, to show your position on the map, calculate and display routes, search for nearby places, and provide local weather. When you request a route or search, the relevant coordinates are transmitted to the providers that fulfill the request (see Section 3). You can withdraw location permission at any time in your device settings; core features of a navigation app will not work without it.

**Ride, favorite, and settings data (stored on your device).** The App stores your ride history, favorite places, recent destinations, and settings on your device. See Section 5 for details and controls.

**Diagnostics and reliability data.** If the App crashes or encounters an error, a diagnostic report may be generated so we can find and fix the problem. Before any report is sent, the App is configured to remove location coordinates and other trip-revealing fields (see Section 4). We also process a small, fixed set of coordinate-free product metrics to keep the Service reliable — whether a route request was served, which quick-link category was tapped, and how many map tiles a session loaded. Section 4 lists them in full.

**Device and technical information.** Providers that serve the App's requests (Section 3) receive standard technical information necessary to respond, such as your IP address and basic device and app information. Our Site is a largely static website; our hosting provider may process standard server logs (such as IP address and browser type) to operate and secure the Site.

**Information you send us.** If you email hello@slowgoapp.com, we receive your email address and the contents of your message, which we use to respond and to improve the Service.

**We do not collect** contacts, photos or videos, microphone audio, health data, biometric data, advertising identifiers, or precise location while the App is closed.

## 2. How We Use Information; Notice at Collection

We use information to: provide the Service (position, routing, place search, weather); operate the App's safety-related display features (for example, identifying higher-speed segments of a route); diagnose and fix crashes and reliability problems; secure and operate the Service; respond to your messages; and comply with law. The categories we process, the purposes, and our retention approach are described in this Policy and, for location and diagnostics, are surfaced in the App at the point of collection. We do **not** use your information for advertising, and we do not build advertising or tracking profiles of you.

## 3. Where Your Information Goes

To fulfill your requests, the App sends your coordinates and related request data to the services that do the work:

| Provider | What it does | What it receives |
|---|---|---|
| BackRoad Apps routing server (Valhalla, operated by us) | Calculates cart-friendly routes, and looks up the posted speed limits along a route it has calculated | Trip start/end coordinates, route requests, and the shape of a calculated route |
| Stadia Maps | Map tiles and styles, place search (geocoding) | The map area being viewed, and search text with a nearby coordinate for distance ranking |
| OpenStreetMap community services (Overpass API) | Nearby-place search, place details, and checking whether paths on a route are cart-legal | Search-area coordinates and queries, and sample points along a calculated route |
| U.S. National Weather Service | Local weather and forecasts | Approximate area coordinates |
| Sentry | Crash and error reporting, and a small set of coordinate-free product metrics we use to keep the App healthy | Diagnostics, configured to exclude location and trip-revealing data before sending; and three app-health events — whether a route request was served, which quick-link category was tapped, and how many map tiles a session loaded (counts and fixed categories only, never coordinates or your search text) |
| Apple | App distribution, and payment processing if paid features are offered | Per Apple's own terms and privacy policy |

**Routing stays with us.** Route calculations and speed-limit verification are performed on SlowGo's own servers. No third party receives your route's origin or destination. The App previously used outside routing services as a backup when our own server could not be reached; it no longer does, and no such request is made under any circumstances.

These providers process requests to deliver the Service under their own terms or public usage policies, and our agreements with them where they exist. **We do not maintain user accounts and do not intentionally build a persistent, account-linked history of where you go.** Our routing server processes route requests to answer them; our access and security logs are configured not to record route coordinates. Providers may retain request and security logs under their own policies, including where reasonably necessary for security, fraud prevention, legal compliance, or backups.

We may also disclose information if required by law, to protect the rights, safety, or property of BackRoad Apps or others, or in connection with a merger, acquisition, or sale of assets (in which case this Policy will continue to apply to previously collected information unless you are notified otherwise).

**We do not sell your personal information, and we do not share it for cross-context behavioral advertising.**

## 4. Crash and Error Reports, and Product Metrics

If SlowGo crashes or hits an error, a diagnostic report may be sent to our crash-reporting provider (Sentry) so we can fix the problem. Crash-reporting tools can otherwise capture sensitive context, so before anything is sent the App is configured to remove latitude and longitude, addresses, route endpoints, search text, and request bodies, URLs, or breadcrumbs that could reveal a trip or destination. We configure the provider to limit IP-address storage, minimize default data collection, and restrict retention and access. Crash reports are about the App's health, not about where you went.

The same connection also carries three product metrics, and we list them here rather than describe them in general terms: whether a route request was served or not, which quick-link category (for example "Coffee" or "Pharmacy") was tapped, and how many map tiles a session loaded. Each is a fixed category or a whole number — there are no coordinates, no addresses and no text you typed in any of them, and they pass through the same removal step described above. We use them to tell whether routing is working and to keep our map-tile usage within budget.

## 5. What Stays on Your Phone

**Your saved ride history stays on your phone.** SlowGo keeps your most recent rides (up to 100) in the App's storage on your device, and stores their start and end points at reduced precision — close enough to remember the trip, not close enough to point at a doorstep. Favorites are stored at full precision so they take you exactly where you saved. (Separately, when you actually request a route, that route's start and end coordinates are transmitted to providers to calculate it, as described in Section 3 — this is different from the on-device history.)

**Your most recent position is also saved on your phone.** So the map can open where you left off instead of a blank screen while your first GPS reading arrives, the App keeps your **single most recent location reading at full precision**, along with what produced it (a live reading or the position your device had already cached), when it was taken, and how accurate it was. It is a single point, not a trail: each new reading overwrites the previous one, and no history of these readings is kept. It stays on your device until you delete the App. This is the most precise location the App keeps on your phone, which is why we name it here specifically.

**An in-progress ride is saved so you can resume it.** When you start navigating, the App saves that ride's **destination at full precision** (with its label), the custom starting point if you set one, and the time you started, so that if the App is closed or crashes mid-ride it can offer to pick the trip back up. It is cleared as soon as you arrive, when you end the ride, when you decline the offer to resume, and automatically if it is more than 90 minutes old or you are no longer near the trip when the App next opens.

**The map's last position is saved.** The App separately stores **where the map was last looking** — a center point and zoom level — so re-opening the App restores your view instead of jumping. This is a map view, not a record of where you were; you can pan the map anywhere without going there. It is overwritten as you move the map and stays on your device until you delete the App.

**Your controls:** you can turn ride saving off ("Save ride history" in Settings), and you can delete all saved rides at any time ("Clear ride history" in Settings). Turning off the App's location permission stops new position readings from being taken or saved. Deleting the App removes all of its on-device data, including the three items above — which, apart from the in-progress ride clearing itself as described, is how they are removed.

**Device protections and backups:** on-device data is stored using standard iOS app storage and is protected by your device's own protections (such as your passcode and the operating system's safeguards). Your device backups (for example, iCloud or computer backups) may include the App's data. We do not separately encrypt this data beyond the protections your device provides.

## 6. Data Retention

Ride history, favorites, recents, and settings remain on your device until you delete them or delete the App. For information we or our infrastructure process: our access and security logs are retained no more than 14 days and are configured not to include route coordinates; reliability telemetry and Sentry crash events are retained approximately 90 days; emails you send us are retained approximately 24 months, or longer if needed for a legal matter; and routine Site server logs are retained approximately 30 days. If we introduce paid features, transaction and tax records may be retained up to 7 years as required by law. Third-party providers retain request data under their own policies. These periods are targets we configure and may adjust as reasonably necessary for security, legal, or operational reasons.

## 7. Security

Requests between the App and service providers are transmitted using industry-standard encryption in transit (HTTPS/TLS). On-device data is protected by your device's safeguards as described in Section 5. No method of transmission or storage is completely secure, and we cannot guarantee absolute security.

## 8. Your Choices

- **Location:** manage the App's location permission in your device settings.
- **Ride history:** toggle saving off, or clear it, in the App's Settings.
- **Crash reporting and reliability data:** these are limited and configured to exclude trip data; deleting the App stops all collection.
- **Do Not Track / Global Privacy Control:** the Service does not track you across other companies' apps or websites, so there is nothing for these signals to opt out of.

## 9. Your Privacy Rights

### United States state privacy rights

Depending on where you live (for example, California, Colorado, Connecticut, Texas, Utah, Virginia, and other states with comprehensive privacy laws), you may have rights to know, access, correct, delete, or obtain a copy of personal information, to opt out of sale, sharing, or targeted advertising, and to withdraw consent to processing of sensitive data such as precise location. **Our practices make most of this simple:** we do not sell or share personal information for advertising, we do not profile you, precise location is used only to provide the Service, and the personal information the Service keeps (your rides, favorites, and settings) lives on your device under your direct control — you can access it in the App and delete it yourself at any time (Section 5).

For anything else — including questions, or access or deletion requests concerning emails you have sent us — contact us at hello@slowgoapp.com and tell us the state where you reside. We will verify and respond as required by applicable law, we will not discriminate against you for exercising your rights, and if we deny a request you may appeal by replying to our response. You may use an authorized agent where applicable law allows.

**California notice:** in the preceding 12 months, we have collected the categories described in Section 1 (identifiers such as IP address; precise geolocation; internet/electronic activity and diagnostic information; and communications you send us), for the purposes in Section 2, disclosed to the service providers in Section 3, and retained per Section 6. We do not sell or share personal information as those terms are defined by California law, and we have no actual knowledge of selling or sharing personal information of consumers under 16. California residents may exercise the rights described above.

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
