from selection import *
import fontgadgets.extensions.robofont.UI
from mojo.UI import CurrentSelectedGlyphNames
"""

"""
f = CurrentFont()
gl = CurrentSelectedGlyphNames()


def getFeaturesFromGlyphs(f, gl):
    result = set()
    for gn in gl:
        g = f[gn]
        for gl, subs in g.features.targetGlyphs.items():
            for s in subs:
                result.update(s.features)
    return result


def getRelatedGlyphsForFeatures(f, features):
    result = []
    for g in f:
        for gl, subs in g.features.targetGlyphs.items():
            for s in subs:
                if set(s.features) & features:
                    result.append(g.name)
    return result


features = getFeaturesFromGlyphs(f, gl)
gl2 = getRelatedGlyphsForFeatures(f, features)
limitFontViewToGlyphList(gl2)
