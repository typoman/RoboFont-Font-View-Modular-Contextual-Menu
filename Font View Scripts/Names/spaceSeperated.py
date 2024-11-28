from mojo.roboFont import CurrentFont
from AppKit import NSPasteboard, NSPasteboardTypeString
from mojo.UI import CurrentSelectedGlyphNames

def get_selected_glyph_names(font, separator=' '):
    """
    Retrieves the names of selected glyphs in the given font.

    Args:
    font (RFont): The font object from RoboFont.
    separator (str): Separator for glyph names. Defaults to comma.

    Returns:
    str: A string containing the selected glyph names separated by the given separator.
    """
    return separator.join(CurrentSelectedGlyphNames())

def copy_to_clipboard(text):
    """
    Copies the given text to the clipboard.

    Args:
    text (str): The text to be copied to the clipboard.
    """
    pasteboard = NSPasteboard.generalPasteboard()
    pasteboard.clearContents()
    pasteboard.setString_forType_(text, NSPasteboardTypeString)

if __name__ == "__main__":
    font = CurrentFont()
    if font is not None:
        selected_glyph_names = get_selected_glyph_names(font)
        copy_to_clipboard(selected_glyph_names)
        print("Glyph names copied to clipboard.")
    else:
        print("No font open.")
