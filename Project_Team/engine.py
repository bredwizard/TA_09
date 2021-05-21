import pygame
BLANCO = (255, 255, 255)

#imagen de plataformas
platform = pygame.image.load("assets/plataforma.png")

# crear clase SISTREM
class System():
    # empezar a definir
    def __init__(self):
        pass
    # verificar entidad
    def check(self, entity):
        # reportar verdadesd
        return True
    # definir acualizacion de pantalla, entidades y plataformas
    def update(self, screen,entities, platforms):
        # para entidad en entidades
        for entity in entities:
            # si se verifica la entidad
            if self.check(entity):
                # acualizar de pantalla , entidad, entidades y plataformas
                self.updateEntity(screen, entity, entities, platforms)
    def updateEntity(self,screen, entity, entities, platforms):
        pass

# crear clase de sistema de camaras
class CameraSystem(System):
    def __init__(self):
        super().__init__()
    def check(self, entity):
        return entity.camera is not None
    def updateEntity(self,screen, entity,entities, platforms):

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
        screen.fill(BLANCO)

        # renderizar plataformas
        for p in platforms:
            newPosRect = pygame.Rect(p.x + offsetX, p.y + offsetY, p.w, p.h)
            screen.blit(platform, (newPosRect))

        #renderizar entidades
        for e in entities:
            s = e.state
            a = e.animations.animationList[s]
            a.draw(screen, e.position.rect.x + offsetX, e.position.rect.y + offsetY, e.direction == "right", False)

        # deshacer rectangulo de camara
        screen.set_clip(None)

class Camera():
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
class Animation():
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
#construir clase entidades
class Entity():
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