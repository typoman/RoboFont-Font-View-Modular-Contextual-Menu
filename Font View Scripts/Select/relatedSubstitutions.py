from mojo.UI import limitFontViewToGlyphSet, CurrentSelectedGlyphNames

f = CurrentFont()
gl = CurrentSelectedGlyphNames()
relatedGlyphs = set()
for gn in gl:
    g = f[gn]
    for gs in g.features.targetGlyphs.keys():
        relatedGlyphs.update(gs)
    for gs in g.features.sourceGlyphs.keys():
        relatedGlyphs.update(gs)

f.selectedGlyphNames = relatedGlyphs
