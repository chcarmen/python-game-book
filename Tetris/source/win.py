from cocos.director import director
from cocos.actions import Blink, Show, FadeIn
from cocos.layer import Layer
from cocos.particle_systems import Fireworks
from cocos.text import Label
from pyglet.window import key


class WinLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        width, height = director.get_window_size()

        # particle effect
        pe = Fireworks()

        pe.position = (width//2, 80)
        pe.duration = 6
        pe.speed = 260
        pe.size = 10.0
        pe.auto_remove_on_finish = True

        self.add(pe)

        action = Blink(20, 2) + Show()

        # msg1
        msg1 = self.create_text("Congratulations!", 72, width//2, height//2)
        msg1.do(action)

        # msg2
        msg2 = self.create_text("You win", 46, width//2, height//3)
        msg2.do(action)

        # msg3
        msg3 = self.create_text("press enter back to menu", 32, width//2, 0)
        msg3.opacity = 0
        msg3.do(FadeIn(2))

    def create_text(self, msg, size, x, y):
        text = Label(msg,
                     font_name="Kristen ITC",
                     font_size=size,
                     color=(255, 0, 0, 255),
                     anchor_x="center",
                     anchor_y="bottom")

        text.position = (x, y)
        self.add(text)

        return text

    def on_key_press(self, k, _):
        if k == key.ENTER:
            director.pop()
