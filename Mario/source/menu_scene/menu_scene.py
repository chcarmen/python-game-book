from cocos.scene import Scene

from common.hud import HudLayer
from .bg_layer import BackgroundLayer
from .menu_layer import MenuLayer


class MenuScene(Scene):
    def __init__(self):
        super().__init__()

        self.add(BackgroundLayer(), z=0)

        hud = HudLayer()
        self.add(hud, z=10)

        self.add(MenuLayer(hud), z=1)
