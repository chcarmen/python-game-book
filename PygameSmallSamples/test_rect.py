import sys

import pygame


def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Rect Test")

    rect0 = (100, 0, 300, 50)
    rect1 = pygame.Rect(100, 60, 300, 160)
    rect2 = rect1.inflate(-40, -40)

    print(rect1.collidepoint((220, 100)))
    print(rect1.colliderect(rect0))
    print(rect1.collidelist([rect0, rect2]))

    dog = pygame.image.load("dog.png").convert_alpha()
    rect3 = dog.get_rect()
    rect3.center = 40, 260

    speed = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        # use quadruples as Rect parameter
        pygame.draw.rect(screen, (255, 193, 37), rect0)

        # use Rect object as Rect parameter
        pygame.draw.rect(screen, (255, 0, 0), rect1)

        # use Rect object as Rect parameter
        pygame.draw.rect(screen, (230, 230, 230), rect2)

        # move dog
        rect3.move_ip(speed, 0)
        if not screen.get_rect().contains(rect3):
            speed = -speed

        screen.blit(dog, rect3)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
