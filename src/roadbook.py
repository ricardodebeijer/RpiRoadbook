#! /usr/bin/env python

import contextlib
import colors
import config
import system
import time
from system import system_cpu_load, system_temperature
import scenes
# Import the screens/scenes
from scenes.home import HomeScene
from scenes.odo import OdoScene
from scenes.maintenance import MaintenanceScene

# To hide the message of the pygame version
with contextlib.redirect_stdout(None):
    import pygame

import pygame.freetype
# The frame rate
fps = 5

# System variables
temperature = -1
cpu = -1

# Theme Light (is white, for day use ) or Dark (is black, for night use)
theme = 'Dark'

# Screen orientation: either Portrait or Landscape
orientation = 'Landscape'

# Language settings
language = 'EN'

# Settings for app
settings = {}

# Pygame font
font = None


def select_screen(active_scene, character):
    if character == '1':
        print('To home')
        active_scene.SwitchToScene(HomeScene())
    elif character == '2':
        print('To odo')
        active_scene.SwitchToScene(OdoScene())
    elif character == '3':
        print('To maintenance')
        active_scene.SwitchToScene(MaintenanceScene())
    else:
        print('No screen set for character: {}'.format(
            character))

# Main app loop


def run_RpiRoadbook(width, height, starting_scene):
    # Read config
    settings = config.get_config()
    orientation = settings['orientation']
    language = settings['language']
    theme = settings['theme']

    print('orientation: {}, language: {}, theme: {}'.format(
        orientation, language, theme))

    # Init pygame
    pygame.init()
    # Set the caption of the display
    pygame.display.set_caption('RPI Roadbook')
    # Create the screen with the given width and height
    if orientation == 'Landscape':
        screen = pygame.display.set_mode((width, height))
    else:
        screen = pygame.display.set_mode((height, width))

    # Setup font
    font = pygame.freetype.SysFont(None,24)
   
    # Hide the mouse
    # pygame.mouse.set_visible(False)
    # Testing: show mouse
    pygame.mouse.set_visible(True)

    # Check theming
    if theme == 'Light':
        pygame.display.get_surface().fill(colors.WHITE)
    else:
        pygame.display.get_surface().fill(colors.BLACK)

    # Save the screen
    active_scene = starting_scene

    # Update screen
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
        interval = 10
        if time.time() - interval > t_sys:
            t_sys = time.time()
            system_temperature()
            system_cpu_load()
            print('{} second interval: {}. CPU load: {}, Temperature: {}'.format(
                interval, t_sys, cpu, temperature))
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
        # Check all the filered events
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
                        # If its valid character, select a screen
                        select_screen(active_scene, event.unicode)
                    elif hasattr(event, 'key'):
                        if event.key != 0:
                            print('Key pressed: {}.'.format(event.key))

        if theme == 'Light':
            pygame.display.get_surface().fill(colors.WHITE)
        else:
            pygame.display.get_surface().fill(colors.BLACK)
        
        # Send the filtered events to the scene
        active_scene.ProcessInput(filtered_events, pressed_keys)
        # Render the scene and pygame display
        active_scene.Render(screen, font)
        # Set the next screen if any is set
        active_scene = active_scene.next
        pygame.display.update()
        # Update clock
        clock.tick(fps)


# Main starting point
print('Starting roadbook, press ESC to exit')
run_RpiRoadbook(800, 480, HomeScene())
