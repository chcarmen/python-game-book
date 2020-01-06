from cocos.actions import MoveBy, Delay, CallFunc
from cocos.sprite import Sprite

from common.image import Image


class Coin(Sprite):
    def __init__(self, pos):
        super().__init__(Image.coin)

        self.position = pos
        self.scale = 0.8

        self.do(MoveBy((0, 35), 0.1) + Delay(0.1) + CallFunc(self.kill))
