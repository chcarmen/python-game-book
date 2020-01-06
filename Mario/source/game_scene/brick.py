from cocos.sprite import Sprite
from cocos.actions import JumpBy, CallFunc
from cocos.particle import ParticleSystem, Color
from cocos.euclid import Point2

from common.image import Image


class PopupBrick(Sprite):
    def __init__(self, name, pos):
        if name == "unknown":
            image = Image.unknown_brick
        else:
            image = Image.normal_brick

        super().__init__(image)

        self.position = pos

        self.do(JumpBy((0, 0), 8, 1, 0.2) + CallFunc(self.kill))


class BrokenBrick(ParticleSystem):
    total_particles = 4
    duration = 0.1
    gravity = Point2(0, -600)
    angle = 90
    angle_var = 90.0
    speed = 100.0
    life = 3.0
    size = 8.0
    start_color = Color(255, 255, 255, 255)
    end_color = Color(255, 255, 255, 255)
    emission_rate = total_particles / duration

    def __init__(self, pos):
        super().__init__()

        self.position = pos
        self.auto_remove_on_finish = True

    def load_texture(self):
        self.__class__.texture = Image.normal_brick2.get_texture()
