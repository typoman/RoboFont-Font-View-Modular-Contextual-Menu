from selection import *
from mojo.UI import CurrentSelectedGlyphNames
"""

"""
f = CurrentFont()
gl = CurrentSelectedGlyphNames()

def getFeaturesFromGlyphs(f, gl):
    result = set()
    for gn in gl:
        g = f[gn]
        for gl, subs in g.features.sourceGlyphs.items():
            for s in subs:
                result.update(s.features)
    return result

def getRelatedGlyphsForFeatures(f, features):
    result = []
    for g in f:
        for gl, subs in g.features.sourceGlyphs.items():
            for s in subs:
                if s.features & features:
                    result.append(g.name)
    return result

features = getFeaturesFromGlyphs(f, gl)
gl2 = getRelatedGlyphsForFeatures(f, features)
limitFontViewToGlyphList(gl2)