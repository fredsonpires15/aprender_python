import pygame
import sys


def check_events(ship):
    """ responde a eventos de pressionamento de teclas e de mouse."""
    """ Esta função verifica se houve um evento de fechar a janela (pygame.QUIT)
      e, se ocorreu, encerra o programa. Essa função será chamada repetidamente
      dentro do laço principal do jogo para garantir que os eventos sejam tratados adequadamente."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Tecla direita precionada")
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                print("Tecla esquerda precionada")
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            print("Event", event.type)
            if event.key == pygame.K_RIGHT:
                print("Tecla direita solta")
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                print("Tecla esquerda solta")
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """ Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # Deixa a tela mais recente visivel 
    pygame.display.flip()



