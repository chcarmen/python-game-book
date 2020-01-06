from cocos.actions import Delay, Show

from common.image import Image
from .actor import Actor
from .action import MoveActor, ShowProp


class Mushroom(Actor):
    def __init__(self, image, pos, maplayer):
        super().__init__(image, pos, maplayer)

        self.velocity = (50, 0)
        self.visible = False

        self.do(Delay(0.3) + Show() + ShowProp() + MoveActor())

    def on_bump_handler(self, vx, vy):
        if self.bumped_x:
            vx = -vx

        if self.bumped_y:
            vy = 0

        return vx, vy


class NormalMushroom(Mushroom):
    def __init__(self, pos, maplayer):
        super().__init__(Image.normal_mushroom, pos, maplayer)


class LifeMushroom(Mushroom):
    def __init__(self, pos, maplayer):
        super().__init__(Image.life_mushroom, pos, maplayer)


class FireFlower(Actor):
    def __init__(self, pos, _):
        super().__init__(Image.fire_flower_blink, pos, _)

        self.visible = False
        self.do(Delay(0.3) + Show() + ShowProp())


# Todo: fire ball feature
class FireBall(Actor):
    def __init__(self, pos, maplayer):
        super().__init__("fireball", pos, maplayer)

        self.velocity = (50, -10)

        self.do(MoveActor())

    def on_bump_handler(self, vx, vy):
        if self.bumped_x:
            vx = 0
            self.kill()

        if self.bumped_y:
            vy = -vy

        return vx, vy
