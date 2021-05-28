# importar librarias
import utils
import globals
import pygame
#imagen de plataformas
platform = pygame.image.load("assets/plataforma.png")

# crear clase SISTEMA
class System():
    # empezar a definir
    def __init__(self):
        pass
    # verificar entidad
    def check(self, entity):
        # reportar verdadesd
        return True
    # definir acualizacion de pantalla, entidades y plataformas
    def update(self, screen = None, inputStream = None):
        # para entidad en entidades
        for entity in globals.world.entities:
            # si se verifica la entidad
            if self.check(entity):
                # acualizar de pantalla , entidad, entidades y plataformas
                self.updateEntity(screen, inputStream, entity)
    # actualizar entidad(en pantalla, inputs, entidad)
    def updateEntity(self,screen, inputStream, entity):
        pass

# clase sistema de animaciones
class AnimationSystem(System):
    # verificar entidad
    def check(self, entity):
        # reportar verdad
        return entity.animations is not None
    # ctualizar entidad
    def updateEntity(self,screen, inputStream, entity):
        # desde la lista de animaciones para cada entidad
        entity.animations.animationList[entity.state].update()

# sistema de fisicas
class PhysicsSystem(System):
    # verificar sistema paraa las entidades
    def check(self, entity):
        # reportar verdad
        return entity.position is not None
    # actualizar entidades en pantalla, inputa y entidades
    def updateEntity(self,screen, inputStream, entity):
        # new_x = posicion de la entidad en el hitbox x
        new_x = entity.position.rect.x
        # new_y = posicion de la entidad en el hitbox y
        new_y = entity.position.rect.y


        if entity.intention is not None:
            # movimiento del jugador
            # ir a la izquierda = tecla A
            if entity.intention.moveLeft:
                # velocidad traslacion izquierda
                new_x -= 3
                # direccion del sprite izquierda
                entity.direction = "left"
                # estado del jugador = caminando
                entity.state = "walking"

            # ir a la derecha = tecla D
            if entity.intention.moveRight:
                # velocidad traslacion derecha
                new_x += 3
                # direccion del sprite derecha
                entity.direction = "right"
                # estado del jugador = caminando
                entity.state = "walking"
            if not entity.intention.moveLeft and not entity.intention.moveRight:
                entity.state = "idle"

            # salto  = W (si esta en el suelo)
            if entity.intention.jump and entity.on_ground:
                # velocidad salto
                entity.speed = -7

        # movimiento horizontal y colision (pocicion en x, posicion en y, longitud colision en x, longitud colision en y)
        new_x_rect = pygame.Rect(
            int(new_x),
            int(entity.position.rect.y),
            entity.position.rect.width,
            entity.position.rect.height)

        # variable colisiones en x
        x_colision = False

        # verificar colision horizontal en la lista de plataformas
        for platform in globals.world.platforms:
            # "si colisiona con la hitbox del jugador en x..."
            if platform.colliderect(new_x_rect):
                x_colision = True
                break

        # fin de la colision o no colision en x
        if x_colision == False:
            entity.position.rect.x = new_x

        # movimiento vertical
        # "la velocidad aumenta a la tasa de la aceleracion en y"
        entity.speed += entity.aceleracion
        # la posicion aumenta a la tasa de la velocidad en y"
        new_y += entity.speed

        # movimiento vertical y colision (pocicion en x, posicion en y, longitud colision en x, longitud colision en y)
        new_y_rect = pygame.Rect(
            int(entity.position.rect.x),
            int(new_y),
            entity.position.rect.width,
            entity.position.rect.height)
        # variable colision en y
        y_colision = False
        # jugador en el suelo = falso
        entity.on_ground = False

        # verificar colision vertical en la lista de plataformas
        for platform in globals.world.platforms:
            # "si colisiona con la hitbox del jugador en x..."
            if platform.colliderect(new_y_rect):
                y_colision = True
                entity.speed = 0
                # "si la plataforma esta debajo del jugador"
                if platform[1] > new_y:
                    # mantener el jugador en la plataforma
                    entity.position.rect.y = platform[1] - entity.position.rect.height
                    # jugador en el suelo = verdadero
                    entity.on_ground = True
                break

        # fin de la colision o no colision en y
        if y_colision == False:
            # la hitbox del personaje es igual a la nueva posicion en y
            entity.position.rect.y = int(new_y)

        #resetear intenciones
        # si las intenciones no es ninguna
        if entity.intention is not None:
            # los movimientos en cualquier direccion ( arriba, derecha, izquierda) son falsos
            entity.intention.moveLeft = False
            entity.intention.moveRight = False
            entity.intention.jump = False

