from selection import *

def anchorNames(self, glyph):
    return set([a.name for a in glyph.anchors])

def filterToGlyphAttribute(font, attribute):
    if len(font.selectedGlyphNames):
        gName = font.selectedGlyphNames[0]
        g = font[gName]
        if attribute in ['anchors', 'contours', 'components']:
            reprAttr = getattr(g, attribute)
            filterList = [g.name for g in font if (
                len(getattr(g, attribute)) == len(reprAttr))]
        elif attribute == 'anchor_names':
            filterList = [
                g.name for g in font if
                anchorNames(g) == anchorNames(g)]
        else:
            filterList = [g.name for g in font if (
                getattr(g, attribute) == getattr(g, attribute))]
        return filterList

if __name__ == '__main__':
    f = CurrentFont()
    gl = filterToGlyphAttribute(f, 'width')
    limitFontViewToGlyphList(gl)
