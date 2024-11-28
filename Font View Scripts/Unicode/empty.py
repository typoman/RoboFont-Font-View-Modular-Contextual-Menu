import fontgadgets.extensions.robofont.UI
from mojo.UI import limitFontViewToGlyphSet, CurrentSelectedGlyphNames

f = CurrentFont()
gl = [g.name for g in f if g.unicodes == ()]
limitFontViewToGlyphSet(gl)
