from cocos.actions import MoveTo, MoveBy
from cocos.sprite import Sprite

from common.image import Image


class Flag(Sprite):
    def __init__(self, pos):
        super().__init__(Image.flag)

        self.position = pos

    def lower(self):
        self.do(MoveTo((self.x, 56), 2))


class CastleFlag(Sprite):
    def __init__(self, pos):
        super().__init__(Image.castle_flag)

        self.position = pos

        self.do(MoveBy((0, 15), 0.5))
