#! /usr/bin/env python

# To hide the message of the pygame version
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

# For display on the framebuffer
import time
import datetime
import os
import configparser
import re
import math

#*******************************************************************************************************#
#---------------------------------------- The class / screen template  -------------------------------#
#*******************************************************************************************************#
class SceneBase:
    def __init__(self, fname = ''):
        self.next = self
        self.filename = fname
        #pygame.display.get_surface().fill((0,0,0))
        #pygame.display.update()

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

#*******************************************************************************************************#
#---------------------------------------- The No Roadbooks present section --------------------------#
#*******************************************************************************************************#
class NoneScene(SceneBase):
    def __init__(self, fname = ''):
        SceneBase.__init__(self)
        self.next = self
        self.filename = fname

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.constants.QUIT:
                self.Terminate()

    def Update(self):
        pass

    def Render(self, screen):
        pass

#*******************************************************************************************************#
#--------------------------------------- The main app loop -------------------------------#
#*******************************************************************************************************#
def run_RpiRoadbook(width, height,  starting_scene):
    pygame.display.init()

    screen = pygame.display.set_mode((width, height))

    active_scene = starting_scene

    while active_scene != None:
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.constants.QUIT:
                quit_attempt = True
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_ESCAPE:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.Update()
        active_scene.Render(screen)
        active_scene = active_scene.next
        pygame.display.update()

#*******************************************************************************************************#
#------------------------- Definition of Flask routing  -----------------------------------------------#
#*******************************************************************************************************#
print('Starting roadbook, press ESC to exit')
run_RpiRoadbook(800, 480, NoneScene())
