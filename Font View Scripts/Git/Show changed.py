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


def get_changed_glyphs(fc):
    diff = fc.diffGlyphNames()
    result = set()
    for _, gs in diff.items():
        result.update(gs)
    return result


if __name__ == '__main__':
    import fontgadgets.extensions.robofont.UI
    from mojo.UI import limitFontViewToGlyphSet

    f = CurrentFont().naked()
    fc = get_font_commit(f)
    gn = get_changed_glyphs(fc)
    limitFontViewToGlyphSet(gn)

