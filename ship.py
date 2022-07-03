import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,screen,ai_settings):

        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.moving_right=False
        self.moving_left=False
        self.image=pygame.image.load('images/ship.bmp') # importing ship's image into screen

        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        ''' positioning the ship at center bottom'''
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.center=float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.center<self.screen_rect.right:
            self.center += 1*self.ai_settings.ship_speed_factor
        if self.moving_left and self.center>0:
            self.center -=1*self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        
        self.screen.blit(self.image,self.rect) # drawing the image

    def center_ship(self):

        self.center = self.screen_rect.centerx