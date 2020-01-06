from cocos.sprite import Sprite
from cocos.collision_model import AARectShape
from cocos.euclid import Vector2
from cocos.mapcolliders import RectMapCollider


class Actor(Sprite, RectMapCollider):
    def __init__(self, image, pos, maplayer):
        Sprite.__init__(self, image)
        RectMapCollider.__init__(self)

        x, y = pos
        self.position = Vector2(x, y)
        self.cshape = AARectShape(self.position, self.width/2, self.height/2)

        self.maplayer = maplayer

    def update_position(self, new_pos):
        x, y = new_pos
        self.position = Vector2(x, y)
        self.cshape.center = self.position
        self.cshape.ry = self.height / 2
