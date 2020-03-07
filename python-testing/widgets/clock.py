import widgets
from widgets.widget import rb_widget

import time

import colors
from colors import GRAY


class time_widget(rb_widget):
    def __init__(self, angle=0, layout='1', widget=0):
        rb_widget.__init__(self, layout, widget)
        self.angle = angle

    def update(self):
        self.now = time.localtime()

    def render(self, scr, pygame):
        # blit.blit_text(scr, (" Time"), (self.x+self.x1,
        #                             self.y+self.y1), self.label_font, self.angle)
        # if self.selected:
        #     blit.blit_text(scr, '{:02d}:{:02d}'.format(self.now.tm_hour, self.now.tm_min),
        #               (self.x+self.x2, self.y+self.y2), self.selected_font, self.angle)
        # else:
        #     blit.blit_text(scr, '{:02d}:{:02d}'.format(self.now.tm_hour, self.now.tm_min),
        #               (self.x+self.x2, self.y+self.y2), self.value_font, self.angle)
        # blit.blit_text(scr, '{:02.0f} '.format(self.now.tm_sec),
        #           (self.x+self.x3, self.y+self.y3), self.unit_font, self.angle)
        r = pygame.draw.rect(scr, GRAY, (self.x, self.y, self.w, self.h), 1)
        pygame.display.update(r)
