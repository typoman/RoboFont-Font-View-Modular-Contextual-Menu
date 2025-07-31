import AppKit
import mojo.UI

def limitFontViewToGlyphSet(gl):
	query_text = 'Name in {"%s"}' % '", "'.join(gl)
	query = AppKit.NSPredicate.predicateWithFormat_(query_text)
	mojo.UI.CurrentFontWindow().getGlyphCollection().setQuery(query)

if __name__ == '__main__':
	f = CurrentFont()
	limitFontViewToGlyphSet(f.selectedGlyphNames)
