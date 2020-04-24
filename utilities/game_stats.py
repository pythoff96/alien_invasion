class GameStats:
    """
    Track statistics for Alien Invasion.
    """

    def __init__(self, ai_game):
        """
        Initialize statistics.
        """
        self.settings = ai_game.settings
        self.game_active = False
        self.high_score = 0

        self.ships_left = None
        self.score = None
        self.level = None

        self.reset_stats()

    def reset_stats(self):
        """
        Initialize statistics that can change during the game.
        """
        self.ships_left = self.settings.ship_limit
        self.settings.initialize_dynamic_settings()
        self.score = 0
        self.level = 1
