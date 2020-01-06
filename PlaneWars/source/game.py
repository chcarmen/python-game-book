import sys
import random

import pygame
from pygame.sprite import Group

from stats import Stats
from background import Background
from hero import Hero
from bullet import Bullet
from enemy import EnemySmall, EnemyMiddle, EnemyBig
from button import Button
from widgets import Logo, EndPrompt, Scoreboard, PauseResume
from sound import Sound


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((480, 852))
        pygame.display.set_caption("Plane Wars")

        try:
            icon = pygame.image.load("../res/image/icon.ico")
        except pygame.error:
            pass
        else:
            pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.stats = Stats()

        self.bg = Background()
        self.hero = Hero(self.surface.get_rect(), self.stats)
        self.bullets = Group()
        self.enemies = Group()

        buttons_name = ["Start", "Restart", "Exit"]
        self.buttons = {name: Button(self.surface.get_rect(), name) for name in buttons_name}

        widgets_name = ["Logo", "EndPrompt", "Scoreboard", "PauseResume"]
        self.widgets = {name: eval(name)(self.surface.get_rect(), self.stats) for name in widgets_name}

        self.sounds = Sound()

        self.frames = 0

    def reset(self):
        self.stats.reset()
        self.hero.reset()
        self.widgets["PauseResume"].reset()

    def run(self):
        while True:
            self.handle_events()

            if self.stats.state == Stats.RUN:
                self.bg.update()
                self.update_bullets()
                self.update_enemies()
                self.handle_collision()

            self.update_screen()

            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mousedown_event(event)
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mousemotion_event(event)

    def handle_mousedown_event(self, event):
        if self.stats.state == Stats.WELCOME:
            if self.buttons["Start"].is_hit(event.pos):
                self.stats.state = Stats.RUN
                # play background music indefinitely
                self.sounds.play("bg")
        elif self.stats.state == Stats.RUN:
            if self.widgets["PauseResume"].is_hit(event.pos):
                self.widgets["PauseResume"].update_click()
                self.stats.state = Stats.PAUSE
                self.sounds.pause("bg")
        elif self.stats.state == Stats.PAUSE:
            if self.widgets["PauseResume"].is_hit(event.pos):
                self.widgets["PauseResume"].update_click()
                self.stats.state = Stats.RUN
                self.sounds.unpause("bg")
        elif self.stats.state == Stats.GAMEOVER:
            if self.buttons["Restart"].is_hit(event.pos):
                self.reset()
                self.stats.state = Stats.RUN
                self.sounds.play("bg")
            elif self.buttons["Exit"].is_hit(event.pos):
                pygame.quit()
                sys.exit()

    def handle_mousemotion_event(self, event):
        if self.stats.state == Stats.RUN:
            if event.buttons[0]:
                self.hero.update(event.pos)

            self.widgets["PauseResume"].update_mouse_motion(event.pos)
        elif self.stats.state == Stats.PAUSE:
            self.widgets["PauseResume"].update_mouse_motion(event.pos)

    def update_bullets(self):
        # create bullet
        self.frames += 1
        if not (self.frames % 5):
            self.bullets.add(Bullet(self.hero.rect))
            self.sounds.play("bullet")

        # move bullets
        self.bullets.update()

    def update_enemies(self):
        if len(self.enemies) < 18:
            screen_rect = self.surface.get_rect()

            weighted_list = [EnemySmall] * 30 + [EnemyMiddle] * 3 + [EnemyBig] * 1
            enemy = random.choice(weighted_list)

            left = random.randint(0, screen_rect.width - enemy.get_max_size()[0])
            top = random.randint(-screen_rect.height, -enemy.get_max_size()[1])

            self.enemies.add(enemy((left, top), screen_rect, self.stats))

        self.enemies.update()

    def handle_collision(self):
        # check bullets & enemies collision
        collide_dict = pygame.sprite.groupcollide(self.bullets, self.enemies, True, False, pygame.sprite.collide_mask)
        collide_enemies_list = []

        if collide_dict:
            for collide_enemies in collide_dict.values():
                collide_enemies_list.extend(collide_enemies)

        if collide_enemies_list:
            for collide_enemy in collide_enemies_list:
                if collide_enemy.current_hp == 1:
                    self.sounds.play("enemy" + str(collide_enemy.type) + "_down")

                collide_enemy.hit_by_bullet()

        # check hero & enemies collision
        enemy = pygame.sprite.spritecollideany(self.hero, self.enemies, pygame.sprite.collide_mask)
        if enemy:
            self.hero.is_collide = True
            self.bullets.empty()
            self.enemies.empty()
            self.widgets["EndPrompt"].update_score_num()
            self.sounds.fadeout("bg")
            self.sounds.play("game_over")

    def update_screen(self):
        # draw background image onto display surface
        self.bg.draw(self.surface)

        if self.stats.state == Stats.WELCOME:
            # welcome state
            self.widgets["Logo"].draw(self.surface)
            self.buttons["Start"].draw(self.surface)
        elif self.stats.state == Stats.RUN or self.stats.state == Stats.PAUSE:
            # run/pause state
            self.hero.draw(self.surface)
            self.bullets.draw(self.surface)
            self.enemies.draw(self.surface)

            # draw pause button and score at last, keeps them above the screen
            self.widgets["PauseResume"].draw(self.surface)
            self.widgets["Scoreboard"].draw(self.surface)
        elif self.stats.state == Stats.GAMEOVER:
            # game over state
            self.widgets["EndPrompt"].draw(self.surface)
            self.buttons["Restart"].draw(self.surface)
            self.buttons["Exit"].draw(self.surface)

        # update display surface
        pygame.display.flip()
