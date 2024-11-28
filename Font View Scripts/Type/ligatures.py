from mojo.UI import limitFontViewToGlyphSet

f = CurrentFont()
gs = set()
for g in f:
    if g.isLigature and not g.isMark:
        gs.add(g.name)

limitFontViewToGlyphSet(gs)