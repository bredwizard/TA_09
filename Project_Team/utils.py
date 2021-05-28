# importar librerias (explicado en main.py)
import pygame
import engine



# variables de color RGB(red, green, blue)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)
GRIS = (50, 50, 50)

# variable fuente de escritura por default
# iniciar fuentes de pygame
pygame.font.init()
# fuente = fuentes de pygame(fuente por defecto, tamaño fuente = 24)
font = pygame.font.Font(pygame.font.get_default_font(), 24)

# -----------------------------------------------------------------------
# letras opacas
# https://nerdparadise.com/programming/pygameblitopacity
# opacar imagen
def blit_alpha(target, source, location, opacity):
    # localizacion en x
    x = location[0]
    # localizacion en y
    y = location[1]
    # temp = suoerfucie(ancho, alto= convertir
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    # mostrar
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)
# -----------------------------------------------------------------------

# optimizar crear texto (texto, posicion en y, posicion en x)
def drawText(screen, t, x, y, fg, alpha):
    text = font.render(t, True, fg, alpha)
    # generar rectangulo de texto
    text_rectangle = text.get_rect()
    # posicion en X y Y del texto
    text_rectangle.topleft = (x, y)
    # degradado en pantalla para texto en x y y y con alpha
    blit_alpha(screen, text, (x,y), alpha)

# imagen de corazon
vida_image = pygame.image.load("assets/vida.png")

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
    # añadir a la moneda el estado de estatico
    entity.animations.add("idle", entityAnimation)
    # decir que la moneda es de tipo coleccionable
    entity.type = "coleccionable"
    # terminar propiedades de la moneda
    return entity

# imagen de los enemigos
enemy0 = pygame.image.load("assets/esbirros/esbirros_1.png")
enemy1 = pygame.image.load("assets/esbirros/esbirros_2.png")

# crear enemigos
def makeEnemy(x, y):
    # decir que es una entidad
    entity = engine.Entity()
    # definir posiciones en x y y(variables) altura y anchura
    entity.position = engine.Position(x, y, 36, 63)
    # animacion del enmigo con las imagenes antes cargadas
    entityAnimation = engine.Animation([enemy0, enemy1])
    # decir que es estatico
    entity.animations.add("idle", entityAnimation)
    # decir que es del tipo peligroso
    entity.type = "dangerous"
    # terminar de darle propiedades
    return entity

mariana0 = pygame.image.load("assets/mariana/mariana_1.png")

def makeEnemy_2(x, y):
    # decir que es una entidad
    entity = engine.Entity()
    # definir posiciones en x y y(variables) altura y anchura
    entity.position = engine.Position(x, y, 40, 64)
    # animacion del enmigo con las imagenes antes cargadas
    entityAnimation = engine.Animation([mariana0])
    # decir que es estatico
    entity.animations.add("idle", entityAnimation)
    # decir que es del tipo peligroso
    entity.type = "dangerous"
    # terminar de darle propiedades
    return entity

nea0 = pygame.image.load("assets/nea/nea_1.png")
nea1 = pygame.image.load("assets/nea/nea_2 (1).png")

def makeEnemy_3(x, y):
    # decir que es una entidad
    entity = engine.Entity()
    # definir posiciones en x y y(variables) altura y anchura
    entity.position = engine.Position(x, y, 40, 96)
    # animacion del enmigo con las imagenes antes cargadas
    entityAnimation = engine.Animation([nea0, nea1])
    # decir que es estatico
    entity.animations.add("idle", entityAnimation)
    # decir que es del tipo peligroso
    entity.type = "dangerous"
    # terminar de darle propiedades
    return entity

pipe = pygame.image.load("assets/personajes/pipe_11.png")

def makeEnemy_pipe(x, y):
    # decir que es una entidad
    entity = engine.Entity()
    # definir posiciones en x y y(variables) altura y anchura
    entity.position = engine.Position(x, y, 128, 128)
    # animacion del enmigo con las imagenes antes cargadas
    entityAnimation = engine.Animation([pipe])
    # decir que es estatico
    entity.animations.add("idle", entityAnimation)
    # terminar de darle propiedades
    return entity

motor = pygame.image.load("assets/personajes/dios hecho gato.png")

def makeEnemy_motor(x, y):
    # decir que es una entidad
    entity = engine.Entity()
    # definir posiciones en x y y(variables) altura y anchura
    entity.position = engine.Position(x, y, 53, 46)
    # animacion del enmigo con las imagenes antes cargadas
    entityAnimation = engine.Animation([motor])
    # decir que es estatico
    entity.animations.add("idle", entityAnimation)
    # decir que es del tipo peligroso

    # terminar de darle propiedades
    return entity

# imagen personajes estatico
idle0 = pygame.image.load("assets/alejo/alejo_1.png")
#imagenes personaje caminando
walking0 = pygame.image.load("assets/alejo/alejo_2.png")
walking1 = pygame.image.load("assets/alejo/alejo_3.png")

# definir resetear jugador al acabar un nivel
def resetPlayer(entity):
    # el score al resetear es 0
    entity.score.score = 0
    # el score vuelve a = 3
    entity.battle.lives = 3
    # restablecer posicion en x a 300
    entity.position.rect.x =300
    # restablecer posicion en y a 190
    entity.position.rect.y = 190
    # restablecer velocidad del jugador a 0
    entity.speed = 0
    # restablecer aceleracion del jugador a 0.2
    entity.aceleracion = 0.2
    # restablecer posicion de la camara en el mundo
    entity.camera.setWorldPos(300, 500)


# definir crear jugador
def makePlayer(x, y):
    # es de clase entidad
    entity = engine.Entity()
    # establecer posicion (x y y variables dependiendo de los inputs de la persona) ancho y alto
    entity.position = engine.Position(x, y, 59, 104)
    # animacion del jugador estatico
    entityIdleAnimation = engine.Animation([idle0])
    # animacion del jugador en movimiento
    entityWalkingAnimation = engine.Animation([walking0, walking1])
    # estado del jugador quieto
    entity.animations.add("idle", entityIdleAnimation)
    # estado del jugador caminando
    entity.animations.add("walking", entityWalkingAnimation)
    # el score del jugador se aloja en el subprograma engine.Score
    entity.score = engine.Score()
    # la situacion de batalla se laoja en engine
    entity.battle = engine.Battle()
    # intencion del jugador
    entity.intention = engine.Intention()
    #acelaracion del jugador
    entity.aceleracion = 0.2
    # tipo de la entidad es jugador
    entity.type = "player"
    # resetear la entidad al entrar en el menu
    entity.reset = resetPlayer
    # terminar definir
    return entity