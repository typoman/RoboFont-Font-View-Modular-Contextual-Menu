from selection import *
import fontgadgets.extensions.unicode

f = CurrentFont()

def findUnusedGlyphs(f):
    cr = f.naked().componentReferences
    result = []
    for g in f:
        if not g.pseudoUnicodes and g.name not in cr:
            result.append(g.name)
    return result

limitFontViewToGlyphList(findUnusedGlyphs(f))
