#! /usr/bin/env python

# To hide the message of the pygame version
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import time
import datetime
import os
import configparser
import re
import math

import scenes
from scenes.home import HomeScene

#*******************************************************************************************************#
#--------------------------------------- The main app loop -------------------------------#
#*******************************************************************************************************#
def run_RpiRoadbook(width, height,  starting_scene):
    pygame.display.init()
    
    pygame.display.set_caption('RPI Roadbook')
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
run_RpiRoadbook(800, 480, HomeScene())
