from mojo.UI import limitFontViewToGlyphSet


def findSameScriptAsCurrentGlyph(f):
    g = CurrentGlyph()
    scripts = g.scripts
    result = []
    for g in f:
        if set(g.scripts) & set(scripts):
            result.append(g.name)
    return result


f = CurrentFont()
limitFontViewToGlyphSet(findSameScriptAsCurrentGlyph(f))
