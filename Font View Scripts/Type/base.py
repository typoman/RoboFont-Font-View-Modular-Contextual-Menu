from mojo.UI import limitFontViewToGlyphSet

f = CurrentFont()
gs = set()
for g in f:
    if g.isBase:
        gs.add(g.name)

limitFontViewToGlyphSet(gs)