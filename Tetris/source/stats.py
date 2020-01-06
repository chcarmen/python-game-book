from collections import deque

from settings import Settings


class Stats:
    def __init__(self):
        self.reset()

    def reset(self):
        self.level = Settings.input_level
        self.lines = 0
        self.score = 0
        self.next_block = None
        self.win = False

        self.msg_queue = deque()

    def update(self, lines_complete):
        score = lines_complete * Settings.LEVEL_INFO[self.level-1]["score"]
        self.score += score

        self.msg_queue.append("+" + str(score))

        self.lines += lines_complete

        if self.lines >= 100:
            self.win = True

        for lvl in Settings.LEVEL_INFO[self.level:]:
            if self.lines >= lvl["lines"]:
                self.level = lvl["level"]

                self.msg_queue.append("level " + str(self.level))
            else:
                break


stats = Stats()
