from selection import *

def getBaseGlyphs(font, glyphList):
    result = set()
    for gName in glyphList:
        result.add(gName)
        g = font[gName]
        for c in g.components:
            result.add(c.baseGlyph)
            result.update(getBaseGlyphs(font, [c.baseGlyph]))
    return result

if __name__ == '__main__':
    f = CurrentFont()
    gl = getBaseGlyphs(f, f.selectedGlyphNames)
    limitFontViewToGlyphList(gl)
