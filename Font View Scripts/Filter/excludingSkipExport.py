from selection import *
f = CurrentFont()

skipExport = f.lib.get("public.skipExportGlyphs", [])

limitFontViewToGlyphList((gn for gn in f.keys() if gn not in skipExport))
