from mojo.UI import limitFontViewToGlyphSet
f = CurrentFont()

skipExport = f.lib.get("public.skipExportGlyphs", [])

limitFontViewToGlyphSet(skipExport)
