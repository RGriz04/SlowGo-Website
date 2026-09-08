# SlowGo QR codes

## The payload never changes

Every SlowGo QR code encodes **`https://slowgoapp.com/go`**. Never the
`apps.apple.com` URL, never a TestFlight link, never anything else.

This is the standing ruling and it is not a style preference. A QR code that has
been printed — on a sign at a cart path, on a card in a rental office, on the
back of a flyer — cannot be recalled or edited. Whatever it encodes, it encodes
forever. Pointing it at our own domain means the destination is decided in
`SlowGo-Launch/_redirects`, in this repo, where it can still be changed. Pointing
it at Apple would hand that decision permanently to a URL we do not control.

For the same reason `/go` answers **200**, not a 301. It is a forced rewrite to
`go/index.html`, so the printed address serves the page itself and there is no
redirect hop for a browser to remember. A 301 would be cached permanently,
pinning every phone that ever scanned the code to today's destination no matter
what `_redirects` said afterward.

## Files

| File | What it is |
|---|---|
| `slowgo-qr-go-v1.svg` | Vector. Use this for print and anywhere it can scale. 370×370 at 1×, 10 units per module. |
| `slowgo-qr-go-v1.png` | Raster, 2072×2072, 56 px per module. Use where SVG isn't accepted. |
| `generate.py` | Regenerates both from one payload constant. |

**Versioned, not overwritten.** If the payload, the colours, or the error
correction ever change, that is `v2` in new files. `v1` stays on disk exactly as
it is, because copies of it are already in the world and we need to be able to
look at what they encode.

## The symbol

- **Payload:** `https://slowgoapp.com/go` (24 bytes)
- **Version 3**, 29×29 modules
- **Error correction H** (~30% recoverable) — chosen over the usual M because
  these end up outdoors, on signage, scuffed and rained on. H costs one QR
  version and buys a lot of damage tolerance.
- **Quiet zone:** 4 modules, the spec minimum. Do not crop it.
- **Dark** `#0B1F15` (`--charcoal`), **light** `#FBF7EF` (`--cream`) — the site
  palette. Contrast is about 16.9:1, far above what any scanner needs.

The light modules are **opaque cream, not transparent**, on purpose. A
transparent QR dropped onto a mid-tone background stops scanning.

## Rules for using it

- Don't recolour it, invert it, round the modules, or put a logo in the middle.
  It is at ECC H, so a small centre logo would probably still scan — but
  "probably" is not good enough for something that cannot be reprinted.
- Don't crop the quiet zone.
- Don't scale the PNG up past 2072 px; use the SVG.
- Print it at 2 cm / 0.8 in square or larger. It decodes down to about 96 px on
  screen, but print, distance and camera shake are less forgiving than a file.

## Verified

Generated 2026-08-25 and decoded back with OpenCV at 2072, 1024, 512, 256, 148
and 96 px, plus a JPEG-q35 pass standing in for a phone photo of a printed sign.
All returned exactly `https://slowgoapp.com/go`. The SVG and PNG module grids
were both compared against the reference matrix and match it exactly.

## Regenerating

```sh
python3 -m pip install segno
python3 generate.py
```

Deterministic — same payload in, same bytes out.
