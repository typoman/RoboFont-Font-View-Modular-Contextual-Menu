def selectGlyphsWithSameMarkColorAsCurrentSelection(font):
    sel_mark = font[font.selectedGlyphNames[0]].markColor
    font.selectedGlyphNames = [
        gname for gname in font.keys() if
        font[gname].markColor == sel_mark]

selectGlyphsWithSameMarkColorAsCurrentSelection(CurrentFont())
