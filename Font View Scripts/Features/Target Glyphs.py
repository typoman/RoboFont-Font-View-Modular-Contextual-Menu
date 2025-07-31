from mojo.UI import limitFontViewToGlyphSet
import fontgadgets.extensions.robofont.UI
from mojo.UI import CurrentSelectedGlyphNames
f = CurrentFont()
gl = CurrentSelectedGlyphNames()

def getSourceGlyphsForGlyphList(font, glyphNameList):
    """
    Returns the fonttools ast.Feature objects that the given glyphs are referenced in.
    """
    result = set()
    for gn in glyphNameList:
        g = font[gn]
        for gl, subs in g.features.targetGlyphs().items():
            result.update(gl)
    return result

gl2 = getSourceGlyphsForGlyphList(f, gl)
gl2.update(gl)

limitFontViewToGlyphSet(gl2)