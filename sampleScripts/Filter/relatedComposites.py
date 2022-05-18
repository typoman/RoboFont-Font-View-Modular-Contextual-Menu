from selection import *

def getRelatedCompositesOfSelectedGlyphs():
    font = CurrentFont()
    component_users = [g for g in font if g.components]
    components_used = {}
    for cu in component_users:
        for c in cu.components:
            components_used.setdefault(c.baseGlyph, []).append(cu.name)

    dependent_glyphs = []
    selection = font.selectedGlyphNames
    dependent_glyphs.extend(selection)
    for gname in selection:
        composite_role = components_used.get(gname, None)
        if composite_role:
            dependent_glyphs.extend(composite_role)
    for dep_gname in dependent_glyphs:
        dependencies = components_used.get(dep_gname)
        if dependencies:
            dependent_glyphs.extend(components_used.get(dep_gname))
    return dependent_glyphs

gl = getRelatedComposites()
limitFontViewToGlyphList(gl)
