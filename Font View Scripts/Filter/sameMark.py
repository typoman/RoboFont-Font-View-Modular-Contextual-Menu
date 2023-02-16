from selection import *
from mojo.UI import CurrentSelectedGlyphNames
f = CurrentFont()
gl = CurrentSelectedGlyphNames()
colors = set()
for gn in gl:
	g = f[gn]
	colors.add(g.markColor)

gl2 = [g.name for g in f if g.markColor in colors]
limitFontViewToGlyphList(gl2)
