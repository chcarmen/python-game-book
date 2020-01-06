from cocos.sprite import Sprite
from cocos.collision_model import AARectShape
from cocos.euclid import Vector2
from pyglet.window import key


class Actor(Sprite):
    def __init__(self, image, pos):
        super().__init__(image)
        self.position = pos
        self.cshape = AARectShape(Vector2(self.x, self.y), self.width/2, self.height/2)

    def update_cshape(self):
        self.cshape.center = Vector2(self.x, self.y)


class Mouse(Actor):
    def __init__(self, pos):
        super().__init__('mouse.png', pos)
        self.direction = 1
        # case 2
        self.schedule(self.move)

    def move(self, dt):
        self.x += self.direction
        if self.x >= 500 or self.x < 0:
            self.direction *= -1

        self.update_cshape()


class Cat(Actor):
    def __init__(self, pos):
        super().__init__('cat.png', pos)

    def move(self, pressed):
        if pressed[key.LEFT]:
            if self.x > 0:
                self.x -= 3
        elif pressed[key.RIGHT]:
            if self.x < 500:
                self.x += 3
        elif pressed[key.UP]:
            if self.y < 300:
                self.y += 3
        elif pressed[key.DOWN]:
            if self.y > 0:
                self.y -= 3

        self.update_cshape()
