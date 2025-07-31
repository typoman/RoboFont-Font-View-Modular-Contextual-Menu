from spaceSeperated import *
from mojo.UI import CurrentSelectedGlyphNames
NON_UNICODE_FALLBACK = ord(' ')

def get_char_for_glyph(glyph):
    if glyph.unicodes:
        return chr(glyph.unicodes[0])
    elif glyph.features.sourceGlyphs:
        sourceGlyphNames = list(glyph.features.sourceGlyphs.keys())[0]
        chars = ""
        for g in sourceGlyphNames:
            chars += get_char_for_glyph(font[g])
        return chars
    else:
        return "/" + glyph.name


def get_selected_glyphs_unicodes(font):
    """
    Set fallback_non_unicode to True if you want to have unicodes for
    non-unicode glyphs based on how they're subsituted in the feature file.
    """
    result = []
    for glyph_name in CurrentSelectedGlyphNames():
        glyph = font[glyph_name]
        result.append(get_char_for_glyph(glyph))
    return "\n".join(result)

if __name__ == "__main__":
    font = CurrentFont()
    if font is not None:
        selected_glyph_names = get_selected_glyphs_unicodes(font)
        copy_to_clipboard(f"{selected_glyph_names}")
        print("Glyph names copied to clipboard.")
    else:
        print("No font open.")
