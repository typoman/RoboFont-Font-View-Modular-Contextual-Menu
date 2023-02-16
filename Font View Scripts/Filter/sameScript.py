from selection import *

def findSameScriptAsCurrentGlyph(f):
    g = CurrentGlyph()
    scripts = g.scripts
    result = []
    for g in f:
        if g.scripts & scripts:
            result.append(g.name)
    return result

f = CurrentFont()
limitFontViewToGlyphList(findSameScriptAsCurrentGlyph(f))
