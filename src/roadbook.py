#! /usr/bin/env python

import contextlib
import colors
import config
import system
import time
from system import system_cpu_load, system_temperature

# To hide the message of the pygame version
with contextlib.redirect_stdout(None):
    import pygame

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

# Main app loop
def run_RpiRoadbook(width, height):
    # Read config
    settings = config.get_config()
    orientation = settings['orientation']
    language = settings['language']
    theme = settings['theme']

    print('orientation: {}, language: {}, theme: {}'.format(
        orientation, language, theme))

    # Create the pygame display
    pygame.display.init()
    # Set the caption of the display
    pygame.display.set_caption('RPI Roadbook')
    # Setup font for display
    pygame.font.init()
    # Create the screen with the given width and height
    if orientation == 'Landscape':
        screen = pygame.display.set_mode((width, height))
    else:
        screen = pygame.display.set_mode((height, width))

    # Hide the mouse
    # pygame.mouse.set_visible(False)
    # Testing: show mouse
    pygame.mouse.set_visible(True)

    # Check theming
    if theme == 'Light':
        pygame.display.get_surface().fill(colors.WHITE)
    else:
        pygame.display.get_surface().fill(colors.BLACK)


    # Update screen
    pygame.display.update()

    # Keep a clock
    clock = pygame.time.Clock()
    # Store system time
    t_sys = time.time()

    system_temperature()
    system_cpu_load()

    quit = False
    # Main loop: while the active_scene is not set to None, we keep going
    while quit != True:
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
                quit = True
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

        pygame.display.update()
        # Update clock
        clock.tick(fps)


# Main starting point
print('Starting roadbook, press ESC to exit')
run_RpiRoadbook(800, 480)
