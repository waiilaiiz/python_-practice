
import pygame
# from pygame.locals import*

class Ship():
    """docstring for ClassName"""
    def __init__(self,ai_settings, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)

        self.move_right = False
        self.move_left  = False
        self.move_top   = False
        self.move_bottom = False


        self.ai_settings = ai_settings

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            pass
        elif self.move_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        elif self.move_top and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        elif self.move_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # pass
