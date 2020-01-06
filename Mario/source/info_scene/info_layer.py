from cocos.text import Label
from cocos.director import director
from cocos.sprite import Sprite
from cocos.layer import Layer

from common.stats import stats
from common.image import Image


class InfoLayer(Layer):
    def __init__(self, world_complete):
        super().__init__()

        width, height = director.get_window_size()

        if world_complete:
            self.create_text("WORLD COMPLETE", width//2, height//2)
            return

        if stats.life <= 0:
            self.create_text("GAME OVER", width//2, height//2)
        else:
            text = " WORLD " + str(stats.major_world) + "-" + str(stats.minor_world)
            self.create_text(text, width // 2, height // 2 + 100)

            sprite = Sprite(Image.mario)
            sprite.position = (width//2 - 40, height//2)
            self.add(sprite)

            self.create_text("x " + str(stats.life), width//2 + 40, height//2)

    def create_text(self, text, x, y):
        text = Label(text,
                     font_name="FixedsysTTF",
                     font_size=30,
                     bold=True,
                     color=(255, 255, 255, 255),
                     anchor_x="center",
                     anchor_y="center")

        text.position = (x, y)
        self.add(text)
