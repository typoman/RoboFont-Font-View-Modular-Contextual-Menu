from fontgadgets.decorators import *
from fontGit import FontGit
from fontGit.utils import RepoCache
import fontgadgets.extensions.glyph
import logging

"""
Clears the background layer and copies the data from given commit index.
The higher the commit index, the older the data in commit history.
"""

import fontgadgets; fontgadgets.tools.DEBUG = True
MASK_LAYER = 'public.background'
@font_property
def background(font):
    try:
        backgroundLayer = font.layers[MASK_LAYER]
    except KeyError:
        backgroundLayer = font.newLayer(MASK_LAYER)
    return backgroundLayer

def get_font_commit(f, commit_index=None):
    p = f.path
    sample_repo = RepoCache(p)
    if commit_index is not None:
        commits = sample_repo.commits
        commit_sha = commits[commit_index]
    else:
        commit_sha = None
    fc = FontGit.open_at_commit(p, commit_sha=commit_sha)
    return fc

def copy_from_glyph(bl, fc, backgroundG, commitG):
    """
    Copy from commitG to backgroundG.
    """
    for c in commitG.components:
        cgn = c.baseGlyph
        cg = fc[cgn]
        bg = bl[cgn]
        copy_from_glyph(bl, fc, bg, cg)
    backgroundG.clear()
    backgroundG.copyDataFromGlyph(commitG)
    fpg = backgroundG.asFontParts()
    fpg.changed()

def get_changed_glyphs(fc, commit_index=None):
    diff = fc.diffGlyphNames()
    result = set()
    for diff_t, gs in diff.items():
        result.update(gs)
    return result

def copy_changed_glyphs_to_background(bl, fc, glyph_names):
    for gn in glyph_names:
        bg = bl[gn]
        gc = fc[gn]
        copy_from_glyph(bl, fc, bg, gc)

if __name__ == '__main__':
    import fontgadgets.extensions.robofont.UI
    from mojo.UI import limitFontViewToGlyphSet

    f = CurrentFont().naked()
    fc = get_font_commit(f)
    gn = get_changed_glyphs(fc)
    bl = f.background
    fc = get_font_commit(f, 0)
    copy_changed_glyphs_to_background(bl, fc, gn)
    limitFontViewToGlyphSet(gn)

