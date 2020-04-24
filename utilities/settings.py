import random


class Settings:
    """
    A class to store all settings for Alien Invasion.
    """
    def __init__(self):
        """
        Initialize the game's settings.
        """
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_limit = 2

        # Bullet settings.
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30

        # alien_settings.
        self.fleet_drop_speed = 10

        # Game settings.
        self.speedup_scale = 1.1

        self.score_scale = 1.5
        self.ship_speed_factor = None
        self.bullet_speed_factor = None
        self.alien_speed_factor = None

        # fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = random.choice((-1, 1))
        # Reward of killing one alien.
        self.alien_reward = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game.
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = random.choice((-1, 1))
        # Reward of killing one alien.
        self.alien_reward = 50

    def increase_speed(self):
        """
        Increase speed settings.
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_reward = int(self.alien_reward * self.score_scale)