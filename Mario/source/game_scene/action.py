from cocos.actions import Action, MoveBy, MoveTo

from common.image import Image


class MoveActor(Action):
    GRAVITY = -1000

    def step(self, dt):
        vx, vy = self.target.velocity

        vy += self.GRAVITY * dt

        dx = vx * dt
        dy = vy * dt

        old = self.target.get_rect()

        new = old.copy()

        new.x += dx
        new.y += dy

        self.target.velocity = self.target.collide_map(self.target.maplayer, old, new, vx, vy)

        self.target.update_position(new.center)


class ShowProp(MoveBy):
    def init(self, delta=(0, 13), duration=0.5):
        super().init(delta, duration)

    def update(self, t):
        super().update(t)
        self.target.update_position(self.target.position)


class BlinkBricks(Action):
    GREY = (128, 128, 128)
    WHITE = (255, 255, 255)

    def init(self):
        self.color_index = 0

    def step(self, dt):
        self._elapsed += dt
        if self._elapsed > 0.5:
            color = self.GREY if self.color_index else self.WHITE
            self.color_index = not self.color_index
            self._elapsed = 0

            for brick in self.target.find_cells(label="unknown brick"):
                self.target.set_cell_color(brick.i, brick.j, color)


class WalkToCastle(MoveTo):
    def init(self, dst_coords, duration=2.5):
        super().init(dst_coords, duration)

    def start(self):
        super().start()
        self.target.image = Image.mario_walk_to_castle[self.target.state]

    def update(self, t):
        super().update(t)
        self.target.scroller.set_focus(self.target.x, 0)
