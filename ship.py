import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        #Initialize ship and it's starting position.
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Load ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Created an attribute to store decimal value for ship's center.
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        # Center the ship on the screen.
        self.center = self.screen_rect.centerx
    def update(self):
        #Update ship center value not the rect value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        #Draw the ship at it's current locatiom.
        self.screen.blit(self.image, self.rect)
