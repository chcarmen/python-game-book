import random

from cocos.director import director
from cocos.layer import ColorLayer
from cocos.scene import Scene
from pyglet.window import key

from background import BackgroundLayer
from block import *
from board import Board
from gameover import GameoverLayer
from hud import HUDLayer
from sound import Sound
from stats import stats
from win import WinLayer


class GameLayer(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__(128, 128, 128, 128)
        self.width = Settings.COLUMN * Settings.SQUARE_SIZE
        self.height = Settings.ROW * Settings.SQUARE_SIZE
        self.position = (120, 10)
        self.elapsed = 0

        stats.reset()

        self.board = Board()
        self.new_block()
        self.schedule(self.drop_block)

        self.sound = Sound()
        self.sound.play("tetris")

    def draw(self):
        super().draw()
        self.board.draw(self.position)
        self.block.draw(self.position)

    def on_text_motion(self, motion):
        if motion == key.MOTION_LEFT:
            self.move_block_left()
        elif motion == key.MOTION_RIGHT:
            self.move_block_right()
        elif motion == key.MOTION_DOWN:
            self.move_block_down()
        elif motion == key.MOTION_UP:
            self.rotate_block()

    def on_landed(self):
        self.board.update(self.block)

        lines = list(self.board.check_lines())
        if lines:
            self.board.move_down_lines(lines)
            stats.update(len(lines))

            self.sound.play("line")

            if "level" in stats.msg_queue[-1]:
                self.sound.play("level")

            if stats.win:
                self.parent.add(WinLayer(), z=10)
                director.window.remove_handlers(self)
                self.unschedule(self.drop_block)

                self.sound.stop("tetris")
                self.sound.play("win")

        if self.board.check_full():
            self.parent.add(GameoverLayer(), z=10)
            director.window.remove_handlers(self)
            self.unschedule(self.drop_block)

            self.sound.stop("tetris")
            self.sound.play("gameover")
        else:
            self.new_block()

    def new_block(self):
        # pick current block from next block stores in stats
        if stats.next_block:
            self.block = stats.next_block
        else:
            self.block = self.random_block()

        # update next block
        stats.next_block = self.random_block()

    def random_block(self):
        block = random.choice((
            BlockI,
            BlockO,
            BlockT,
            BlockZ,
            BlockS,
            BlockL,
            BlockJ
        ))

        return block()

    def drop_block(self, dt):
        self.elapsed += dt
        if self.elapsed > Settings.LEVEL_INFO[stats.level-1]["speed"]:
            self.elapsed = 0
            self.move_block_down()

    def move_block_left(self):
        self.block.backup()
        self.block.move_left()

        if not self.board.check_valid(self.block):
            self.block.restore()

    def move_block_right(self):
        self.block.backup()
        self.block.move_right()

        if not self.board.check_valid(self.block):
            self.block.restore()

    def move_block_down(self):
        self.block.backup()
        self.block.move_down()

        if not self.board.check_valid(self.block):
            self.block.restore()
            self.on_landed()
            self.sound.play("drop")

    def rotate_block(self):
        self.block.backup()
        self.block.rotate()

        if not self.board.check_valid(self.block):
            self.block.restore()

        self.sound.play("move")


def create_game_scene():
    scene = Scene()
    scene.add(BackgroundLayer(), z=0)
    scene.add(HUDLayer(), z=1)
    scene.add(GameLayer(), z=2)

    return scene
