import pygame


class Button:
    def __init__(self, screen_rect, text):
        # button border attributes
        self.border_color = (96, 96, 96)
        self.border_rect = pygame.Rect(0, 0, 180, 40)
        self.border_rect.center = screen_rect.center

        if text == "Start":
            self.border_rect.centery += 80
        elif text == "Restart":
            self.border_rect.centery += 80
        elif text == "Exit":
            self.border_rect.centery += 140

        # button text attributes
        text_color = self.border_color
        font = pygame.font.SysFont(None, 40)
        self.text_image = font.render(text, True, text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.border_rect.center

    def draw(self, display_surface):
        # draw button border
        pygame.draw.rect(display_surface, self.border_color, self.border_rect, 3)

        # draw button text
        display_surface.blit(self.text_image, self.text_rect)

    def is_hit(self, pos):
        return self.border_rect.collidepoint(pos)
