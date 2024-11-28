from mojo.UI import limitFontViewToGlyphSet
import fontgadgets.extensions.robofont.UI
from mojo.UI import CurrentSelectedGlyphNames
f = CurrentFont()
d = f.info.descender
gs = set()
for g in CurrentSelectedGlyphNames():
    g = f[g]
    if g.isLigature and not g.isMark:
        gs.add(g.name)

limitFontViewToGlyphSet(gs)