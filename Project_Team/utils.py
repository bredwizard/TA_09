import pygame
import engine

# colores(red,green,blue)
NEGRO = (50, 50, 50)
AMARILLO = (255, 255, 0)

#lista de imagenes de monedas (cada una es una imagen de la animacion)
coin1 = pygame.image.load("assets/objetos/moneda_0.png")
coin2 = pygame.image.load("assets/objetos/moneda_1.png")
coin3 = pygame.image.load("assets/objetos/moneda_2.png")
coin4 = pygame.image.load("assets/objetos/moneda_3.png")
coin5 = pygame.image.load("assets/objetos/moneda_4.png")
coin6 = pygame.image.load("assets/objetos/moneda_5.png")
coin7 = pygame.image.load("assets/objetos/moneda_6.png")


# definir crear moneda
def makeCoin(x, y):
    # variable entidad
    entity = engine.Entity()
    # variable posicion de entidad (en x, en y, ancho, alto)
    entity.position = engine.Position(x, y,23,23)
    # animacion de la entidad desde el subprograma engine con la lista de imagenes de la moneda
    entityAnimation = engine.Animation([coin1,coin2,coin3,coin4,coin5,coin6,coin7])
    # 
    entity.animations.add("idle", entityAnimation)
    entity.type = "coleccionable"
    return entity

enemy0 = pygame.image.load("assets/esbirros/esbirros_1.png")
enemy1 = pygame.image.load("assets/esbirros/esbirros_2.png")

def makeEnemy(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, 92, 84)
    entityAnimation = engine.Animation([enemy0, enemy1])
    entity.animations.add("idle", entityAnimation)
    entity.type = "dangerous"
    return entity


idle0 = pygame.image.load("assets/alejo/alejo_1.png")

walking0 = pygame.image.load("assets/alejo/alejo_2.png")
walking1 = pygame.image.load("assets/alejo/alejo_3.png")

def makePlayer(x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x, y, 59, 104)
    entityIdleAnimation = engine.Animation([idle0])
    entityWalkingAnimation = engine.Animation([walking0, walking1])
    entity.animations.add("idle", entityIdleAnimation)
    entity.animations.add("walking", entityWalkingAnimation)
    entity.type = "player"
    return entity



