from selection import *
import fontgadgets.extensions.features

f = CurrentFont()

required_glyphs = (".notdef", ".null")

def findUnusedGlyphs(f):
    cr = f.naked().componentReferences
    skip_export = set(f.lib.get('public.skipExportGlyphs', []))
    skip_export.update(required_glyphs)
    result = []
    for g in f:
        gn = g.name
        if g.unicodes or gn in skip_export:
            continue
        if g.features.sourceGlyphs == {} and gn not in cr:
            result.append(g.name)
    return result

limitFontViewToGlyphList(findUnusedGlyphs(f))
