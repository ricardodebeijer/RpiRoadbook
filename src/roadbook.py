#! /usr/bin/env python

import contextlib
import datetime
import math
import os
import re
import time

import colors
# Import config
import config
# Import fonts used
import fonts
from fonts import setup_alphabet
# Import colors used in the scenes
import scenes
import system
# Import the screens/scenes
from scenes.home import HomeScene
# Import system methods for getting cpu load and temperature
from system import system_cpu_load, system_temperature

# To hide the message of the pygame version
with contextlib.redirect_stdout(None):
    import pygame

# Text shown on screen in label dict
labels = {}

# The frame rate
fps = 5

# System variables
temperature = -1
cpu = -1

# Font related
alphabet = {}
alphabet_size_x = {}
alphabet_size_y = {}

myfont = {}

# Theme Light (is white, for day use ) or Dark (is black, for night use)
theme = 'Dark'

# Screen orientation: either Portrait or Landscape
orientation = 'Landscape'

# Language settings
language = 'EN'

# Settings for app
settings = {}

labels = {}
old_labels = {}

#--------------------------------------------------------------------------------- ----------#
#------------------------------ Widget organization ------------------------------------#
#---------------------------------------------------------------------------------- ---------#
current_screen = 1
current_widget = 0
old_widget = 1
widgets = {}
nb_widgets = 1
widget_isselected = False
widget_iscountdown = False
widget_select_t = 0
default_widget = 7

#------------------------------ Definition of widgets ---------------------------------------------#
widget_presets = {
    'pajra1' : {'orientation':'Landscape','theme':'Light','mode':'Rally','layout':'1'},
    'pajra2' : {'orientation':'Landscape','theme':'Light','mode':'Rally','layout':'2'},
    'pajra3' : {'orientation':'Landscape','theme':'Light','mode':'Rally','layout':'3'},
    'pajra4' : {'orientation':'Landscape','theme':'Light','mode':'Rally','layout':'4'},
    'panra1' : {'orientation':'Landscape','theme':'Dark','mode':'Rally','layout':'1'},
    'panra2' : {'orientation':'Landscape','theme':'Dark','mode':'Rally','layout':'2'},
    'panra3' : {'orientation':'Landscape','theme':'Dark','mode':'Rally','layout':'3'},
    'panra4' : {'orientation':'Landscape','theme':'Dark','mode':'Rally','layout':'4'},
    'pojra1' : {'orientation':'Portrait','theme':'Light','mode':'Rally','layout':'5'},
    'pojra2' : {'orientation':'Portrait','theme':'Light','mode':'Rally','layout':'6'},
    'one' : {'orientation':'Portrait','theme':'Light','mode':'Rally','layout':'7'},
    'pojra4' : {'orientation':'Portrait','theme':'Light','mode':'Rally','layout':'8'},
    'pojra5' : {'orientation':'Portrait','theme':'Light','mode':'Rally','layout':'9'},
    'pojra6' : {'orientation':'Portrait','theme':'Light','mode':'Rally','layout':'10'},
    'ponra1' : {'orientation':'Portrait','theme':'Dark','mode':'Rally','layout':'5'},
    'ponra2' : {'orientation':'Portrait','theme':'Dark','mode':'Rally','layout':'6'},
    'ponra3' : {'orientation':'Portrait','theme':'Dark','mode':'Rally','layout':'7'},
    'ponra4' : {'orientation':'Portrait','theme':'Dark','mode':'Rally','layout':'8'},
    'ponra5' : {'orientation':'Portrait','theme':'Dark','mode':'Rally','layout':'9'},
    'ponra6' : {'orientation':'Portrait','theme':'Dark','mode':'Rally','layout':'10'},
    'pajro1' : {'orientation':'Landscape','theme':'Light','mode':'Route','layout':'11'},
    'panro1' : {'orientation':'Landscape','theme':'Dark','mode':'Route','layout':'11'},
    'pojro1' : {'orientation':'Portrait','theme':'Light','mode':'Route','layout':'12'},
    'ponro1' : {'orientation':'Portrait','theme':'Dark','mode':'Route','layout':'12'},
    'pajzz' : {'orientation':'Landscape','theme':'Light','mode':'Zoom','layout':'0'},
    'pojzz' : {'orientation':'Portrait','theme':'Light','mode':'Zoom','layout':'00'},
}

widget_sizes = {
    # Number of fields for landscape rally formats
    '1' : 3,
    '2' : 4,
    '3' : 5,
    '4' : 6,
    # Number of fields for portrait rally formats
    '5' : 2,
    '6' : 3,
    '7' : 4,
    '8' : 1,
    '9' : 2,
    '10': 3,
    # Number of fields for landscape and portrait single meters
    '11': 5,
    '12': 5,
    # For the zoom
    '0' : 0,
    '00': 0
    }

