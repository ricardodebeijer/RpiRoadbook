from colors import RED, GRAY
import colors
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


class rb_widget():
    def __init__(self, widget_layouts, layout='1', widget=0):
        global angle, widget_iscountdown
        self.widget_order = widget
        widget_iscountdown = False
        angle = 0 if layout in ('0', '1', '2', '3', '4', '11', 'Z') else 90
        a = widget_layouts[layout][widget]
        # setup_alphabet(a['label_font'])
        # setup_alphabet(a['value_font'])
        # setup_alphabet(a['unit_font'])
        # setup_alphabet(a['selected_font'])

        self.selected_font = a['selected_font']
        self.label_font = a['label_font']
        self.value_font = a['value_font']
        self.unit_font = a['unit_font']
        self.over_font = a['over_font']
        self.inside_font = a['inside_font']

        (self.x, self.y) = (a['x'], a['y'])
        (self.w, self.h) = (a['w'], a['h'])
        (self.x1, self.y1) = (a['x1'], a['y1'])
        (self.x2, self.y2) = (a['x2'], a['y2'])
        (self.x3, self.y3) = (a['x3'], a['y3'])
        self.selected = False

    def upup(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def downdown(self):
        pass

    def ok(self, current_widget, nb_widgets):
        current_widget += 1
        if current_widget > nb_widgets:
            current_widget = 0

    def reset(self):
        pass

    def update(self):
        pass

    def render(self, scr):
        if self.selected:
            r = pygame.draw.rect(scr, RED, (self.x, self.y, self.w, self.h), 1)
        else:
            r = pygame.draw.rect(
                scr, GRAY, (self.x, self.y, self.w, self.h), 1)
        pygame.display.update(r)

    def select(self):
        global widget_iscountdown
        self.selected = True
        widget_iscountdown = False

    def deselect(self):
        self.selected = False
