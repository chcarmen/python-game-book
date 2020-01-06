from cocos.sprite import Sprite
from cocos.mapcolliders import RectMapCollider
from cocos.layer import ScrollingManager
from pyglet.window import key


class Actor(Sprite, RectMapCollider):
    MOVE_SPEED = 100
    GRAVITY = -500

    def __init__(self, pos, maplayer):
        Sprite.__init__(self, "ball.png", pos)
        RectMapCollider.__init__(self, "slide")

        self.maplayer = maplayer
        self.velocity = (0, 0)

    def on_enter(self):
        super().on_enter()
        self.scroller = self.get_ancestor(ScrollingManager)

    def update_position(self, dt, pressed):
        if dt > 0.1:
            return

        old = self.get_rect()
        new = old.copy()

        vx, vy = self.velocity
        vx = (pressed[key.RIGHT] - pressed[key.LEFT]) * self.MOVE_SPEED
        vy += dt * self.GRAVITY

        new.x += vx * dt
        new.y += vy * dt

        self.velocity = self.collide_map(self.maplayer, old, new, vx, vy)

        self.position = new.center
        self.scroller.set_focus(160, self.y)

    def collide_bottom(self, cell):
        print(cell)
