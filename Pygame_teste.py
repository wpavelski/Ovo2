import pygame


#Iniciar Pygame
pygame.init()

#Criando Tela do Jogo
screen = pygame.display.set_mode((800,600))

#Título
pygame.display.set_caption("Space Invaders")

#Loop pra rodar o jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False