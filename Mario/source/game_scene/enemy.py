from cocos.actions import Delay, CallFunc

from common.image import Image
from .actor import Actor
from .action import MoveActor


class Enemy(Actor):
    def __init__(self, image, pos, maplayer):
        super().__init__(image, pos, maplayer)

        self.velocity = (-50, 0)
        self.active = True

        self.do(MoveActor())

    def on_bump_handler(self, vx, vy):
        if self.bumped_x:
            vx = -vx

        if self.bumped_y:
            vy = 0

        return vx, vy


class Goomba(Enemy):
    def __init__(self, pos, maplayer):
        super().__init__(Image.goomba_move, pos, maplayer)

    def die(self):
        self.active = False
        self.stop()
        self.image = Image.goomba_die
        self.do(Delay(0.3) + CallFunc(self.kill))


class Koopa(Enemy):
    def __init__(self, pos, maplayer):
        super().__init__(Image.koopa_move, pos, maplayer)

    def die(self):
        self.active = False
        self.stop()
        self.image = Image.koopa_die
