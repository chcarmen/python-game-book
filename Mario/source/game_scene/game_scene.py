from cocos.scene import Scene
from cocos.tiles import load
from cocos.layer import ScrollingManager, ColorLayer

from .game_layer import GameLayer
from .action import BlinkBricks


class GameScene(Scene):
    def __init__(self, hud):
        super().__init__()

        try:
            fullmap = load("mario-world1-1.tmx")
        except Exception as e:
            raise SystemExit(e)

        bg_map = fullmap["Background"]
        fg_map = fullmap["Foreground"]
        ob_map = fullmap["Objects"]
        tileset = fullmap["Mario"]

        fg_map.do(BlinkBricks())
        fg_map.set_cell_opacity(64, 5, 0)

        scroller = ScrollingManager()
        scroller.add(bg_map, z=0)
        scroller.add(fg_map, z=2)
        scroller.add(GameLayer(hud, fg_map, ob_map, tileset), z=1)

        scroller.scale = 2.5

        self.add(ColorLayer(107, 140, 255, 255), z=0)
        self.add(scroller, z=1)
        self.add(hud, z=10)
