#importar librerias y subprogramas
#libreria pygame
import pygame
# subprograma/subcodigo engine(camaras, animaciones, hitbox, score, vidas, entidades)
import engine
# subprograma/subcodigo utils(degradado de letras y fondo, colocar texto en escena, crear enemigos, monedas, jugador)
import utils
# subprograma/subcodigo nivel(definir los niveles como una clase y si este esta perdido o ganado)
import nivel
# # subprograma/subcodigo scene(crear escenas(menu)del juego, selector de niveles, dibujo de texto en estos y transiciones)
import scene
# subprograma/subcodigo globals(lista de los niveles, constantes)
import globals
#  subprograma/subcodigo (situaciones de tecla del teclado(abajo, presionado, liberada)
import inputstream


# direccion del sprite del jugador
player_direction = "right"

# INICIAR
pygame.init()
# definir pantalla y tamañp
screen = pygame.display.set_mode(globals.SCREEN_SIZE)
# nombre del juego en la ventana de windows
pygame.display.set_caption("Project Team")
# define la tasa de fotogramas por segundo en el juego
clock = pygame.time.Clock()



# PLATAFORMAS --> hitbox plataforma(posicion x, posicion y, longitud x, longitud y)
platform = pygame.image.load("assets/plataforma.png")

#traer escena desde scene
sceneManager = scene.SceneManager()
#traer menus desde scene
mainMenu = scene.MainMenuScene()
# traer presionar boton desde scene/sceneManager
sceneManager.push(mainMenu)
# inputs predefido(controles del menu)
inputStream = inputstream.InputStream()

# crar jugador
# ENTIDAD JUGADOR(posX, posY)iniciales
globals.player1 = utils.makePlayer(300, 190)
# camara del jugador (posX, posY, ancho, alto) en relacion al jugador
globals.player1.camera = engine.Camera(0, 0, 1000, 560)
# posicionar camara del jugador en el mundo
globals.player1.camera.setWorldPos(300, 500)
# decirle a la camara que siga al jugador
globals.player1.camera.trackEntity(globals.player1)
# sistema de controles del jugador ( w=salto, s=abajo(sin uso), a=izquirda, d=derecha)
globals.player1.input = engine.Input(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)


# LOOP
running = True
#mientras corre
while running:

    # ver. salir (si le damos a la x de windows salimos del juego)
    for event in pygame.event.get():
        # si se produce el evento SALIR
        if event.type == pygame.QUIT:
            # el juego no se esta ejecutando
            running = False

    # sistema de input(controles)
    inputStream.processInput()
    #si no hay escenas...
    if sceneManager.isEmpty():
        #...el juego no se esta ejecutando
        running = False
    # comandos del escena
    sceneManager.input(inputStream)
    # actualizacion de escena
    sceneManager.update(inputStream)
    # dibujar escena en la pantalla
    sceneManager.draw(screen)

    # limitadortasa de fotogramas por segundos (60 fps)
    clock.tick(60)

# salir del programa
pygame.quit()