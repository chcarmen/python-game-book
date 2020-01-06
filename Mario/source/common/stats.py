class Stats:
    def __init__(self):
        self.reset_new_game()
        self.reset_current_game()

    def reset_new_game(self):
        self.score = 0
        self.coins = 0
        self.major_world = 1
        self.minor_world = 1

        self.life = 3

    def reset_current_game(self):
        self.time = 400
        self._elapsed = 0

    def update_timer(self, dt):
        self._elapsed += dt
        if self._elapsed >= 1:
            self.time -= int(self._elapsed)
            self._elapsed = 0

    def update_score_flagpole_height(self, y):
        if y >= 140:
            self.score += 2000
        elif 90 <= y < 140:
            self.score += 400
        elif 40 <= y < 90:
            self.score += 100


stats = Stats()
