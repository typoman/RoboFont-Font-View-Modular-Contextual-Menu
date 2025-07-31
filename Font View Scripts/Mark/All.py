from mojo.UI import limitFontViewToGlyphSet
f = CurrentFont()

gl2 = [g.name for g in f if g.isMark]
limitFontViewToGlyphSet(gl2)
