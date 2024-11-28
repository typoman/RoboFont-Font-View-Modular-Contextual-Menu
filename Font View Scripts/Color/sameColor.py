from selection import *
from mojo.UI import CurrentSelectedGlyphNames
import mojo

f = CurrentFont()
gl = CurrentSelectedGlyphNames()
visibleGlyphNames = [
    g.name for g in mojo.UI.CurrentFontWindow().getGlyphCollection().getVisibleGlyphs()
]
colors = set()

for gn in gl:
    g = f[gn]
    colors.add(g.markColor)

gl = [g.name for g in f if g.markColor in colors]
gl2 = [g for g in gl if g in visibleGlyphNames]
limitFontViewToGlyphList(gl2)
