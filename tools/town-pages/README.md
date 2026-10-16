# Town and state cart-rules pages

Generator for `/cart-rules` and `/golf-carts/<slug>` on slowgoapp.com. Never edit the built HTML: edit the
content modules, rebuild, check.

| File | What it is |
|---|---|
| `towns.py`, `towns_fl_coast.py`, `towns_fl_inland.py`, `towns_ga_az.py`, `states.py` | Page content (one dict per page) |
| `build.py` | Builds every page, the hub, the sitemap block, the `_redirects` rewrites and `netlify/counted-links.mjs` TOWN_LINKS |
| `check.py` | Read-only checks of the built pages against Ron's rulings. Exit 0 = pass. Commits gate on it |
| `recheck.py` | Fetches the official sources, keeps `check-log.csv`, writes `recheck-schedule.json` |
| `check-log.csv` | One row per page, source and check |
| `recheck-schedule.json` | Per-page status and next due date. A copy goes to `~/Desktop/SlowGo/hub/data/town-rechecks.json` for the HUB |
| `held/` | Held pages (publish=False). Nothing in here ships |
| `review.py`, `review_scale.py` | Review sheets for Ron |

```
python3 tools/town-pages/build.py && python3 tools/town-pages/check.py
```

## Fixed wording (Ron 2026-10-17 afternoon, from the Codex review; check.py enforces it)

- Signs box: "Follow applicable law, posted restrictions and lawful directions from officers. If permission is
  unclear, don't use that road or path until confirmed." The old "final word" sentence must not appear anywhere.
- SlowGo paragraph: "SlowGo routes on roads posted 35 mph or under and never along faster roads; it doesn't
  establish cart access here." Then the page's own `slowgo` text (what SlowGo doesn't know about this town) sits in
  an amber "Check local rules before you ride." box right above the Get SlowGo button.
- Every LSV answer includes "can't travel along roads posted over 35; lawful crossings are separately regulated."
- No "faster stretches" or 36–45 wording anywhere.
- State pages: any sentence with "35" is about LSVs/NEVs, SlowGo or state park roads, never golf cart permission.
- Map links say what the map is and who publishes it (`street_map=(label, url[, note])`).
- Every town page links to its published state page.
- "No carts" pages (`no_carts=True`) can only be published with `prohibition=dict(vehicle=, roads=, jurisdiction=,
  source=)` from an official source that affirmatively prohibits. If we only failed to find permission, the page
  says "We haven't verified public-road authorization." Sentences that say "not allowed" because we "didn't find"
  something fail check.py.
- Held pages live in `held/`. The hub, sitemap, `_redirects` and TOWN_LINKS list published pages only.
- FAQ structured data, the meta description and the social descriptions are built from the visible text, and
  check.py compares them.

## "Rules checked" dates and rechecks (D23)

Each page shows `Rules checked <Month D, YYYY>`. build.py takes that date from `check-log.csv`. Nobody types it.
It's the **oldest** of the page's sources' latest *verified* checks, so every source was compared at least that
recently.

`check-log.csv` columns: `page, source_url, fetched, sha256, text_sha256, snapshot, result, verified, note`.
A row is `verified=yes` only when:

1. someone fetched the source, read it, and compared it with the page (`--mark-verified` or `--record`), or
2. an automatic fetch found the text exactly the same as a previous verified row (same `text_sha256`).

New baselines, changed sources and failed fetches are never verified, so the date only moves after a real fetch
and comparison.

The first rows (fetched 2026-10-15/16, no hash) record the reads behind the first drafts, taken from each page's
review notes, from before this log existed. The 2026-10-16 rows with hashes are the first fetched baseline.

### Quarterly recheck (every 91 days; `next_due` in the schedule)

```
python3 tools/town-pages/recheck.py --dry-run     # what would be fetched
python3 tools/town-pages/recheck.py               # fetch every published page's sources
```

- Polite by design: one request at a time, at least 4 s apart, 20 s apart on the same host, 120 a run at most.
  It never fetches Municode or LexisNexis (it refuses them and logs the refusal).
- Sources whose text hasn't changed since a verified check become verified automatically, and their pages' dates
  move.
- **Changed** or **failed** sources show as `needs read` in `recheck-schedule.json`. Read the source, fix the page
  content if the rules changed, then:

```
python3 tools/town-pages/recheck.py --mark-verified --url <URL> [--page <slug>] --note "what you read"
python3 tools/town-pages/build.py && python3 tools/town-pages/check.py
```

- Some city sites (CivicPlus and others) change their HTML on every load, so they often show as "changed" even
  when the rules haven't. That costs a read, never a wrong date.
- A host that blocks scripts (Osceola County's Akamai returns 403) can be fetched another way, read, and logged:

```
python3 tools/town-pages/recheck.py --record <slug> <URL> <downloaded file> --note "how it was fetched"
```

### Immediate recheck

On any complaint, or any sign of an official change (new ordinance, council action, a town email), recheck
that page right away:

```
python3 tools/town-pages/recheck.py --page <slug>
```

Read the result, fix the content, mark it verified, rebuild, check. If the page might now be wrong and can't be
fixed at once, set `publish=False` and rebuild. That holds the page.

A recheck never deploys anything. Pages go live only in a bundled, counted Netlify deploy after Ron's go.
