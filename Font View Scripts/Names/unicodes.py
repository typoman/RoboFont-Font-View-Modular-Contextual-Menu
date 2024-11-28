from spaceSeperated import *
from mojo.UI import CurrentSelectedGlyphNames
NON_UNICODE_FALLBACK = ord(' ')

def get_selected_glyphs_unicodes(font, fallback_non_unicode=False):
    """
    Set fallback_non_unicode to True if you want to have unicodes for
    non-unicode glyphs based on how they're subsituted in the feature file.
    """
    glyph_unis = []
    for glyph_name in CurrentSelectedGlyphNames():
        glyph = font[glyph_name]
        if glyph.unicode:
            glyph_uni = glyph.unicode
        elif fallback_non_unicode:
            sourceGlyphNames = list(glyph.features.sourceGlyphs.keys())
            if sourceGlyphNames:
                glyph = font[sourceGlyphNames[0]]
                glyph_uni = glyph.unicode
            else:
                glyph_uni = NON_UNICODE_FALLBACK
        else:
            continue
        glyph_unis.append(glyph_uni)
    return glyph_uni

if __name__ == "__main__":
    font = CurrentFont()
    if font is not None:
        selected_glyph_names = get_selected_glyphs_unicodes(font)
        copy_to_clipboard(f"/{selected_glyph_names}")
        print("Glyph names copied to clipboard.")
    else:
        print("No font open.")
