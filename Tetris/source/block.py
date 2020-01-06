import copy

from cocos.euclid import Point2

from settings import Settings


class Block:
    def __init__(self):
        self.rot = 0

        # left-bottom corner position corresponding to board array
        self.pos = Point2((Settings.COLUMN-self.n)//2, Settings.ROW-2)

        self.color_shape()

    def color_shape(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.shape[i][j]:
                    self.shape[i][j] = self.color

    def draw(self, pos):
        left = pos[0]
        bottom = pos[1]

        for i in range(self.n):
            for j in range(self.n):
                color = self.get_value(i, j)
                if color:
                    Settings.IMAGES[color].blit((j + self.pos.x) * Settings.SQUARE_SIZE + left,
                                                (i + self.pos.y) * Settings.SQUARE_SIZE + bottom)

    def get_value(self, x, y):
        if self.rot == 0:
            i, j = x, y
        elif self.rot == 1:
            i, j = y, (self.n - x - 1)
        elif self.rot == 2:
            i, j = (self.n - x - 1), (self.n - y - 1)
        elif self.rot == 3:
            i, j = (self.n - y - 1), x

        return self.shape[i][j]

    def move_left(self):
        self.pos.x -= 1

    def move_right(self):
        self.pos.x += 1

    def move_down(self):
        self.pos.y -= 1

    def rotate(self):
        self.rot = (self.rot + 1) % self.type

    def backup(self):
        self.save_pos = copy.copy(self.pos)
        self.save_rot = self.rot

    def restore(self):
        self.pos = self.save_pos
        self.rot = self.save_rot


class BlockI(Block):
    n = 4
    type = 2
    color = Settings.COLOR_BLUE

    shape = [[0, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]


class BlockO(Block):
    n = 2
    type = 1
    color = Settings.COLOR_GREEN

    shape = [[1, 1],
             [1, 1]]


class BlockT(Block):
    n = 3
    type = 4
    color = Settings.COLOR_MAGENTA

    shape = [[1, 1, 1],
             [0, 1, 0],
             [0, 0, 0]]


class BlockZ(Block):
    n = 3
    type = 2
    color = Settings.COLOR_ORANGE

    shape = [[0, 1, 1],
             [1, 1, 0],
             [0, 0, 0]]


class BlockS(Block):
    n = 3
    type = 2
    color = Settings.COLOR_PINK

    shape = [[1, 1, 0],
             [0, 1, 1],
             [0, 0, 0]]


class BlockL(Block):
    n = 3
    type = 4
    color = Settings.COLOR_VIOLET

    shape = [[1, 1, 1],
             [0, 0, 1],
             [0, 0, 0]]


class BlockJ(Block):
    n = 3
    type = 4
    color = Settings.COLOR_YELLOW

    shape = [[1, 1, 1],
             [1, 0, 0],
             [0, 0, 0]]
