# menuTitle: Skip Export - Mass Toggle Selected
# source: https://gist.github.com/ryanbugden/7f20d42ef45ed0d657ad4f744bf9a373#file-toggle_nonexport-py

'''
Go through all selected glyphs, and change whether they are set to export or non-export, based on the opposite of the state of the first glyph.

2021.10.28
'''

f = CurrentFont()

# check to see if the public.skipExportGlyphs key is in the lib. if not, make it
try:
    # stephen’s duplicate-clean-up step, but sandwiched in here
    f.lib['public.skipExportGlyphs'] = list(
        set(f.lib['public.skipExportGlyphs']))
except KeyError:
    f.lib['public.skipExportGlyphs'] = []

# starting empty lists to print out later when filled
non_exp = []
exp = []

# check first glyph of selection, and plan to set everything to the opposite state of that
if f.selectedGlyphNames[0] in f.lib['public.skipExportGlyphs']:
    make_nonExp = False
else:
    make_nonExp = True

# let's change states
for g_name in f.selectedGlyphNames:  # f.selection is deprecated

    g = f[g_name]

    if make_nonExp is True:
        if g_name not in f.lib['public.skipExportGlyphs']:
            f.lib['public.skipExportGlyphs'].append(g_name)
            non_exp.append(g_name)

    elif make_nonExp is False:
        if g_name in f.lib['public.skipExportGlyphs']:
            f.lib['public.skipExportGlyphs'].remove(g_name)
            exp.append(g_name)

    g.changed()  # officially "updates" the glyph. g.update() is deprecated.
    # doing the above on the "glyph" level should help it update in the UI

# print results
if exp != []:
    print("NEWLY SET TO EXPORT:")
    print(exp)

if non_exp != []:
    print("NEWLY SET TO NON-EXPORT:")
    print(non_exp)
