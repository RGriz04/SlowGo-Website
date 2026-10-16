import sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset
src, out = sys.argv[1], sys.argv[2]
RANGES = {"latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2190-2193,U+2212,U+2215,U+FEFF,U+FFFD",
 "latin-ext": "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"}
UNUSED = "U+0000-024F,U+0259,U+02B0-02FF,U+0300-036F,U+1E00-1EFF,U+2000-206F,U+20A0-20CF,U+2100-214F,U+2190-21FF,U+2212,U+2215,U+FEFF,U+FFFD"
jobs = [
 ("fraunces_Fraunces[SOFT,WONK,opsz,wght].ttf", "Fraunces-Roman.var.woff2", {"wght":(400,600), "SOFT":(30,100)}),
 ("fraunces_Fraunces-Italic[SOFT,WONK,opsz,wght].ttf", "Fraunces-Italic.var.woff2", {"wght":(400,600), "SOFT":(30,100)}),
 ("inter_Inter[opsz,wght].ttf", "Inter.var.woff2", {"wght":(400,600), "opsz":14}),
 ("jetbrainsmono_JetBrainsMono[wght].ttf", "JetBrainsMono.var.woff2", {"wght":(400,500)}),
]
for s, o, limits in jobs:
    f = TTFont(f"{src}/{s}", lazy=False)
    print(s, {a.axisTag:(a.minValue,a.defaultValue,a.maxValue) for a in f["fvar"].axes})
    f = instancer.instantiateVariableFont(f, limits); import io; b=io.BytesIO(); f.save(b); b.seek(0); f=TTFont(b, lazy=False)
    base = f
    for rn, U in RANGES.items():
     b=io.BytesIO(); base.save(b); b.seek(0); f=TTFont(b, lazy=False)
     opts = subset.Options(); opts.flavor = "woff2"; opts.layout_features = ["*"]; opts.name_IDs=["*"]; opts.name_languages=["*"]; opts.notdef_outline=True; opts.glyph_names=False
     sub = subset.Subsetter(opts); sub.populate(unicodes=subset.parse_unicodes(U)); sub.subset(f)
     f.flavor = "woff2"; on=o.replace(".var.", f".{rn}.var."); f.save(f"{out}/{on}")
     print(" ->", on, {a.axisTag:(a.minValue,a.defaultValue,a.maxValue) for a in f["fvar"].axes} if "fvar" in f else "static")
