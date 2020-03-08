import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import colors
from colors import *

import globals

# Font style index
WHITE_25 = 0
WHITE_50 = 1
WHITE_75 = 2
WHITE_100 = 3
WHITE_200 = 4
WHITE_25_inv = 5
WHITE_25_inv = 5
WHITE_50_inv = 6
RED_25 = 7
RED_25_inv = 8
GREEN_25 = 9
GRAY75 = 10
WHITE_80 = 11
WHITE_20 = 12
RED_20 = 13
WHITE_3 = 14
WHITE_4 = 15
WHITE_5 = 16
RED_3 = 17
RED_4 = 18
RED_5 = 19
GREEN_3 = 20
GREEN_4 = 21
GREEN_5 = 22
WHITE_20_inv = 23
WHITE_3_inv = 24
WHITE_4_inv = 25
WHITE_5_inv = 26

# Font size for each style
SALPHA = {
    WHITE_25: 25,
    WHITE_50: 50,
    WHITE_75: 75,
    WHITE_100: 100,
    WHITE_200: 200,
    WHITE_25_inv: 25,
    WHITE_50_inv: 50,
    RED_25: 25,
    RED_25_inv: 25,
    GREEN_25: 25,
    GRAY75: 75,
    WHITE_80: 80,
    WHITE_20: 20,
    WHITE_20_inv: 20,
    RED_20: 20,
    WHITE_3: 90,
    WHITE_3_inv: 90,
    WHITE_4: 59,
    WHITE_4_inv: 59,
    WHITE_5: 45,
    WHITE_5_inv: 45,
    RED_3: 90,
    RED_4: 59,
    RED_5: 45,
    GREEN_3: 90,
    GREEN_4: 59,
    GREEN_5: 45
}


def load_font(myfont, police=WHITE_25):
    # Loading a font if not yet cached
    if not police in myfont:
        if police in SALPHA:
            myfont[police] = pygame.font.SysFont("cantarell", SALPHA[police])
        else:
            myfont[police] = pygame.font.SysFont("cantarell", 25)


def setup_alphabet(alphabet,alphabet_size_x,alphabet_size_y,myfont,angle,theme,police=WHITE_25):
    # Load the requested font
    load_font(myfont,police)
    # All allowed character to be printed
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    # Mapping of fonts to styles (day/night + foreground+background)
    light_foreground = {WHITE_25: BLACK,  WHITE_50: BLACK,  WHITE_75: BLACK,  WHITE_100: BLACK,  WHITE_200: BLACK,  WHITE_25_inv: WHITE, WHITE_50_inv: WHITE, RED_25: RED, RED_25_inv: WHITE, GREEN_25: BLUE,  GRAY75: GRAY, WHITE_80: BLACK,
               WHITE_20: BLACK, RED_20: RED, WHITE_3: BLACK, WHITE_4: BLACK, WHITE_5: BLACK, RED_3: RED, RED_4: RED, RED_5: RED, GREEN_3: GREEN, GREEN_4: GREEN, GREEN_5: GREEN, WHITE_20_inv: WHITE, WHITE_3_inv: WHITE, WHITE_4_inv: WHITE, WHITE_5_inv: WHITE}
    light_background = {WHITE_25: WHITE, WHITE_50: WHITE, WHITE_75: WHITE, WHITE_100: WHITE, WHITE_200: WHITE, WHITE_25_inv: BLACK,  WHITE_50_inv: BLACK,  RED_25: WHITE, RED_25_inv: RED, GREEN_25: WHITE, GRAY75: WHITE, WHITE_80: WHITE, WHITE_20: WHITE,
               RED_20: WHITE, WHITE_3: WHITE, WHITE_4: WHITE, WHITE_5: WHITE, RED_3: WHITE, RED_4: WHITE, RED_5: WHITE, GREEN_3: WHITE, GREEN_4: WHITE, GREEN_5: WHITE, WHITE_20_inv: BLACK, WHITE_3_inv: BLACK, WHITE_4_inv: BLACK, WHITE_5_inv: BLACK}
    night_foreground = {WHITE_25: YELLOW, WHITE_50: YELLOW, WHITE_75: YELLOW, WHITE_100: YELLOW, WHITE_200: YELLOW, WHITE_25_inv: BLACK,  WHITE_50_inv: BLACK,  RED_25: RED, RED_25_inv: RED,  GREEN_25: GREEN,  GRAY75: GRAY, WHITE_80: YELLOW, WHITE_20: YELLOW,
               RED_20: YELLOW, WHITE_3: YELLOW, WHITE_4: YELLOW, WHITE_5: YELLOW, RED_3: RED, RED_4: RED, RED_5: RED, GREEN_3: GREEN, GREEN_4: GREEN, GREEN_5: GREEN, WHITE_20_inv: BLACK, WHITE_3_inv: BLACK, WHITE_4_inv: BLACK, WHITE_5_inv: BLACK}
    night_background = {WHITE_25: BLACK,  WHITE_50: BLACK,  WHITE_75: BLACK,  WHITE_100: BLACK,  WHITE_200: BLACK,  WHITE_25_inv: YELLOW, WHITE_50_inv: YELLOW, RED_25: BLACK,  RED_25_inv: YELLOW, GREEN_25: BLACK,  GRAY75: BLACK, WHITE_80: BLACK, WHITE_20: BLACK,
               RED_20: BLACK, WHITE_3: BLACK, WHITE_4: BLACK, WHITE_5: BLACK, RED_3: BLACK, RED_4: BLACK, RED_5: BLACK, GREEN_3: BLACK, GREEN_4: BLACK, GREEN_5: BLACK, WHITE_20_inv: YELLOW, WHITE_3_inv: YELLOW, WHITE_4_inv: YELLOW, WHITE_5_inv: YELLOW}

    if theme:
        if angle == 90:
            for i in printable:
                alphabet[(i, police, angle)] = pygame.transform.rotate(
                    myfont[police].render(i, 1, light_foreground[police], light_background[police]), 90)
                alphabet_size_x[(i, police, angle)] = 0
                alphabet_size_y[(i, police, angle)] = - \
                    alphabet[(i, police, angle)].get_size()[1]
        else:
            for i in printable:
                alphabet[(i, police, angle)] = myfont[police].render(
                    i, 1, light_foreground[police], light_background[police])
                alphabet_size_x[(i, police, angle)] = alphabet[(
                    i, police, angle)].get_size()[0]
                alphabet_size_y[(i, police, angle)] = 0
        alphabet[(' ', police, angle)].fill(light_background[police])
    else:
        if angle == 90:
            for i in printable:
                alphabet[(i, police, angle)] = pygame.transform.rotate(
                    myfont[police].render(i, 1, night_foreground[police], night_background[police]), 90)
                alphabet_size_x[(i, police, angle)] = 0
                alphabet_size_y[(i, police, angle)] = - \
                    alphabet[(i, police, angle)].get_size()[1]
        else:
            for i in printable:
                alphabet[(i, police, angle)] = myfont[police].render(
                    i, 1, night_foreground[police], night_background[police])
                alphabet_size_x[(i, police, angle)] = alphabet[(
                    i, police, angle)].get_size()[0]
                alphabet_size_y[(i, police, angle)] = 0
        alphabet[(' ', police, angle)].fill(night_background[police])
