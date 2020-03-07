import contextlib

import fonts

with contextlib.redirect_stdout(None):
    import pygame


# Text AA
def blit_text(screen, st, coords, alphabet, alphabet_size_x, alphabet_size_y,  col=fonts.WHITE_25, angle=0):
    if (not angle in (0, 90)):
        angle = 0
    (x, y) = coords
    if angle == 0:
        for i in st:
            r = screen.blit(alphabet[(i, col, angle)], (x, y))
            x += alphabet_size_x[(i, col, angle)]
            y += alphabet_size_y[(i, col, angle)]
            pygame.display.update(r)
    else:
        for i in st:
            x += alphabet_size_x[(i, col, angle)]
            y += alphabet_size_y[(i, col, angle)]
            r = screen.blit(alphabet[(i, col, angle)], (x, y))
            pygame.display.update(r)
