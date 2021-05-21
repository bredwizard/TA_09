import pygame
import engine
import utils

#optimizar crear texto (texto, posicion en y, posicion en x)
def drawText(t, x, y):
    text = font.render(t, True, AMARILLO, GRIS)
    # generar rectangulo de texto
    text_rectangle = text.get_rect()
    # posicion en X y Y del texto
    text_rectangle.topleft = (x, y)
    # poner en pantalla el texto
    screen.blit(text, text_rectangle)

# VARIABLES
# tamaño de pantalla
SCREEN_SIZE = (1000, 560)

# colores(red,green,blue)
GRIS = (50, 50, 50)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)


#direccion del sprite del jugador
player_direction = "right"

# INICIAR
pygame.init()
# definir pantalla y tamañp
screen = pygame.display.set_mode(SCREEN_SIZE)
# nombre del juego en la ventana de windows
pygame.display.set_caption("Project Team")
# define la tasa de fotogramas por segundo en el juego
clock = pygame.time.Clock()
# variable fuente de escritura por default
font = pygame.font.Font(pygame.font.get_default_font(), 24)

#estado de juego para ganar-perder
game_state = "playing"

entities = []

# velocidad inicial del jugador
player_speed = 0
# aceleracion del jugador
player_aceleracion = 0.2
# puntuacion
score = 0
# vidas iniciales
vidas = 3

# PLATAFORMAS --> hitbox plataforma(posicion x, posicion y, longitud x, longitud y)
platform = pygame.image.load("assets/plataforma.png")
platforms = [
    # plataforma media(izquierda a derecha)
    pygame.Rect(100, 300, 64, 64),
    pygame.Rect(164, 300, 64, 64),
    pygame.Rect(228, 300, 64, 64),
    pygame.Rect(292, 300, 64, 64),
    pygame.Rect(356, 300, 64, 64),
    pygame.Rect(420, 300, 64, 64),
    # plataforma de la izquierda
    pygame.Rect(100, 236, 64, 64),
    # plataforma de la derecha
    pygame.Rect(420, 236, 64, 64),
]

# LISTA DE IMAGENES
# moneda
coin = pygame.image.load("assets/objetos/moneda_0.png")
# imagen vidas
vida_image = pygame.image.load("assets/vida.png")

# ---------
# ENTIDADES
# ---------

# entidades de monedas
entities.append(utils.makeCoin(110, 185))
entities.append(utils.makeCoin(430, 185))

# ENTIDADES ENEMIGOS
enemy1 = utils.makeEnemy(170, 240)
enemy1.camera = engine.Camera(420,10,200,200)
entities.append(enemy1)

# ENTIDAD JUGADOR
player = utils.makePlayer(300, 190)
player.camera = engine.Camera(10, 10, 400, 400)
entities.append(player)

cameraSystem = engine.CameraSystem()

