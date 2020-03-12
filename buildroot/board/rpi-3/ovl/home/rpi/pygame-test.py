import pygame
from pygame.locals import *

pygame.display.init()

(width,height) = (800,480)
screen = pygame.display.set_mode((width, height))

pygame.font.init()
font = pygame.font.SysFont("cantarell", 24)

text = font.render('Text to show',True,(200,0,0))

while True:
    # clear the screen
    screen.fill((0, 0, 0))
    # place the image
    # screen.blit(image, (0, 0))
    # the the image
    screen.blit(text,(10,450))
    # render/update the display
    pygame.display.flip()