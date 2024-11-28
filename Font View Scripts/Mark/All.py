from selection import *
f = CurrentFont()

gl2 = [g.name for g in f if g.isMark]
limitFontViewToGlyphList(gl2)
