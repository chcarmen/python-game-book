import pygame

from image import Image


class Logo:
    def __init__(self, *args):
        screen_rect = args[0]
        self.image = Image.logo
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery - 150

    def draw(self, display_surface):
        display_surface.blit(self.image, self.rect)


class Scoreboard:
    def __init__(self, *args):
        self.stats = args[1]
        self.score_color = (0, 0, 0)

        try:
            self.font = pygame.font.Font("../res/font/comici.ttf", 35)
        except Exception as e:
            print(e)
            self.font = pygame.font.SysFont(None, 50)

    def draw(self, display_surface):
        score_image = self.font.render(str(self.stats.score), True, self.score_color)
        display_surface.blit(score_image, (80, 0))


class PauseResume:
    # Pause and resume states
    PAUSE_NORMAL, PAUSE_PRESSED, RESUME_NORMAL, RESUME_PRESSED = range(4)

    def __init__(self, *args):
        self.images = Image.pause_resume
        self.state = PauseResume.PAUSE_NORMAL

        self.rect = self.images[self.state].get_rect()
        self.rect.topleft = (0, 5)

    def reset(self):
        self.state = PauseResume.PAUSE_NORMAL

    def draw(self, display_surface):
        display_surface.blit(self.images[self.state], self.rect)

    def is_hit(self, pos):
        return self.rect.collidepoint(pos)

    def update_click(self):
        if self.state == PauseResume.PAUSE_NORMAL or self.state == PauseResume.PAUSE_PRESSED:
            self.state = PauseResume.RESUME_NORMAL
        else:
            self.state = PauseResume.PAUSE_NORMAL

    def update_mouse_motion(self, pos):
        is_mouse_on = self.is_hit(pos)

        if is_mouse_on:
            if self.state == PauseResume.PAUSE_NORMAL:
                self.state = PauseResume.PAUSE_PRESSED
            elif self.state == PauseResume.RESUME_NORMAL:
                self.state = PauseResume.RESUME_PRESSED
        else:
            if self.state == PauseResume.PAUSE_PRESSED:
                self.state = PauseResume.PAUSE_NORMAL
            elif self.state == PauseResume.RESUME_PRESSED:
                self.state = PauseResume.RESUME_NORMAL


class EndPrompt:
    def __init__(self, *args):
        screen_rect = args[0]
        self.stats = args[1]

        # outside border
        self.border_color = (96, 96, 96)
        self.border_rect = pygame.Rect(0, 0, 350, 300)
        self.border_rect.centerx = screen_rect.centerx
        self.border_rect.centery = screen_rect.centery + 40

        # score
        self.score_color = self.border_color
        self.font = pygame.font.SysFont(None, 40)

        # score text
        self.score_text_image = self.font.render("Score:", True, self.score_color)
        self.score_text_top = self.border_rect.top + 30
        self.score_text_left = self.border_rect.left + 30

        # score number
        self.update_score_num()

    def update_score_num(self):
        self.score_num_image = self.font.render(str(self.stats.score), True, self.score_color)
        self.score_num_rect = self.score_num_image.get_rect()
        self.score_num_rect.centerx = self.border_rect.centerx
        self.score_num_rect.centery = self.border_rect.top + 80

    def draw(self, display_surface):
        # draw border
        pygame.draw.rect(display_surface, self.border_color, self.border_rect, 3)

        # draw score text
        display_surface.blit(self.score_text_image, (self.score_text_left, self.score_text_top))

        # draw score number
        display_surface.blit(self.score_num_image, self.score_num_rect)
