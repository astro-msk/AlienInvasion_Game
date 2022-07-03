
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():

    pygame.init()

    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    ship = Ship(screen,ai_settings)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings,screen,stats)
    play_button = Button(ai_settings,screen,"PLAY")

    pygame.display.set_caption("A L I E N    I N V A S I O N")

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)

        if stats.game_state :
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,sb,stats,aliens,bullets)
            gf.update_aliens(ai_settings,aliens,ship,bullets,stats,screen,sb)
        
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)


run_game()