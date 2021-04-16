#importar librerias
import pygame, sys

# logo y nombre del programa
icon = pygame.image.load("gato.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("project team")

# definir la pantalla y tamaño y cambio de color(RGB)
size = (720,480)
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))
pygame.display.update()

#background
background = pygame.image.load("escenario_1.png")
screen.blit(background(0,0))

# bucle de repeticion(va al final)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()