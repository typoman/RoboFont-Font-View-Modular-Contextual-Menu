from selection import *
f = CurrentFont()

skipExport = f.lib.get("public.skipExportGlyphs", [])

limitFontViewToGlyphList(skipExport)
