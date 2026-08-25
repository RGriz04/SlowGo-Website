#!/usr/bin/env python3
"""Regenerate the SlowGo /go QR code.

    python3 -m pip install segno
    python3 generate.py

The payload is https://slowgoapp.com/go and it must stay that way. It is never
the apps.apple.com URL: a printed QR cannot be recalled, and pointing it at the
site keeps the destination changeable in SlowGo-Launch/_redirects. See README.md
in this folder.
"""
import segno

PAYLOAD  = "https://slowgoapp.com/go"
VERSION  = "v1"
DARK     = "#0B1F15"   # --charcoal
LIGHT    = "#FBF7EF"   # --cream
SCALE    = 56          # integer px per module, so no module lands on a half pixel

qr = segno.make(PAYLOAD, error="h", mode="byte")

qr.save(f"slowgo-qr-go-{VERSION}.svg", scale=10, border=4, dark=DARK, light=LIGHT)
qr.save(f"slowgo-qr-go-{VERSION}.png", scale=SCALE, border=4, dark=DARK, light=LIGHT)

modules = qr.symbol_size(scale=1, border=0)[0]
print(f"payload : {PAYLOAD}")
print(f"symbol  : version {qr.version}, ECC {qr.error.upper()}, {modules}x{modules} modules")
print(f"png     : {qr.symbol_size(scale=SCALE, border=4)[0]}px square, {SCALE}px per module")
