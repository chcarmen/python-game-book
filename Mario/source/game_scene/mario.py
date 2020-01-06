from collections import deque

from cocos.layer import ScrollingManager
from cocos.director import director
from cocos.actions import JumpBy, MoveBy, CallFunc, Delay
from pyglet.window import key

from common.image import Image
from common.sound import Sound
from .action import WalkToCastle
from .actor import Actor


class Mario(Actor):
    SMALL, BIG, FIRE = range(3)
    RIGHT, LEFT = range(2)

    MOVE_SPEED = 120
    JUMP_SPEED = 360
    GRAVITY = -1000

    GROUND_POS_Y = [40, 48, 48]

    def __init__(self, pos, maplayer):
        super().__init__(Image.mario_stand[Mario.SMALL][Mario.RIGHT], pos, maplayer)

        self.state = Mario.SMALL
        self.direction = Mario.RIGHT

        self.on_bump_handler = self.on_bump_slide
        self.velocity = (0, 0)

        self.on_ground = True
        self.may_jump = True
        self.image_index = 0
        self.elapsed = 0

        self.collide_cells = deque()
        self.last_rect = None

    def on_enter(self):
        super().on_enter()

        self.scroller = self.get_ancestor(ScrollingManager)
        self.keys = key.KeyStateHandler()

        director.window.push_handlers(self.keys)

    def update_(self, dt):
        self.update_position(dt)
        self.update_animation(dt)

    def update_position(self, dt):
        if dt > 0.1:
            return

        view_x = self.maplayer.view_x
        view_w = self.maplayer.view_w

        vx, vy = self.velocity

        vx = (self.keys[key.RIGHT] - self.keys[key.LEFT]) * self.MOVE_SPEED
        vy += self.GRAVITY * dt

        if not self.keys[key.A] and self.on_ground:
            self.may_jump = True

        if self.keys[key.A] and self.may_jump:
            vy = self.JUMP_SPEED
            self.may_jump = False

            if self.state == Mario.SMALL:
                Sound.play("small_jump")
            else:
                Sound.play("big_jump")

        dx = vx * dt
        dy = vy * dt

        old = self.get_rect()
        self.last_rect = old

        new = old.copy()
        new.x += dx
        new.y += dy

        # prevent scroll the map backwards
        if new.x < view_x:
            new.x = old.x

        self.velocity = self.collide_map(self.maplayer, old, new, vx, vy)

        if new.x > view_x + view_w / 2:
            self.scroller.set_focus(new.x, 0)

        self.on_ground = (new.bottom == old.bottom)

        super().update_position(new.center)

    def update_animation(self, dt):
        if self.keys[key.RIGHT]:
            self.direction = Mario.RIGHT

        if self.keys[key.LEFT]:
            self.direction = Mario.LEFT

        old_height = self.get_rect().height

        if self.keys[key.A] and not self.on_ground:
            self.image = Image.mario_jump[self.state][self.direction]
        elif (self.keys[key.RIGHT] or self.keys[key.LEFT]) and self.on_ground:
            self.elapsed += dt
            if self.elapsed > 0.06:
                self.image_index += 1
                if self.image_index > 2:
                    self.image_index = 0

                self.image = Image.mario_walk[self.state][self.direction][self.image_index]
                self.elapsed = 0
        else:
            self.image = Image.mario_stand[self.state][self.direction]

        new_height = self.get_rect().height

        if new_height != old_height:
            self.image_anchor_y = new_height / 2
            self.y += new_height / 2

    def collide_top(self, cell):
        self.collide_cells.append(cell)

    def collide_right(self, cell):
        if cell.get("label") == "flagpole":
            self.collide_cells.append(cell)

    def collide_bottom_obj(self, obj):
        last_rect = self.last_rect
        current_rect = self.get_rect()
        obj_rect = obj.get_rect()

        if current_rect.bottom <= obj_rect.top < last_rect.bottom:
            return True

        return False

    def die(self):
        self.image = Image.mario_die
        self.do(JumpBy((0, -100), 100, 1, 1))

    def raise_flag(self, x):
        ground_y = Mario.GROUND_POS_Y[self.state]

        def lower_flag():
            self.image = Image.mario_lower_flag[self.state]

            delta_y = ground_y - self.y + 16
            self.do(MoveBy((8, 0), 0.2) + MoveBy((0, delta_y), 1.8))

        def turn_around_after_lower_flag():
            delta_y = ground_y - self.y
            self.do(MoveBy((16, 0), 0.1) + MoveBy((8, delta_y), 0.1))
            self.image = Image.mario_lower_flag_turn_around[self.state]

        self.do(CallFunc(lower_flag) + Delay(2) +
                CallFunc(turn_around_after_lower_flag) + Delay(0.5) +
                CallFunc(Sound.play, "stage_clear") +
                WalkToCastle((x, ground_y)) +
                CallFunc(self.kill))
