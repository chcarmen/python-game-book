import sys

import pygame


class Dog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image0 = pygame.image.load("dog.png").convert_alpha()
        image1 = pygame.transform.flip(image0, 1, 0)
        mask0 = pygame.mask.from_surface(image0)
        mask1 = pygame.mask.from_surface(image1)

        self.images = [image0, image1]
        self.masks = [mask0, mask1]
        self.image_idx = 1
        self.image = image1
        self.mask = mask1

        self.rect = self.image.get_rect()
        self.rect.center = (50, 270)
        self.speed = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > 500 or self.rect.left < 0:
            self.speed = -self.speed

            self.image_idx = not self.image_idx
            self.image = self.images[self.image_idx]
            self.mask = self.masks[self.image_idx]


class Bone(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("bone.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 1
        if self.rect.top >= 300:
            self.rect.bottom = 0


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Collision")

    dog = Dog()
    bones = pygame.sprite.Group()

    for i in range(5):
        bones.add(Bone((50+i*100, 0)))

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # update actors
        dog.update()
        bones.update()

        # check collision
        pygame.sprite.spritecollide(dog, bones, True, pygame.sprite.collide_mask)

        # draw screen
        screen.fill((255, 255, 255))
        dog.draw(screen)
        bones.draw(screen)
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
