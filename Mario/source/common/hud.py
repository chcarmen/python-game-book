from cocos.layer import Layer
from cocos.text import Label

from common.stats import stats


class HudLayer(Layer):
    def __init__(self):
        super().__init__()

        self.position = (0, 540)  # default anchor position is left-bottom corner

        self.score_text = self.create_text("MARIO", 100, 30)
        self.score_num = self.create_text("", 100, 0)

        self.coins_text = self.create_text("COINS", 300, 30)
        self.coins_num = self.create_text("", 300, 0)

        self.world_text = self.create_text("WORLD", 500, 30)
        self.world_num = self.create_text("", 500, 0)

        self.time_text = self.create_text("TIME", 700, 30)
        self.time_num = self.create_text("", 700, 0)

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

        return text

    def draw(self):
        self.score_num.element.text = str(stats.score)
        self.coins_num.element.text = str(stats.coins)
        self.world_num.element.text = "-".join([str(stats.major_world), str(stats.minor_world)])
        self.time_num.element.text = str(stats.time)
