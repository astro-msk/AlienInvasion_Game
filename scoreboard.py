from this import s
from turtle import Screen
import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():

    def __init__(self,ai_settings,screen,stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):

        rounded_score = int(round(self.stats.score,-1))
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):

        high_score = int(round(self.stats.high_score))
        hs_str = "High Score: " + "{:,}".format(high_score)
        self.hs_img = self.font.render(hs_str,True,self.text_color,self.ai_settings.bg_color)

        self.hs_rect = self.hs_img.get_rect()
        self.hs_rect.top = 20
        self.hs_rect.centerx = self.screen_rect.centerx

    def prep_level(self):

        lvl = self.stats.level
        lvl_str = "Level: " + str(lvl)
        self.lvl_img = self.font.render(lvl_str,True,self.text_color,self.ai_settings.bg_color)

        self.lvl_img_rect = self.lvl_img.get_rect()
        self.lvl_img_rect.top = 20
        self.lvl_img_rect.right = self.score_rect.left - 100
    
    def prep_ships(self):

        self.ships = Group()
        for ship_no in range(self.stats.ships_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.x = 10 + ship_no * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):

        self.screen.blit(self.score_img,self.score_rect)
        self.screen.blit(self.hs_img,self.hs_rect)
        self.screen.blit(self.lvl_img,self.lvl_img_rect)
        self.ships.draw(self.screen)