# LOOP
running = True
while running:

    # ------
    # INPUTS
    # ------

    # ver. salir (si le damos a la x de windows salimos del juego)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state  == "playing":

        # nuevas posiciones de personaje en X y Y (movimiento)
        new_player_x = player.position.rect.x
        new_player_y = player.position.rect.y

        # movimiento del jugador
        # variable para "tecla presionada"
        teclas = pygame.key.get_pressed()
        # ir a la izquierda = tecla A

        if teclas[pygame.K_a]:
            # velocidad traslacion izquierda
            new_player_x -= 2
            #direccion del sprite izquierda
            player.direction = "left"
            # estado del jugador = caminando
            player.state = "walking"

        # ir a la derecha = tecla D
        if teclas[pygame.K_d]:
            # velocidad traslacion derecha
            new_player_x += 2
            #direccion del sprite derecha
            player.direction = "right"
            # estado del jugador = caminando
            player.state = "walking"
        if not teclas[pygame.K_a] and not teclas[pygame.K_d]:
            player_state = "idle"


        # salto  = W (si esta en el suelo)
        if teclas[pygame.K_w] and player_on_ground:
            # velocidad salto
            player_speed = -7

    # ------
    # UPDATE
    # ------

    # si estamos jugando...
    if game_state == "playing":

        #actualizar animacion de las entidades
        for entity in entities:
            entity.animations.animationList[entity.state].update()


        # movimiento horizontal y colision (pocicion en x, posicion en y, longitud colision en x, longitud colision en y)
        new_player_rect = pygame.Rect(new_player_x, player.position.rect.y, player.position.rect.width, player.position.rect.height)
        # variable colisiones en x
        x_colision = False

        # verificar colision horizontal en la lista de plataformas
        for p in platforms:
            # "si colisiona con la hitbox del jugador en x..."
            if p.colliderect(new_player_rect):
                x_colision = True
                break

        # fin de la colision o no colision en x
        if x_colision == False:
            player.position.rect.x = new_player_x

        # movimiento vertical
        # "la velocidad aumenta a la tasa de la aceleracion en y"
        player_speed += player_aceleracion
        # la posicion aumenta a la tasa de la velocidad en y"
        new_player_y += player_speed

        # movimiento vertical y colision (pocicion en x, posicion en y, longitud colision en x, longitud colision en y)
        new_player_rect = pygame.Rect(int(player.position.rect.x), int(new_player_y), player.position.rect.width, player.position.rect.height)
        # variable colision en y
        y_colision = False
        # jugador en el suelo = falso
        player_on_ground = False

        # verificar colision vertical en la lista de plataformas
        for p in platforms:
            # "si colisiona con la hitbox del jugador en x..."
            if p.colliderect(new_player_rect):
                y_colision = True
                player_speed = 0
                # "si la plataforma esta debajo del jugador"
                if p[1] > new_player_y:
                    # mantener el jugador en la plataforma
                    player.position.rect.y = p[1] - player.position.rect.height
                    # jugador en el suelo = verdadero
                    player_on_ground = True
                break

        # fin de la colision o no colision en y
        if y_colision == False:
            # la hitbox del personaje es igual a la nueva posicion en y
            player.position.rect.y = int(new_player_y)

        # verificar si una moneda fue recolectada en las posiciones (posicion en x del jugador, posicion en y del jugador, ancho del jugador, altura del jugador)
        player_rect = pygame.Rect(int(player.position.rect.x),int(player.position.rect.y), player.position.rect.width, player.position.rect.height)

        #para las entidades en la lista de entidades
        for entity in entities:
            #si las entidades son del tipo cleccionables
            if entity.type == "coleccionable":
                # si el jugador colisiona con las entidades
                if entity.position.rect.colliderect(player_rect):
                    # remover la entidad
                    entities.remove(entity)
                    #sumar 1 al puntaje
                    score +=1
                    # si el puntaje es major a 2 ganar4e
                    if score >= 2:
                        game_state = "win"

        # sistema de enemigos
        # para las entidades en la lista de entidades
        for entity in entities:
            # si son del tipo peligrosos
            if entity.type == "dangerous":
                # si colisionamos con la entidad peligrosa
                if entity.position.rect.colliderect(player_rect):
                    # "restablecer posicion y velocidad"
                    player.position.rect.x = 300
                    player.position.rect.y = 190
                    player_speed = 0
                    # "...restar una vida"
                    vidas -= 1
                    # cambiar el estado del juego si no quedan vidas
                    if vidas <= 0:
                        #si nos quedamos sin vidas el estado del juego es "perder"
                        game_state = "lose"


    # ----
    # DRAW
    # ----

    # background y color
    screen.fill(GRIS)

    cameraSystem._update(screen, entities, platforms)

    # imagen de score "misma de coin"
    #screen.blit(coin, (10, 10))
    #drawText(str(score), 65, 35)

    # vidas
    #for l in range(vidas):
        # poner vidas en pantalla en X + repeticion cuantas vidas hayan, y
    #    screen.blit(vida_image, (10 + (l * 20), 65))

    # si ganamos o perdemos mostrar en pantalla:
    # si ganamos
    #if game_state == "win":
        # texto de victoria
    #    drawText("¡YOU WIN, CONGRATULATIONS!", 400, 50)
    # si perdemos
    #if game_state == "lose":
        # texto de derrota
    #    drawText("GAME OVER", 400, 50)


    # pantalla actual
    pygame.display.flip()

    # limitadortasa de fotogramas por segundos (60 fps)
    clock.tick(60)

# salir del programa
pygame.quit()

# coin sprite por DasBilligeAlien
# https://opengameart.org/content/rotating-coin-0

# sprite corazon por BenBushnell
# https://pixabay.com/es/illustrations/pixel-corazón-corazón-píxeles-2779422/