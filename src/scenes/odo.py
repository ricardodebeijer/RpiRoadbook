import contextlib

import scenes
from scenes.base import BaseScene

with contextlib.redirect_stdout(None):
    import pygame

# Odo scene
class OdoScene(BaseScene):
    def __init__(self, fname=''):
        BaseScene.__init__(self)
        self.next = self
        self.filename = fname
        self.title = 'Odo'

    def ProcessInput(self, events, pressed_keys):
        pass

    # def Update(self):
    #     pass

    # def Render(self, screen):
    #     print('Render Odo')
    #     super().Render(screen)
