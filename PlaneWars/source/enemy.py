import pygame
from pygame.sprite import Sprite

from image import Image


class Enemy(Sprite):
    def __init__(self, topleft, screen_rect, stats):
        super().__init__()

        self.screen_rect = screen_rect
        self.stats = stats

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = pygame.Rect(topleft, self.get_max_size())
        self.current_hp = self.max_hp
        self.is_hit_bullet = False

    def update(self):
        self.rect.top += 2

        # remove enemy outside the screen from group
        if self.rect.top >= self.screen_rect.bottom:
            self.kill()

    def hit_by_bullet(self):
        if self.current_hp > 0:
            self.current_hp -= 1
            self.is_hit_bullet = True

    @classmethod
    def get_max_size(cls):
        max_width_image = max(cls.images, key=lambda x: x.get_width())
        max_height_image = max(cls.images, key=lambda x: x.get_height())

        return max_width_image.get_width(), max_height_image.get_height()


class EnemySmall(Enemy):
    type = 1
    max_hp = 1
    score = 2
    images = Image.small_enemies

    def update(self):
        super().update()

        if self.current_hp > 0:
            self.image_index = 0
        else:
            if self.image_index < len(self.images) - 1:
                self.image_index += 1
            else:
                self.kill()
                self.stats.score += self.score

        self.image = self.images[self.image_index]


class EnemyMiddle(Enemy):
    type = 2
    max_hp = 10
    score = 10
    images = Image.mid_enemies

    def update(self):
        super().update()

        if self.current_hp > 0:
            if self.is_hit_bullet:
                self.image_index = 1
                self.is_hit_bullet = False
            else:
                self.image_index = 0
        else:
            if self.image_index < len(self.images) - 1:
                self.image_index += 1
            else:
                self.kill()
                self.stats.score += self.score

        self.image = self.images[self.image_index]


class EnemyBig(Enemy):
    type = 3
    max_hp = 25
    score = 100
    images = Image.big_enemies

    def update(self):
        super().update()

        if self.current_hp > 0:
            if self.is_hit_bullet:
                self.image_index = 2
                self.is_hit_bullet = False
            else:
                self.image_index = (self.image_index + 1) % 2
        else:
            if self.image_index < len(self.images) - 1:
                self.image_index += 1
            else:
                self.kill()
                self.stats.score += self.score

        self.image = self.images[self.image_index]
