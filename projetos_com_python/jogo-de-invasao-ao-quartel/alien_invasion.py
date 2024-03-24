import pygame 
from pygame.locals import QUIT
from settings import Settings
from ship import Ship
import game_functions as gf 

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Invasão Ao Quartel")
    clock = pygame.time.Clock()

    # Criar uma espaçonave 
    ship = Ship(screen)

    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        
        clock.tick(60)
