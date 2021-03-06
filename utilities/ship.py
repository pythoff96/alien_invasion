import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, settings, screen):
        """
        Initialize the ship and set its starting position.
        """
        super().__init__()
        self.settings = settings
        self.screen = screen

        self.image_path = self.settings.ship_image_path
        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ships position based on the movement flag
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        Center the ship on the screen.
        """
        self.center = self.screen_rect.centerx
