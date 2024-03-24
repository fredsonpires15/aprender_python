import pygame
import sys
import matplotlib.pyplot as plt

event_data = []

class Ship():

    

    def __init__(self, screen):
        """ inicializa a espacionave e defina sua posição inicial"""
        self.screen = screen  # carrega imagem da espaçonave e obtém seu rect
        self.imagem = pygame.image.load('nave_grande.png')
        self.rect = self.imagem.get_rect()
        self.screen_rect = screen.get_rect()  

        # inicia cada espaçonave na parte inferior central da screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # flag de movimento para controlar o movimento da espaconave
        self.moving_right = False 
        self.moving_left = False

 
    def update(self):
        """ Atualiza a posição da espaçonave de acordo com a flag de movimento  """

        if self.moving_right:  # Esta função move a espacionave para a direita se a flag for True
            self.rect.centerx += 1
            event_data.append(self.rect.centerx)
            with open("ficheiro_de_jogo.txt", "w") as ficheiro:
                ficheiro.write(f"{event_data}")
            print(self.rect.centerx)

        if self.moving_left:  # Esta função move a espacionave para a esquerda se a flag for True
            self.rect.centerx -= 1
            event_data.append(self.rect.centerx)
        
        if self.moving_left and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0: 
            self.center -= self.ai_settings.ship_speed_factor
        
        

    def blitme(self):
        self.screen.blit(self.imagem, self.rect)


    


