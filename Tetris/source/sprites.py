from cocos.actions import *
from cocos.layer import Layer
from cocos.sprite import Sprite
import pyglet


class SpritesLayer(Layer):
    def __init__(self):
        super().__init__()

        try:
            sprite0 = Sprite("sp.png")
            sprite1 = Sprite("block_blue.png")
            sprite2 = Sprite("block_magenta.png")
            sprite3 = Sprite("block_yellow.png")
            sprite4 = Sprite("block_magenta.png")
            sprite5 = Sprite("block_orange.png")
        except pyglet.resource.ResourceNotFoundException:
            raise SystemExit("cannot find sprite image!")

        sprite0.position = (400, 150)
        sprite0.opacity = 0
        sprite0.do(FadeIn(2))
        self.add(sprite0)

        sprite1.position = (325, 600)
        sprite1.do(MoveTo((325, 265), 2) + JumpTo((208, 119), 200, 5, 5))
        self.add(sprite1)

        sprite2.position = (354, 600)
        sprite2.do(MoveTo((354, 265), 3) + JumpTo((412, 177), 300, 3, 3))
        self.add(sprite2)

        sprite3.position = (500, 600)
        sprite3.do(MoveTo((500, 120), 3) | (RotateBy(360, 1)) * 3)
        self.add(sprite3)

        sprite4.position = (587, 600)
        sprite4.do(MoveTo((587, 236), 5) | (ScaleBy(3, 2) + Reverse(ScaleBy(3, 2))))
        self.add(sprite4)

        sprite5.position = (150, 600)
        sprite5.do(MoveTo((150, 120), 3) | (RotateBy(360, 1)) * 3)
        self.add(sprite5)

        self.do(Delay(7) + FadeOutBLTiles(grid=(16, 12), duration=3) + StopGrid())
