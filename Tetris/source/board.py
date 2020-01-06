from settings import Settings


class Board:
    def __init__(self):
        self.array = [[0 for col in range(Settings.COLUMN)] for row in range(Settings.ROW)]

    def draw(self, pos):
        left = pos[0]
        bottom = pos[1]

        for i in range(Settings.ROW):
            for j in range(Settings.COLUMN):
                color = self.array[i][j]
                if color:
                    Settings.IMAGES[color].blit(j * Settings.SQUARE_SIZE + left, i * Settings.SQUARE_SIZE + bottom)

    def check_lines(self):
        # Check if any lines complete
        for i in range(Settings.ROW):
            for j in range(Settings.COLUMN):
                color = self.array[i][j]
                if not color:
                    break
            else:
                yield i

    def move_down_lines(self, lines):
        lines.reverse()

        for line in lines:
            for i in range(line, Settings.ROW - 1):
                for j in range(Settings.COLUMN):
                    self.array[i][j] = self.array[i + 1][j]

    def check_full(self):
        for j in range(Settings.COLUMN):
            if self.array[-1][j]:
                return True

        return False

    def check_valid(self, block):
        for i in range(block.n):
            for j in range(block.n):
                if block.get_value(i, j):
                    if block.pos.x + j < 0:
                        return False
                    if block.pos.x + j >= Settings.COLUMN:
                        return False
                    if block.pos.y + i < 0:
                        return False
                    if block.pos.y + i >= Settings.ROW:
                        return False
                    if self.array[block.pos.y + i][block.pos.x + j]:
                        return False

        return True

    def update(self, block):
        for i in range(block.n):
            for j in range(block.n):
                value = block.get_value(i, j)
                if value:
                    self.array[block.pos.y + i][block.pos.x + j] = value