class InputSystem(System):
    def check(self, entity):
        return entity.input is not None and entity.intention is not None
    def updateEntity(self, screen, inputStream, entity):
        # up = saltar
        if inputStream.keyboard.isKeyDown(entity.input.up):
            entity.intention.jump = True
        else:
            entity.intention.jump = False
        # left = caminar izquierda
        if inputStream.keyboard.isKeyDown(entity.input.left):
            entity.intention.moveLeft = True
        else:
            entity.intention.moveLeft = False
        # derecha = mover derecha
        if inputStream.keyboard.isKeyDown(entity.input.right):
            entity.intention.moveRight = True
        else:
            entity.intention.moveRight = False

class CollectionSystem(System):
    # verificar entidad
    def check(self, entity):
        # reportar verdadesd
        return entity.type == "player" and entity.score is not None
    # actualizar entidad en pantalla, con los inputs y las entidades
    def updateEntity(self,screen, inputStream, entity):
        # para otras entidades en la lista de entidades en el mundo
        for otherEntity in globals.world.entities:
            # si otras entidades no son entidades son del tipo coleccionable
            if otherEntity is not entity and otherEntity.type == "coleccionable":
                # si se colisiona con la otra entidad
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    # entity.collectable.onCollide(entity, otherEntity)
                    # si hay colision
                    globals.world.entities.remove(otherEntity)
                     # sumar 1 al puntaje
                    entity.score.score += 1

# sitema de batalla
class BattleSystem(System):
    # verificar entidad
    def check(self, entity):
        # reportar verdadesd
        return entity.type == "player" and entity.battle is not None
    # actualizacion de entidad en pantalla, con los inputs y las entidades
    def updateEntity(self,screen, inputStream, entity):
        # para otras entidades en la lista de entidades
        for otherEntity in globals.world.entities:
            # si otras entidades no es la entidad y es del tipo peligroso
            if otherEntity is not entity and otherEntity.type == "dangerous":
                # si colisionamos
                if entity.position.rect.colliderect(otherEntity.position.rect):
                    # restablecer posiciones en x y y, velocidad
                    entity.position.rect.x = 300
                    entity.position.rect.y = 190
                    entity.speed = 0
                    # "...restar una vida"
                    entity.battle.lives -= 1


# crear clase de sistema de camaras
class CameraSystem(System):
    def check(self, entity):
        return entity.camera is not None
    def updateEntity(self, screen, inputStream, entity):

        # hacer rectangulo de camara
        cameraRect = entity.camera.rect
        clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
        screen.set_clip(clipRect)

        # actualizar camara si esta siguiendo la entidad
        if entity.camera.entityToTrack is not None:

            trackedEntity = entity.camera.entityToTrack

            currentX = entity.camera.worldX
            currentY = entity.camera.worldY

            targetX = trackedEntity.position.rect.x + trackedEntity.position.rect.w/2
            targetY = trackedEntity.position.rect.y + trackedEntity.position.rect.h/2
            #velocidad de delay en el seguimiento de la camara
            entity.camera.worldX = (currentX * 0.92) + (targetX * 0.08)
            entity.camera.worldY = (currentY * 0.92) + (targetY * 0.08)

            # calcular bordes de la camara(offsets)
        # borde en x = rectangulo camara en x + la mitad de el ancho del rect de camara - la entidad de la camara en x
        offsetX = cameraRect.x + cameraRect.w/2 - entity.camera.worldX
        # borde en x = rectangulo camara en y + la mitad de la altura del rect de camara - la entidad de la camara en y
        offsetY = cameraRect.y + cameraRect.h/2 - entity.camera.worldY

        #color fondo de pantalla camara
        screen.fill(globals.GRIS)

        # renderizar plataformas
        for p in globals.world.platforms:
            newPosRect = pygame.Rect(p.x + offsetX, p.y + offsetY, p.w, p.h)
            screen.blit(platform, (newPosRect))

        #renderizar entidades
        for e in globals.world.entities:
            s = e.state
            a = e.animations.animationList[s]
            a.draw(screen, e.position.rect.x + offsetX, e.position.rect.y + offsetY, e.direction == "right", False)

            #HUD del jugador

            # PUNTAJE
            if entity.score is not None:
                screen.blit(utils.coin1, (entity.camera.rect.x + 10, entity.camera.rect.y + 10))
                utils.drawText(screen, str(entity.score.score), entity.camera.rect.x + 65, entity.camera.rect.y + 35, globals.BLANCO,255)

            # VIDAS
            if entity.battle is not None:
                for l in range(entity.battle.lives):
                    # poner vidas en pantalla en X + repeticion cuantas vidas hayan, y
                    screen.blit(utils.vida_image, (entity.camera.rect.x + 10 + (l * 20), entity.camera.rect.y + 65))


        # deshacer rectangulo de camara
        screen.set_clip(None)

