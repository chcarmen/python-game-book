import sys

import pygame
from pygame.locals import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("Event Handling1")

    font = pygame.font.SysFont(None, 36)

    text0 = ""
    text1 = ""

    while True:
        pygame.event.pump()
        #pygame.event.get()
        #pygame.event.wait()
        #pygame.event.poll()
        #pygame.event.clear()

        # handle mouse input
        buttons = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        text0 = "mouse position: " + str(pos)
        if buttons[0]:
            text0 += "  left button pressed"
        elif buttons[1]:
            text0 += "  middle button pressed"
        elif buttons[2]:
            text0 += "  right button pressed"

        # handle keyboard input
        keys = pygame.key.get_pressed()

        if keys[K_q]:
            sys.exit()
        elif keys[K_a]:
            text1 = "key a pressed"
        elif keys[K_b] and keys[K_c]:
            text1 = "key b and key c pressed"
        else:
            text1 = ""

        # text 0: mouse info
        text0_surface = font.render(text0, True, (255, 0, 0))

        # text 1: keyboard info
        text1_surface = font.render(text1, True, (0, 0, 255))

        # draw and display
        screen.fill((255, 255, 255))
        screen.blit(text0_surface, (10, 50))
        screen.blit(text1_surface, (10, 150))
        pygame.display.flip()


if __name__ == "__main__":
    main()
