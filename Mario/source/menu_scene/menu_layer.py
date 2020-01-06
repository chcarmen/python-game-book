from cocos.layer import Layer
from cocos.text import Label
from cocos.sprite import Sprite
from cocos.director import director
from pyglet.window import key

from common.stats import stats
from common.image import Image
from info_scene.info_scene import InfoScene


class MenuLayer(Layer):
    is_event_handler = True

    def __init__(self, hud):
        super().__init__()

        self.hud = hud
        width, height = director.get_window_size()

        self.menu_item_one_text = self.create_text("1 PLAYER GAME", width//2, height//2-100)
        self.menu_item_one_icon = self.create_icon(200, self.menu_item_one_text.y)

        self.menu_item_two_text = self.create_text("2 PLAYER GAME", width//2, height//2-150)
        self.menu_item_two_icon = self.create_icon(200, self.menu_item_two_text.y)
        self.menu_item_two_icon.visible = False

    def create_text(self, text, x, y):
        text = Label(text,
                     font_name="FixedsysTTF",
                     font_size=32,
                     bold=True,
                     color=(255, 255, 255, 255),
                     anchor_x="center",
                     anchor_y="center")

        text.position = (x, y)
        self.add(text)
        return text

    def create_icon(self, x, y):
        icon = Sprite(Image.menu)
        icon.position = (x, y)
        self.add(icon)
        return icon

    def on_key_press(self, k, _):
        if k == key.UP:
            self.menu_item_one_icon.visible = True
            self.menu_item_two_icon.visible = False
        elif k == key.DOWN:
            self.menu_item_one_icon.visible = False
            self.menu_item_two_icon.visible = True
        elif k == key.ENTER:
            if self.menu_item_one_icon.visible:
                stats.reset_new_game()
                director.push(InfoScene(self.hud))
            elif self.menu_item_two_icon.visible:
                pass
