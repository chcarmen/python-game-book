from cocos.director import director
from cocos.actions import MoveTo, FadeIn
from cocos.layer import Layer
from cocos.text import Label
from pyglet.window import key


class GameoverLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        width, height = director.get_window_size()

        # msg1
        msg1 = self.create_text("Game over", 72, width//2, height)
        msg1.do(MoveTo((width//2, height//2), 1))

        # msg2
        msg2 = self.create_text("press enter back to menu", 32, width//2, 0)
        msg2.opacity = 0
        msg2.do(FadeIn(2))

    def create_text(self, msg, size, x, y):
        text = Label(msg,
                     font_name="Kristen ITC",
                     font_size=size,
                     color=(255, 255, 255, 255),
                     anchor_x="center",
                     anchor_y="bottom")

        text.position = (x, y)
        self.add(text)

        return text

    def on_key_press(self, k, _):
        if k == key.ENTER:
            director.pop()
