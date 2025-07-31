from mojo.UI import CurrentSpaceCenter
from mojo.UI import limitFontViewToGlyphSet
"""
Filter the glyph set in the view to the glyphs inside the space center.
"""

def geComps(g):
    return set([c.baseGlyph for c in g.components])

def limitVeiwToSpaceCenter(includingComposites=True):
    f = CurrentFont()
    glyphSet = set(f.keys())
    sp = CurrentSpaceCenter()
    gl = set(sp.get()) & glyphSet
    finalList = set(gl)
    if includingComposites:
        for g in gl:
            g = f[g]
            for c in g.components:
                finalList.add(c.baseGlyph)
        for g in f:
            if not g.contours and geComps(g) - finalList == set():
                finalList.add(g.name)

    limitFontViewToGlyphSet(finalList)

limitVeiwToSpaceCenter(1)
