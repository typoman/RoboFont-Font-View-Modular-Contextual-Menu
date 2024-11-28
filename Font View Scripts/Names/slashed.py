from spaceSeperated import *

if __name__ == "__main__":
    font = CurrentFont()
    if font is not None:
        selected_glyph_names = get_selected_glyph_names(font, " /")
        copy_to_clipboard(f"/{selected_glyph_names}")
        print("Glyph names copied to clipboard.")
    else:
        print("No font open.")
