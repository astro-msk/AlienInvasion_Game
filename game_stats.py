class GameStats():

    def __init__(self,ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()

        self.high_score = 0

        self.game_state = False 
        ''' start in inactive state'''

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_life
        self.score = 0
        self.level = 1

