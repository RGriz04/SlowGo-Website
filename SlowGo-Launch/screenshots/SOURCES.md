# Where these screenshots came from

The four screens on the homepage are derived from the **exact PNGs uploaded to
App Store Connect for the v1.0 submission** - the 6.9-inch portrait set,
1290x2796. They are not captures of the App Store web page.

Confirmed against the live listing on 2026-08-25: the screenshot filenames the
iTunes lookup API returns for id 6803226504 match this set one-for-one, in
order. Version 1.0.

**The originals live at `/Users/ron/Desktop/AppStore/6.9in/` and are untouched.**
They are not copied into this repo - they are about 1.1 MB each. The SHA-256 of
each original is recorded here so any derivative can be traced back to the file
it came from.

| On the page | Source original | SHA-256 of the 1290x2796 original |
|---|---|---|
| `route-chooser.webp` / `route-chooser.png` (600x1300) | `03-route-chooser.png` | `3ece365e6b0d40b9a926ad3a564124dcea3a3ee05a55802dfe3a93d602186468` |
| `heads-up.webp` / `heads-up.png` (600x1300) | `06-heads-up-detail.png` | `ae4f1b081a31f6cd17c3241fb9844cbd3825faeb06130d4d9e4cc2f5865c30d2` |
| `turn-by-turn.webp` / `turn-by-turn.png` (600x1300) | `01-turn-by-turn-hero.png` | `451d60cf51fd780ff9e9234935a5cef8ba121821b9bf881c34f7b10622956f99` |
| `nogo.webp` / `nogo.png` (600x1300) | `02-nogo.png` | `251565787936447ed3081dab0d92b690295464de16a58d1effb2d7d805891904` |

The 6.5-inch set (`../6.5in/`, 1242x2688) and the CarPlay set are the same
screens at other sizes. The 6.9-inch set is used here because it is the
highest resolution available.

## Why two formats

Each screen ships as WebP with a PNG fallback in a `<picture>` element. WebP is
roughly less than half the bytes and every current browser takes it; the PNG is
there for anything that doesn't. No build step is involved either way.

## Regenerating

Downscale to 600 px wide with Lanczos. WebP at quality 82. PNG quantised to a
128-colour palette with Floyd-Steinberg dither - these are flat UI over vector
map tiles, so the palette is visually lossless and roughly halves the file
against truecolour.

Do not upscale, do not crop, and do not add device frames. The site shows the
screens as they actually appear in the app.
