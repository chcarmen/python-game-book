from collections import defaultdict

from pyglet import resource, media


class DummyPlayer:
    def play(self):
        pass

    def pause(self):
        pass


class Sound:
    resource.path.append("../res/sound")
    resource.reindex()

    try:
        snd = resource.media("main_theme.mp3", streaming=False)
    except Exception as e:
        music = DummyPlayer()
        print(e)
    else:
        music = media.Player()
        music.queue(snd)
        music.loop = True

    sounds_name = ["big_jump", "brick_smash", "bump", "coin", "death",
                   "flagpole", "game_over", "out_of_time", "powerup", "powerup_appears",
                   "small_jump", "stage_clear", "stomp"]

    sounds = defaultdict(DummyPlayer)

    for sound in sounds_name:
        try:
            sounds[sound] = resource.media(sound + ".mp3", streaming=False)
        except Exception as e:
            print(e)

    @classmethod
    def play(cls, name):
        if name == "mario":
            cls.music.play()
        else:
            cls.sounds[name].play()

    @classmethod
    def stop(cls, name):
        if name == "mario":
            cls.music.pause()