class Camera:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.worldX = 0
        self.worldY = 0
        self.entityToTrack = None
    def  setWorldPos(self, x, y):
        self.worldX = x
        self.worldY = y
    def trackEntity(self,e):
        self.entityToTrack = e

#posiciones
class Position():
    # construir clase posicion
    def __init__(self, x, y, w, h):
        # rectangulo (pos x, pos y, ancho, alto),
        self.rect = pygame.Rect(x, y, w, h)

#clase Animaciones
class Animations():
    def __init__(self):
        self.animationList = {}
    def add(self, state, animation):
        self.animationList[state] = animation

# -----------
# ANIMACION
# -----------

# construir clase ANIMACION
class Animation:
    def __init__(self, imageList):
        # definir la lista de imagenes
        self.imageList = imageList
        # definir el ingreso de imagenes
        self.imageIndex = 0
        # cronometro de la animacion
        self.animationTimer = 0
        # velocidad de la animacion (fps)
        self.animationSpeed = 10
    # ACTUALIZACION DE ANIMACION
    def update(self):
        # agregar una unidad al tiempo
        self.animationTimer += 1
        # cuando la velocidad de animacion sea mayor al tiempo de animacion
        if self.animationTimer > self.animationSpeed:
            # que el cronometro vuelva a 0
            self.animationTimer = 0
            # mostrar una nueva imagen
            self.imageIndex += 1
            # si la secuencia de imagenes que ya se han ingresado es mayor a la de la lista...
            if self.imageIndex > len(self.imageList) - 1 :
                # se vuelve a la primera imagen anexada
                self.imageIndex = 0
    # dibujar imagen en la pantalla en las pociciones X y Y
    def draw(self,screen, x, y, flipX, flipY):
        screen.blit(pygame.transform.flip(self.imageList[self.imageIndex], flipX, flipY), (x, y))

# --------
#ENTIDADES
# --------

class Score():
    # construir clase posicion
    def __init__(self):
        # rectangulo (pos x, pos y, ancho, alto),
        self.score = 0

class Battle:
    # construir clase batalla
    def __init__(self):
        # rectangulo (pos x, pos y, ancho, alto),
        self.lives = 3

class Input:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right


class Intention:
    def __init__(self):
        self.moveLeft = False
        self.moveRight = False
        self.jump = False


def resetEntity(entity):
    pass


#construir clase entidades, los self.algo son las propiedades de este
class Entity:
    def __init__(self):
        #estado "quieto"
        self.state = "idle"
        #estado "normal"
        self.type = "normal"
        #posicion = ninguna
        self.position = None
        #animacion = en animaciones
        self.animations = Animations()
        #direccion de animaciones  = derecha
        self.direction = "right"
        # camara = ninguna
        self.camera = None
        # propiedad puntuacion
        self.score = None
        # propiedad batalla
        self.battle = None
        # propiedad velocidad
        self.speed = 0
        # propiedad input
        self.input = None
        # propiedad intencion por defecto ninguna
        self.intention = None
        # propiedad en el suelo por defecto falsa
        self.on_ground = False
        # aceleracion del jugador inicial = 0
        self.aceleracion = 0
        # propiedad resetear entidad
        self.reset = resetEntity