from mojo.UI import CurrentFontWindow
import AppKit
import random
from mojo.events import addObserver
from mojo.roboFont import CurrentFont

"""
This code is written by Frank Grishammer.
"""

class Contextual_Menu(object):
    def __init__(self):
        addObserver(
            self,
            '_fontOverviewAdditionContextualMenuItems',
            'fontOverviewAdditionContextualMenuItems')

    def _fontOverviewAdditionContextualMenuItems(self, notification):
        font = CurrentFont()
        if font.selectedGlyphNames:
            myMenuItems = [
                ('Filter same …', [
                    ('mark', self.add_attribute(
                        self.filter_glyph_attribute, font, 'markColor')),
                    ('width', self.add_attribute(
                        self.filter_glyph_attribute, font, 'width')),
                    # ('Unicode range', self.add_attribute(
                    #     self.filter_glyph_attribute, font, 'unicode_range')),
                    ('anchor count', self.add_attribute(
                        self.filter_glyph_attribute, font, 'anchors')),
                    ('anchor names', self.add_attribute(
                        self.filter_glyph_attribute, font, 'anchor_names')),
                    ('component count', self.add_attribute(
                        self.filter_glyph_attribute, font, 'components')),
                    ('contour count', self.add_attribute(
                        self.filter_glyph_attribute, font, 'contours')),
                ]),
                ('Filter …', [
                    ('dependent glyphs', self.filter_dependent),
                    ('L kerning group', self.add_attribute(
                        self.kerning_glyph_group, font, 'L')),
                    ('R kerning group', self.add_attribute(
                        self.kerning_glyph_group, font, 'R')),
                ]),
                ('Select …', [
                    ('non-suffixed base glyphs', self.add_font(
                        self.select_baseglyphs, font)),
                    ('same mark color', self.add_font(
                        self.select_same_mark_color, font)),
                    ('pure composite glyphs', self.add_font(
                        self.select_pure_composites, font)),
                    ('mixed composite glyphs', self.add_font(
                        self.select_mixed_composites, font)),
                ]),
                ('Macro', [
                    ('Select alphanumeric', self.add_font(
                        self.select_alphanumeric, font)),
                    ('Print font', self.print_font),
                    ('Select composites', self.add_font(
                        self.select_composites, font)),
                    ('Mark problems', self.add_font(
                        self.mark_problems, font)),
                    ('Invert selection', self.add_font(
                        self.invert_selection, font)),
                    ('Create OpenType', self.create_opentype),
                ]),
                ('Add alternate', self.add_font(
                    self.make_copy, font)),
                ('Isolate selection', self.add_font(
                    self.isolate, font)),
            ]
            notification["additionContextualMenuItems"].extend(myMenuItems)
        else:
            pass

    def make_query(self, glyph_list):
        query_text = 'Name in {"%s"}' % '", "'.join(glyph_list)
        query = AppKit.NSPredicate.predicateWithFormat_(query_text)
        CurrentFontWindow().getGlyphCollection().setQuery(query)

    def add_attribute(self, func, font, attribute):
        def wrapper(sender):
            func(sender, font, attribute)
        return wrapper

    def add_font(self, func, font):
        def wrapper(sender):
            func(sender, font)
        return wrapper

    def print_font(self, sender):
        print('font')

    def anchor_names(self, glyph):
        return set([a.name for a in glyph.anchors])

    def filter_glyph_attribute(self, sender, font, attribute):
        if len(font.selectedGlyphNames):
            repr_glyph_name = font.selectedGlyphNames[0]
            repr_glyph = font[repr_glyph_name]
            if attribute in ['anchors', 'contours', 'components']:
                repr_attr = getattr(repr_glyph, attribute)
                filter_list = [g.name for g in font if (
                    len(getattr(g, attribute)) == len(repr_attr))]
            elif attribute == 'anchor_names':
                filter_list = [
                    g.name for g in font if
                    self.anchor_names(g) == self.anchor_names(repr_glyph)]
            # elif attribute == 'unicode_range':
            #     print('XXX not implemented')
            else:
                filter_list = [g.name for g in font if (
                    getattr(g, attribute) == getattr(repr_glyph, attribute))]
            self.make_query(filter_list)

    def invert_selection(self, sender, font):
        combined_selection = (
            list(font.selectedGlyphNames)+list(font.templateSelectedGlyphNames))
        all_glyphs = set(
            font.glyphOrder) | set([g.name for g in font.templateGlyphs])
        invertedSelection = all_glyphs - set(combined_selection)
        font.selectedGlyphNames = list(invertedSelection)

    def select_composites(self, sender, font):
        font.selectedGlyphNames = [g.name for g in font if g.components]

    def select_pure_composites(self, sender, font):
        font.selectedGlyphNames = [
            g.name for g in font if g.components and not g.contours]

    def select_mixed_composites(self, sender, font):
        font.selectedGlyphNames = [
            g.name for g in font if g.components and g.contours]

    def create_opentype(self, sender):
        pass

    def new_name(self, gname, alt_index=1):
        return gname.split('.')[0] + '.' + '{:0>2d}'.format(alt_index)

    def isolate(self, sender, font):
        self.make_query(font.selectedGlyphNames)

    def make_copy(self, sender, font):
        for gname in font.selectedGlyphNames:
            old_glyph = font[gname]
            alt_index = 1
            new_name = self.new_name(gname, alt_index)
            while new_name in font.keys():
                alt_index += 1
                new_name = self.new_name(gname, alt_index)
            new_glyph = font.newGlyph(new_name, clear=True)
            for layer in [
                lname for lname in font.layerOrder if lname != 'background'
            ]:
                old_layer_glyph = old_glyph.getLayer(layer)
                new_layer_glyph = new_glyph.getLayer(layer)
                new_layer_glyph.appendGlyph(old_layer_glyph)
                new_layer_glyph.width = old_layer_glyph.width
            # new_glyph.width = old_glyph.width

    def select_alphanumeric(self, sender, font):
        alphanumeric = [ord(ch) for ch in (
            'abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789')]
        font.selectedGlyphNames = [
            g.name for g in font if g.unicode in alphanumeric]

    def select_baseglyphs(self, sender, font):
        font.selectedGlyphNames = [
            gname.split('.')[0] for gname in font.selectedGlyphNames if
            font.selectedGlyphNames]

    def select_same_mark_color(self, sender, font):
        sel_mark = font[font.selectedGlyphNames[0]].markColor
        font.selectedGlyphNames = [
            gname for gname in font.keys() if
            font[gname].markColor == sel_mark]

    def mark_problems(self, sender, font):
        problems = random.sample(
            set(font.glyphOrder), len(font.glyphOrder) // 2)
        font.selectedGlyphNames = problems

    def filter_dependent(self, sender):
        font = CurrentFont()
        component_users = [g for g in font if g.components]
        components_used = {}
        for cu in component_users:
            for c in cu.components:
                components_used.setdefault(c.baseGlyph, []).append(cu.name)

        dependent_glyphs = []
        selection = font.selectedGlyphNames
        dependent_glyphs.extend(selection)
        for gname in selection:
            composite_role = components_used.get(gname, None)
            if composite_role:
                dependent_glyphs.extend(composite_role)
        for dep_gname in dependent_glyphs:
            dependencies = components_used.get(dep_gname)
            if dependencies:
                dependent_glyphs.extend(components_used.get(dep_gname))

        self.make_query(dependent_glyphs)

    def kerning_glyph_group(self, sender, font, side):
        gname = font.selectedGlyphNames[0]
        print('using first selected glyph:', gname)
        containing_groups = font.groups.findGlyph(gname)
        if containing_groups:
            if side == 'L':
                kern_group = next((
                    gr_name for gr_name in containing_groups if
                    gr_name.startswith('public.kern1.')), None)
                if kern_group:
                    self.make_query(font.groups.get(kern_group))
                else:
                    self.make_query([gname])
            elif side == 'R':
                kern_group = next((
                    gr_name for gr_name in containing_groups if
                    gr_name.startswith('public.kern2.')), None)
                if kern_group:
                    self.make_query(font.groups.get(kern_group))
                else:
                    self.make_query([gname])


Contextual_Menu()
