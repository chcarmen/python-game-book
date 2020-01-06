from cocos.actions import Show, Delay, Hide
from cocos.layer import Layer, ColorLayer
from cocos.text import Label

from settings import Settings
from stats import stats


class HUDLayer(Layer):
    def __init__(self):
        super().__init__()

        self.position = (440, 10)  # left-bottom corner

        # hint region
        self.hint = ColorLayer(128, 128, 128, 128, 240, 120)
        self.hint.position = (0, 460)
        self.add(self.hint, z=-1)

        self.level = self.create_text(0, 380)
        self.lines = self.create_text(0, 300)
        self.score = self.create_text(0, 220)

        self.msg = Label("",
                         font_name="Kristen ITC",
                         font_size=46,
                         color=(176, 48, 96, 255),
                         anchor_x="left",
                         anchor_y="bottom")

        self.msg.position = (0, 50)
        self.add(self.msg)

    def create_text(self, x, y):
        text = Label("",
                     font_name="Kristen ITC",
                     font_size=32,
                     color=(105, 105, 105, 255),
                     anchor_x="left",
                     anchor_y="bottom")

        text.position = (x, y)
        self.add(text)
        return text

    def draw(self):
        self.level.element.text = "level  " + str(stats.level)
        self.lines.element.text = "lines  " + str(stats.lines)
        self.score.element.text = "score " + str(stats.score)

        stats.next_block.draw((self.position[0]-Settings.SQUARE_SIZE, self.position[1]-Settings.SQUARE_SIZE))

        if stats.msg_queue:
            self.show_msg(stats.msg_queue.popleft())

    def show_msg(self, msg):
        self.msg.element.text = msg
        self.msg.do(Show() + Delay(1) + Hide())
