# import contextlib

# import scenes
# from scenes.base import BaseScene

# with contextlib.redirect_stdout(None):
#     import pygame

# # Home scene
# class HomeScene(BaseScene):
#     def __init__(self, fname=''):
#         BaseScene.__init__(self)
#         self.next = self
#         self.filename = fname

#     def ProcessInput(self, events, pressed_keys):
#         for event in events:
#             if event.type == pygame.constants.QUIT:
#                 self.Terminate()

#     def Update(self):
#         pass

#     def Render(self, screen):
#         pass
