import fontgadgets.extensions.robofont.UI
import fontgadgets.extensions.unicode.properties
from mojo.UI import limitFontViewToGlyphSet, CurrentSelectedGlyphNames

if __name__ == "__main__":
	gname = CurrentSelectedGlyphNames()[0]
	f = CurrentFont()
	g = f[gname]
	unicodeCategory = g.unicodeCategory
	gl = [g.name for g in f if g.unicodeCategory == unicodeCategory]
	limitFontViewToGlyphSet(gl)
