class Game_Stats:
    def __init__(self, confg):
        self.confg = confg
        self.game_active = True
        self.reset_stats()
    def reset_stats(self):
        self.balls_left = self.confg.balls_limit