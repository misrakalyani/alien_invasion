class GameStats():
    # Track the statistics for Alien Invasion
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        "Initialize statistics that can change anytime during the game."
        self.ships_left = self.ai_settings.ship_limit
        # Resets the score everytime game starts.
        self.score = 0
        self.level = 1
        
