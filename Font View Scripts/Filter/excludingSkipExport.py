from mojo.UI import limitFontViewToGlyphSet
f = CurrentFont()

skipExport = f.lib.get("public.skipExportGlyphs", [])

limitFontViewToGlyphSet((gn for gn in f.keys() if gn not in skipExport))
