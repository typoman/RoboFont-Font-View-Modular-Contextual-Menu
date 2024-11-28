from selection import *
f = CurrentFont()

gl2 = [g.name for g in f if g.isMark and g.anchors == ()]
limitFontViewToGlyphList(gl2)
