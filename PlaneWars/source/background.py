from image import Image


class Background:
    def __init__(self):
        self.image = Image.background
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)

    def update(self):
        # move down background image
        if self.y < self.rect.height:
            self.y += 1.5
        else:
            self.y = 0

        self.rect.y = self.y

    def draw(self, display_surface):
        # draw 2 images onto display surface
        display_surface.blit(self.image, (0, self.rect.y))
        display_surface.blit(self.image, (0, self.rect.y - self.rect.height))
