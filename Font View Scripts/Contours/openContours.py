f = CurrentFont()
f.selectedGlyphNames = [g.name for g in f if g.contours and any([contour.open for contour in g.contours])]
