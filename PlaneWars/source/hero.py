import pygame

from stats import Stats
from image import Image


class Hero:
    def __init__(self, screen_rect, stats):
        self.screen_rect = screen_rect
        self.stats = stats

        self.images = Image.heros
        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.image_index = 0
        self.is_collide = False

    def draw(self, display_surface):
        if self.is_collide:
            if self.image_index < len(self.images) - 1:
                self.image_index += 1
            else:
                pygame.time.delay(200)
                self.stats.state = Stats.GAMEOVER
        else:
            self.image_index = not self.image_index

        self.image = self.images[self.image_index]

        display_surface.blit(self.image, self.rect)

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.rect.center = pos
