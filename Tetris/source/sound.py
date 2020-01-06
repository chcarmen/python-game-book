from collections import defaultdict

import pyglet

from settings import Settings


class DummySound:
    def play(self):
        pass

    def pause(self):
        pass


class Sound:
    pyglet.resource.path.append("../res/sound")
    pyglet.resource.reindex()

    try:
        button_sound = pyglet.resource.media("button.mp3", streaming=False)
    except Exception as e:
        button_sound = DummySound()
        print(e)

    def __init__(self):

        if Settings.input_music:
            try:
                snd = pyglet.resource.media("tetris.mp3", streaming=False)
            except Exception as e:
                self.music = DummySound()
                print(e)
            else:
                self.music = pyglet.media.Player()
                self.music.queue(snd)
                self.music.loop = True
        else:
            self.music = DummySound()

        self.sounds = defaultdict(DummySound)

        if Settings.input_sound:
            sounds = ["drop", "level", "line", "move", "gameover", "win"]
            try:
                self.sounds = {sound: pyglet.resource.media(sound + ".mp3", streaming=False) for sound in sounds}
            except Exception as e:
                print(e)

    def play(self, name):
        if name == "tetris":
            self.music.play()
        else:
            self.sounds[name].play()

    def stop(self, name):
        if name == "tetris":
            self.music.pause()
