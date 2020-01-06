from collections import defaultdict

import pygame


class DummySound:
    def play(self, *args):
        pass

    def pause(self):
        pass

    def unpause(self):
        pass

    def fadeout(self, *args):
        pass


class Sound:
    def __init__(self):
        # background music
        try:
            pygame.mixer.music.load("../res/sound/game_music.wav")
        except pygame.error as e:
            self.music = DummySound()
            print(e)
        else:
            self.music = pygame.mixer.music

        # sound effect
        self.sounds = defaultdict(DummySound)

        sounds_name = ["bullet", "enemy1_down", "enemy2_down", "enemy3_down", "game_over"]

        for sound in sounds_name:
            try:
                self.sounds[sound] = pygame.mixer.Sound(sound.join(["../res/sound/", ".wav"]))
            except pygame.error as e:
                print(e)

    def play(self, name):
        if name == "bg":
            self.music.play(-1)
        else:
            self.sounds[name].play()

    def pause(self, name):
        if name == "bg":
            self.music.pause()

    def unpause(self, name):
        if name == "bg":
            self.music.unpause()

    def fadeout(self, name):
        if name == "bg":
            self.music.fadeout(1000)