from fonts import RED_3, RED_20,RED_25,WHITE_20,WHITE_3, WHITE_4,WHITE_25,GREEN_3,GREEN_4,GREEN_25, WHITE_20_inv,WHITE_3_inv,RED_4, WHITE_4_inv,WHITE_5, RED_5,GREEN_5,WHITE_5_inv, WHITE_25_inv,WHITE_200, WHITE_100

widget_layouts = {
    '0' : [
        {'x':500,'y':0,'w':300,'h':30,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':0,'y1':1,'x2':120,'y2':1,'x3':240,'y3':1}],
    '00' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_20,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100}],
    '1' : [
        {'x':500,'y':0,'w':300,'h':30,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':1,'x2':120,'y2':1,'x3':240,'y3':1},
        {'x':500,'y':30,'w':300,'h':150,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':5,'y1':115,'x2':15,'y2':1,'x3':240,'y3':115},
        {'x':500,'y':180,'w':300,'h':150,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':5,'y1':115,'x2':15,'y2':1,'x3':240,'y3':115},
        {'x':500,'y':330,'w':300,'h':150,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':5,'y1':115,'x2':15,'y2':1,'x3':240,'y3':115}],
    '2' : [
        {'x':500,'y':0,'w':300,'h':30,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':1,'x2':120,'y2':1,'x3':240,'y3':1},
        {'x':500,'y':30,'w':300,'h':110,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':75,'x2':100,'y2':1,'x3':240,'y3':75},
        {'x':500,'y':140,'w':300,'h':110,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':75,'x2':100,'y2':1,'x3':240,'y3':75},
        {'x':500,'y':250,'w':300,'h':110,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':75,'x2':100,'y2':1,'x3':240,'y3':75},
        {'x':500,'y':360,'w':300,'h':110,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':75,'x2':100,'y2':1,'x3':240,'y3':75}],
    '3' : [
        {'x':500,'y':0,'w':300,'h':30,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':1,'x2':120,'y2':1,'x3':240,'y3':1},
        {'x':500,'y':30,'w':300,'h':90,'label_font':RED_25,'value_font':WHITE_5,'unit_font':WHITE_25,'over_font':RED_5,'inside_font':GREEN_5,'selected_font':WHITE_5_inv,'x1':150,'y1':1,'x2':5,'y2':20,'x3':150,'y3':40},
        {'x':500,'y':120,'w':300,'h':90,'label_font':RED_25,'value_font':WHITE_5,'unit_font':WHITE_25,'over_font':RED_5,'inside_font':GREEN_5,'selected_font':WHITE_5_inv,'x1':150,'y1':1,'x2':5,'y2':20,'x3':150,'y3':40},
        {'x':500,'y':210,'w':300,'h':90,'label_font':RED_25,'value_font':WHITE_5,'unit_font':WHITE_25,'over_font':RED_5,'inside_font':GREEN_5,'selected_font':WHITE_5_inv,'x1':150,'y1':1,'x2':5,'y2':20,'x3':150,'y3':40},
        {'x':500,'y':300,'w':300,'h':90,'label_font':RED_25,'value_font':WHITE_5,'unit_font':WHITE_25,'over_font':RED_5,'inside_font':GREEN_5,'selected_font':WHITE_5_inv,'x1':150,'y1':1,'x2':5,'y2':20,'x3':150,'y3':40},
        {'x':500,'y':390,'w':300,'h':90,'label_font':RED_25,'value_font':WHITE_5,'unit_font':WHITE_25,'over_font':RED_5,'inside_font':GREEN_5,'selected_font':WHITE_5_inv,'x1':150,'y1':1,'x2':5,'y2':20,'x3':150,'y3':40}],
    '4' : [
        {'x':500,'y':0,'w':300,'h':30,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':1,'x2':120,'y2':1,'x3':240,'y3':1},
        {'x':500,'y':30,'w':300,'h':75,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':25,'x2':155,'y2':25,'x3':240,'y3':25},
        {'x':500,'y':105,'w':300,'h':75,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':25,'x2':155,'y2':25,'x3':240,'y3':25},
        {'x':500,'y':180,'w':300,'h':75,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':25,'x2':155,'y2':25,'x3':240,'y3':25},
        {'x':500,'y':255,'w':300,'h':75,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':25,'x2':155,'y2':25,'x3':240,'y3':25},
        {'x':500,'y':330,'w':300,'h':75,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':25,'x2':155,'y2':25,'x3':240,'y3':25},
        {'x':500,'y':405,'w':300,'h':75,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':25,'x2':155,'y2':25,'x3':240,'y3':25}],
    '5' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':0,'w':150,'h':480,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':1,'y1':480,'x2':20,'y2':380,'x3':1,'y3':70},
        {'x':180,'y':0,'w':150,'h':480,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':1,'y1':480,'x2':20,'y2':380,'x3':1,'y3':70}],
    '6' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':0,'w':150,'h':480,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':1,'y1':475,'x2':1,'y2':320,'x3':1,'y3':70},
        {'x':180,'y':240,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70},
        {'x':180,'y':0,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70}],
    '7' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':240,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70},
        {'x':30,'y':0,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70},
        {'x':180,'y':240,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70},
        {'x':180,'y':0,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70}],
    '8' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':0,'w':150,'h':480,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':1,'y1':475,'x2':30,'y2':320,'x3':1,'y3':70}],
    '9' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':240,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70},
        {'x':30,'y':0,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70}],
    '10' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':240,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':110,'y3':70},
        {'x':30,'y':0,'w':75,'h':240,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':35,'y3':70},
        {'x':105,'y':0,'w':75,'h':240,'label_font':RED_25,'value_font':WHITE_25,'unit_font':WHITE_25,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_25_inv,'x1':1,'y1':235,'x2':35,'y2':200,'x3':35,'y3':70}],
    '11' : [
        {'x':0,'y':0,'w':300,'h':30,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':1,'x2':120,'y2':1,'x3':240,'y3':1},
        {'x':0,'y':30,'w':300,'h':150,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':5,'y1':115,'x2':15,'y2':1,'x3':240,'y3':115},
        {'x':0,'y':180,'w':300,'h':150,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':5,'y1':115,'x2':15,'y2':1,'x3':240,'y3':115},
        {'x':0,'y':330,'w':300,'h':150,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':5,'y1':115,'x2':15,'y2':1,'x3':240,'y3':115},
        {'x':300,'y':0,'w':500,'h':300,'label_font':RED_25,'value_font':WHITE_200,'unit_font':WHITE_25,'over_font':WHITE_200,'inside_font':WHITE_200,'selected_font':WHITE_200,'x1':5,'y1':265,'x2':100,'y2':1,'x3':440,'y3':265},
        {'x':300,'y':300,'w':500,'h':180,'label_font':RED_25,'value_font':WHITE_100,'unit_font':WHITE_25,'over_font':WHITE_100,'inside_font':WHITE_100,'selected_font':WHITE_200,'x1':5,'y1':130,'x2':100,'y2':1,'x3':440,'y3':130}],
    '12' : [
        {'x':0,'y':0,'w':30,'h':480,'label_font':RED_20,'value_font':WHITE_20,'unit_font':RED_20,'over_font':RED_25,'inside_font':GREEN_25,'selected_font':WHITE_20_inv,'x1':1,'y1':400,'x2':1,'y2':280,'x3':1,'y3':100},
        {'x':30,'y':0,'w':150,'h':480,'label_font':RED_25,'value_font':WHITE_3,'unit_font':WHITE_25,'over_font':RED_3,'inside_font':GREEN_3,'selected_font':WHITE_3_inv,'x1':1,'y1':475,'x2':35,'y2':380,'x3':1,'y3':70},
        {'x':180,'y':240,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':30,'y2':200,'x3':100,'y3':70},
        {'x':180,'y':0,'w':150,'h':240,'label_font':RED_25,'value_font':WHITE_4,'unit_font':WHITE_25,'over_font':RED_4,'inside_font':GREEN_4,'selected_font':WHITE_4_inv,'x1':1,'y1':235,'x2':30,'y2':200,'x3':100,'y3':70},
        {'x':330,'y':0,'w':300,'h':480,'label_font':RED_25,'value_font':WHITE_200,'unit_font':WHITE_25,'over_font':WHITE_200,'inside_font':WHITE_200,'selected_font':WHITE_200,'x1':1,'y1':475,'x2':40,'y2':400,'x3':1,'y3':70},
        {'x':630,'y':0,'w':170,'h':480,'label_font':RED_25,'value_font':WHITE_100,'unit_font':WHITE_25,'over_font':WHITE_100,'inside_font':WHITE_200,'selected_font':WHITE_200,'x1':1,'y1':480,'x2':40,'y2':400,'x3':1,'y3':70}],
    'Z' : [
        {'x':400,'y':0,'w':400,'h':120,'label_font':RED_25,'value_font':WHITE_100,'unit_font':WHITE_25,'over_font':WHITE_100,'inside_font':WHITE_100,'selected_font':WHITE_100,'x1':1,'y1':1,'x2':70,'y2':1,'x3':1,'y3':80},
    ],
}

# Main app loop
def run_RpiRoadbook(width, height,  starting_scene):
    global fps

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
    # Save the screen
    active_scene = starting_scene

    # Check theming
    if theme == 'Light':
        pygame.display.get_surface().fill(colors.WHITE)
    else:
        pygame.display.get_surface().fill(colors.BLACK)

    # Update setup_alphabet
    setup_alphabet(alphabet, alphabet_size_x,
                   alphabet_size_y, myfont, theme, 90)

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
