from category import *

if __name__ == "__main__":
    gname = CurrentSelectedGlyphNames()[0]
    f = CurrentFont()
    g = f[gname]
    scripts = g.scripts
    gl = [g.name for g in f if g.scripts == scripts]
    limitFontViewToGlyphSet(gl)
