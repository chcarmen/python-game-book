class Stats:
    # Game states
    WELCOME, RUN, GAMEOVER, PAUSE = range(4)

    def __init__(self):
        self.state = Stats.WELCOME
        self.score = 0

    def reset(self):
        self.score = 0
