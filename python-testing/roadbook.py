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

# Import the screens/scenes
import scenes
from scenes.home import HomeScene

# Import colors used in the scenes
import colors

# Import system methods for getting cpu load and temperature
temperature = -1
cpu = -1
import system
from system import system_cpu_load,system_temperature 

# Text shown on screen in label dict
labels = {} 

# The frame rate
fps = 5

# Main app loop
def run_RpiRoadbook(width, height,  starting_scene):
    global fps
    # Create the pygame display
    pygame.display.init()
    # Set the caption of the display
    pygame.display.set_caption('RPI Roadbook')
    # Setup font for display
    pygame.font.init()
    # Create the screen with the given width and height
    screen = pygame.display.set_mode((width, height))
    # Hide the mouse
    # pygame.mouse.set_visible(False)
    # Testing: show mouse
    pygame.mouse.set_visible(True)
    # Save the screen
    active_scene = starting_scene
    
    day_mode = True
    if day_mode :
        pygame.display.get_surface().fill(colors.WHITE)
    else :
        pygame.display.get_surface().fill(colors.BLACK)
    pygame.display.update()

    # Keep a clock
    clock = pygame.time.Clock()
    # Store system time
    t_sys = time.time()
    
    system_temperature()
    system_cpu_load()
    
    # Main loop: while the active_scene is not set to None, we keep going
    while active_scene != None:
        # Get the keys which got pressed
        pressed_keys = pygame.key.get_pressed()
        # We only check the temperature and the cpu load at the given interval
        interval = 5
        if time.time() - interval > t_sys :
            t_sys = time.time()
            system_temperature()
            system_cpu_load()
            print('{} second interval: {}. CPU load: {}, Temperature: {}'.format(interval, t_sys, cpu,temperature))
        # Store the filtered events in this array
        filtered_events = []
        # Loop trough each event
        for event in pygame.event.get():
            # Flag to indicate if we want to exit/quit the application
            quit_attempt = False
            # If its the QUIT constant, we want to stop
            if event.type == pygame.constants.QUIT:
                quit_attempt = True
            # Else if its the ESC key, we also want to stop
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_ESCAPE:
                    quit_attempt = True
            # If we want to stop: terminate the active scene (sets scene to None, will stop the while loop)
            if quit_attempt:
                active_scene.Terminate()
            else:
                # Else add the event to the array of valid events
                filtered_events.append(event)

        if len(filtered_events) > 0:
            for event in filtered_events:
                if event.type == pygame.constants.MOUSEBUTTONDOWN:
                    if hasattr(event, 'pos'):
                        if hasattr(event, 'button'):
                            print('Mouse clicked at: {}.'.format(event.pos))
                            # print('Mouse event: {}.'.format(event))
                elif event.type == pygame.constants.KEYDOWN:
                    # print('Key?: {}.'.format(event))
                    if hasattr(event, 'unicode') and event.unicode != '':
                        print('Character pressed: {}.'.format(event.unicode))
                    elif hasattr(event, 'key'):
                        if event.key != 0:
                            print('Key pressed: {}.'.format(event.key))
                            
        # Send the filtered events to the scene
        active_scene.ProcessInput(filtered_events, pressed_keys)
        # Update/render the scene and pygame display
        active_scene.Update()
        active_scene.Render(screen)
        active_scene = active_scene.next
        pygame.display.update()
        # Update clock
        clock.tick(fps)

# Main starting point
print('Starting roadbook, press ESC to exit')
run_RpiRoadbook(800, 480, HomeScene())
