import contextlib
with contextlib.redirect_stdout(None):
    import pygame

# The template used for other scenes/screens to extend from
class BaseScene:
    def __init__(self, fname=''):
        self.next = self
        self.filename = fname
        self.title = 'Base'

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    # def Update(self):
    #     print("uh-oh, you didn't override this in the child class")

    def Render(self, screen, font):
        pygame.display.set_caption('RPI Roadbook - {}'.format(self.title))
        text_surface, rect = font.render('Current screen: {}'.format(self.title), (0, 0, 0))
        screen.blit(text_surface, (0, 0))

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
