import sys
from math import pi

import pygame


BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Draw Shapes")

    while True:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        # draw a line
        pygame.draw.line(screen, RED, (20, 80), (160, 0))

        # draw an anti-aliased line
        pygame.draw.aaline(screen, GREEN, (20, 100), (160, 20))

        # draw lines
        pygame.draw.lines(screen, BLACK, False, ((20, 140), (50, 180), (160, 60), (220, 80)))

        # draw closed lines
        pygame.draw.lines(screen, RED, True, ((20, 160), (50, 200), (160, 80), (220, 100)))

        # draw anti-aliased closed lines
        pygame.draw.aalines(screen, GREEN, True, ((20, 180), (50, 220), (160, 100), (220, 120)))

        # draw a triangle
        pygame.draw.lines(screen, RED, True, ((30, 320), (110, 200), (190, 320)), 2)

        # draw a rectangle
        pygame.draw.rect(screen, BLACK, (30, 380, 160, 40), 1)

        # draw a rectangle with solid color fill
        pygame.draw.rect(screen, BLACK, (30, 440, 160, 40))

        # draw a polygon
        pygame.draw.polygon(screen, BLUE, ((20, 580), (60, 500), (100, 580)), 2)

        # draw a polygon with solid color fill
        pygame.draw.polygon(screen, BLUE, ((120, 580), (160, 500), (200, 580)))

        # draw a circle
        pygame.draw.circle(screen, GREEN, (360, 60), 60, 1)

        # draw a circle with solid color fill
        pygame.draw.circle(screen, GREEN, (500, 60), 60)

        # draw an ellipse
        pygame.draw.ellipse(screen, RED, (330, 160, 60, 180), 2)

        # draw an ellipse with solid color fill
        pygame.draw.ellipse(screen, RED, (470, 160, 60, 180))

        # draw an arc
        pygame.draw.arc(screen, BLACK, (310, 400, 120, 100), pi, 2*pi, 2)

        # draw another arc
        pygame.draw.arc(screen, BLUE, (430, 400, 120, 100), 0, pi, 2)

        pygame.display.flip()


if __name__ == "__main__":
    main()
