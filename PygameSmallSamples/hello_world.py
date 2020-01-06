import sys

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Hello World")

    logo = pygame.image.load("pygame.png")
    logo_rect = logo.get_rect()
    logo_rect.center = (400, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(logo, logo_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
