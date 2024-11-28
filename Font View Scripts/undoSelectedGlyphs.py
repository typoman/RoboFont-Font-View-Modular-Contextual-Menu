# menuTitle : Undo Glyphs - Contextual Menu
from pprint import pprint

"""
source: https://gist.github.com/ryanbugden/3b410f53f6a53eabeddc4753642df6a2
Run an undo on selected glyphs (menu)

2023.05.01
Ryan Bugden
"""

f = CurrentFont()
sel = f.selectedGlyphNames

glyphs_and_undo_titles = {}
for g_name in sel:
    g = f[g_name]
    m = f.document().getUndoManagerForGlyph_(g.naked())
    undo_title = m.undoMenuItemTitle()
    m.undo()
    g.changed()

    glyphs_and_undo_titles.update({g_name: undo_title})

f.changed()
print(f"\nPerformed the following undo(s) on the selected glyphs:")
pprint(glyphs_and_undo_titles)
