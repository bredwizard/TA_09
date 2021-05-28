#imporat librarias y subprogramas
import globals
import pygame
import utils

# definir nivel
class Level:
    # se definen a el mismo, plataformas, entidades, ganar y perder
    def __init__(self, platforms = None, entities = None, winFunc = None, loseFunc = None):
        # definir plataformas
        self.platforms = platforms
        # definir entidades
        self.entities = entities
        # definir ganar
        self.winFunc = winFunc
        # definir perder
        self.loseFunc = loseFunc
    # definir ganar
    def isWon(self):
        # si no se ah ganado aun:
        if self.winFunc is None:
            # decir que es falso haber ganado
            return False
        # de lo contrario decir que se ah ganado
        return self.winFunc(self)
    # definir perder
    def isLost(self):
        # si no se ah perdido
        if self.loseFunc is None:
            #decir que es falso
            return False
        # de lo contrario se ah perdido
        return self.loseFunc(self)

# perder si el jugador no tiene vidas
def lostLevel(level):
    # para entidades en nivel/entidades
    for entity in level.entities:
        # si la entidad es el jugador
        if entity.type == "player":
            # si el jugador esta en batalla(batalla es no no)(no no=si)
            if entity.battle is not None:
                # si quedan vidas
                if entity.battle.lives > 0:
                    # perder es falso
                    return False
    # perder es cierto(nivel perdido)
    return True

# ganar si el score es 2
def wonLevel(level):
    # para las entidades en las entidades del nivel
    for entity in level.entities:
        # si para entidades de tipo coleccionable
        if entity.type == "coleccionable":
            # osea el nivel es ganado si no hay entidades de tipo coleccionables(monedas)
            return False

    # si no devolver falso
    return True


# -------
# niveles
# -------
# los comentarios del nivel uno sirven para todos los niveles
# definir cargar nivel
def loadLevel(levelNumber):
    # numero de nivel
    if levelNumber == 1:
        # cargar nivel 1
        globals.world = Level(
            #plataformas(cubos) en el nivel pos x, pos y
            platforms = [
                # cubo principal-----------------------------------
                # plataforma media(izquierda a derecha)((posX, posY, ancho, alto))
                pygame.Rect(100, 300, 64, 64),
                pygame.Rect(164, 300, 64, 64),
                pygame.Rect(228, 300, 64, 64),
                pygame.Rect(292, 300, 64, 64),
                pygame.Rect(356, 300, 64, 64),
                pygame.Rect(420, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(548, 300, 64, 64),
                pygame.Rect(612, 300, 64, 64),
                pygame.Rect(676, 300, 64, 64),
                pygame.Rect(740, 300, 64, 64),
                pygame.Rect(804, 300, 64, 64),
                pygame.Rect(868, 300, 64, 64),
                pygame.Rect(932, 300, 64, 64),
                pygame.Rect(996, 300, 64, 64),
                pygame.Rect(1060, 300, 64, 64),
                pygame.Rect(1124, 300, 64, 64),
                pygame.Rect(1188, 300, 64, 64),
                #plataforma horizontal arriba
                pygame.Rect(100, -852, 64, 64),
                pygame.Rect(164, -852, 64, 64),
                pygame.Rect(228, -852, 64, 64),
                pygame.Rect(292, -852, 64, 64),
                pygame.Rect(356, -852, 64, 64),
                pygame.Rect(420, -852, 64, 64),
                pygame.Rect(484, -852, 64, 64),
                pygame.Rect(548, -852, 64, 64),
                pygame.Rect(612, -852, 64, 64),
                pygame.Rect(676, -852, 64, 64),
                pygame.Rect(740, -852, 64, 64),
                pygame.Rect(804, -852, 64, 64),
                pygame.Rect(868, -852, 64, 64),
                pygame.Rect(932, -852, 64, 64),
                pygame.Rect(996, -852, 64, 64),
                pygame.Rect(1060, -852, 64, 64),
                pygame.Rect(1124, -852, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # plataforma de la izquierda((posX, posY, ancho, alto))
                pygame.Rect(100, 236, 64, 64),
                pygame.Rect(100, 172, 64, 64),
                pygame.Rect(100, 108, 64, 64),
                pygame.Rect(100, 44, 64, 64),
                pygame.Rect(100, -20, 64, 64),
                pygame.Rect(100, -84, 64, 64),
                pygame.Rect(100, -148, 64, 64),
                pygame.Rect(100, -212, 64, 64),
                pygame.Rect(100, -276, 64, 64),
                pygame.Rect(100, -340, 64, 64),
                pygame.Rect(100, -404, 64, 64),
                pygame.Rect(100, -468, 64, 64),
                pygame.Rect(100, -532, 64, 64),
                pygame.Rect(100, -596, 64, 64),
                pygame.Rect(100, -660, 64, 64),
                pygame.Rect(100, -724, 64, 64),
                pygame.Rect(100, -788, 64, 64),
                pygame.Rect(100, -852, 64, 64),
                # plataforma de la derecha((posX, posY, ancho, alto))
                pygame.Rect(1188, 236, 64, 64),
                pygame.Rect(1188, 172, 64, 64),
                pygame.Rect(1188, 108, 64, 64),
                pygame.Rect(1188, 44, 64, 64),
                pygame.Rect(1188, -20, 64, 64),
                pygame.Rect(1188, -84, 64, 64),
                pygame.Rect(1188, -148, 64, 64),
                pygame.Rect(1188, -212, 64, 64),
                pygame.Rect(1188, -276, 64, 64),
                pygame.Rect(1188, -340, 64, 64),
                pygame.Rect(1188, -404, 64, 64),
                pygame.Rect(1188, -468, 64, 64),
                pygame.Rect(1188, -532, 64, 64),
                pygame.Rect(1188, -596, 64, 64),
                pygame.Rect(1188, -660, 64, 64),
                pygame.Rect(1188, -724, 64, 64),
                pygame.Rect(1188, -788, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
             # fin cuadro principal-----------------------
             # plataformoas especificas del nivel---------
                pygame.Rect(164, -20, 64, 64),
                pygame.Rect(228, -20, 64, 64),
                pygame.Rect(292, -20, 64, 64),
                pygame.Rect(356, -20, 64, 64),
                pygame.Rect(420, -20, 64, 64),
                pygame.Rect(484, -20, 64, 64),
                pygame.Rect(548, -20, 64, 64),
                pygame.Rect(612, -20, 64, 64),
                pygame.Rect(676, -20, 64, 64),
                pygame.Rect(740, -20, 64, 64),
                pygame.Rect(804, -20, 64, 64),
                pygame.Rect(868, -20, 64, 64),
                pygame.Rect(996, 236, 64, 64),
                pygame.Rect(1060, 172, 64, 64),
                pygame.Rect(1124, 108, 64, 64),
                pygame.Rect(932, 44, 64, 64),

                pygame.Rect(164, -212, 64, 64),
                pygame.Rect(228, -148, 64, 64),
                pygame.Rect(292, -84, 64, 64),
                pygame.Rect(356, -276, 64, 64),
                pygame.Rect(420, -340, 64, 64),
                pygame.Rect(484, -340, 64, 64),
                pygame.Rect(548, -340, 64, 64),
                pygame.Rect(612, -340, 64, 64),
                pygame.Rect(676, -340, 64, 64),
                pygame.Rect(740, -340, 64, 64),
                pygame.Rect(804, -340, 64, 64),
                pygame.Rect(868, -340, 64, 64),
                pygame.Rect(932, -340, 64, 64),
                pygame.Rect(996, -340, 64, 64),
                pygame.Rect(1060, -340, 64, 64),
                pygame.Rect(1124, -340, 64, 64),

                pygame.Rect(164, -660, 64, 64),
                pygame.Rect(228, -660, 64, 64),
                pygame.Rect(292, -660, 64, 64),
                pygame.Rect(356, -660, 64, 64),
                pygame.Rect(420, -660, 64, 64),
                pygame.Rect(484, -660, 64, 64),
                pygame.Rect(548, -660, 64, 64),
                pygame.Rect(612, -660, 64, 64),
                pygame.Rect(676, -660, 64, 64),
                pygame.Rect(740, -660, 64, 64),
                pygame.Rect(804, -660, 64, 64),
                pygame.Rect(868, -660, 64, 64),
                pygame.Rect(932, -596, 64, 64),
                pygame.Rect(996, -404, 64, 64),
                pygame.Rect(1060, -468, 64, 64),
                pygame.Rect(1124, -532, 64, 64),




             #--------------------------------------------
            ],
            # entidades en el nivel pos x, pos y
            entities = [
                #monedas pos x, pos y
                utils.makeCoin(500, 150),
                utils.makeCoin(750, -224),
                utils.makeCoin(550, -500),
                utils.makeCoin(700, -403),
                utils.makeCoin(400, -83),
                utils.makeCoin(600, -83),
                utils.makeCoin(550, -720),
                utils.makeCoin(164, -720),
                utils.makeCoin(164, -784),
                utils.makeCoin(228, -720),
                utils.makeCoin(228, -784),
                # enemigos pos x, pos y
                utils.makeEnemy_2(500, 237),
                utils.makeEnemy_2(750, -83),
                utils.makeEnemy_2(550, -403),
                #varios
                utils.makeEnemy_pipe(170, 237),
                utils.makeEnemy_motor(240, 247),


                # jugador
                globals.player1

            ],
            # ganar
            winFunc = wonLevel,
            # perder
            loseFunc = lostLevel
        )
    if levelNumber == 2:
        # cargar nivel 2
        globals.world = Level(
            platforms = [
                # cubo principal-----------------------------------
                # plataforma media(izquierda a derecha)((posX, posY, ancho, alto))
                pygame.Rect(100, 300, 64, 64),
                pygame.Rect(164, 300, 64, 64),
                pygame.Rect(228, 300, 64, 64),
                pygame.Rect(292, 300, 64, 64),
                pygame.Rect(356, 300, 64, 64),
                pygame.Rect(420, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(548, 300, 64, 64),
                pygame.Rect(612, 300, 64, 64),
                pygame.Rect(676, 300, 64, 64),
                pygame.Rect(740, 300, 64, 64),
                pygame.Rect(804, 300, 64, 64),
                pygame.Rect(868, 300, 64, 64),
                pygame.Rect(932, 300, 64, 64),
                pygame.Rect(996, 300, 64, 64),
                pygame.Rect(1060, 300, 64, 64),
                pygame.Rect(1124, 300, 64, 64),
                pygame.Rect(1188, 300, 64, 64),
                # plataforma horizontal arriba
                pygame.Rect(100, -852, 64, 64),
                pygame.Rect(164, -852, 64, 64),
                pygame.Rect(228, -852, 64, 64),
                pygame.Rect(292, -852, 64, 64),
                pygame.Rect(356, -852, 64, 64),
                pygame.Rect(420, -852, 64, 64),
                pygame.Rect(484, -852, 64, 64),
                pygame.Rect(548, -852, 64, 64),
                pygame.Rect(612, -852, 64, 64),
                pygame.Rect(676, -852, 64, 64),
                pygame.Rect(740, -852, 64, 64),
                pygame.Rect(804, -852, 64, 64),
                pygame.Rect(868, -852, 64, 64),
                pygame.Rect(932, -852, 64, 64),
                pygame.Rect(996, -852, 64, 64),
                pygame.Rect(1060, -852, 64, 64),
                pygame.Rect(1124, -852, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # plataforma de la izquierda((posX, posY, ancho, alto))
                pygame.Rect(100, 236, 64, 64),
                pygame.Rect(100, 172, 64, 64),
                pygame.Rect(100, 108, 64, 64),
                pygame.Rect(100, 44, 64, 64),
                pygame.Rect(100, -20, 64, 64),
                pygame.Rect(100, -84, 64, 64),
                pygame.Rect(100, -148, 64, 64),
                pygame.Rect(100, -212, 64, 64),
                pygame.Rect(100, -276, 64, 64),
                pygame.Rect(100, -340, 64, 64),
                pygame.Rect(100, -404, 64, 64),
                pygame.Rect(100, -468, 64, 64),
                pygame.Rect(100, -532, 64, 64),
                pygame.Rect(100, -596, 64, 64),
                pygame.Rect(100, -660, 64, 64),
                pygame.Rect(100, -724, 64, 64),
                pygame.Rect(100, -788, 64, 64),
                pygame.Rect(100, -852, 64, 64),
                # plataforma de la derecha((posX, posY, ancho, alto))
                pygame.Rect(1188, 236, 64, 64),
                pygame.Rect(1188, 172, 64, 64),
                pygame.Rect(1188, 108, 64, 64),
                pygame.Rect(1188, 44, 64, 64),
                pygame.Rect(1188, -20, 64, 64),
                pygame.Rect(1188, -84, 64, 64),
                pygame.Rect(1188, -148, 64, 64),
                pygame.Rect(1188, -212, 64, 64),
                pygame.Rect(1188, -276, 64, 64),
                pygame.Rect(1188, -340, 64, 64),
                pygame.Rect(1188, -404, 64, 64),
                pygame.Rect(1188, -468, 64, 64),
                pygame.Rect(1188, -532, 64, 64),
                pygame.Rect(1188, -596, 64, 64),
                pygame.Rect(1188, -660, 64, 64),
                pygame.Rect(1188, -724, 64, 64),
                pygame.Rect(1188, -788, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # fin cuadro principal-----------------------
                # plataformoas especificas del nivel---------
                pygame.Rect(164, -20, 64, 64),
                pygame.Rect(228, -20, 64, 64),
                pygame.Rect(292, -20, 64, 64),
                pygame.Rect(356, -20, 64, 64),
                pygame.Rect(420, -20, 64, 64),
                pygame.Rect(484, -20, 64, 64),
                pygame.Rect(548, -20, 64, 64),
                pygame.Rect(740, -20, 64, 64),
                pygame.Rect(804, -20, 64, 64),
                pygame.Rect(868, -20, 64, 64),
                pygame.Rect(932, 44, 64, 64),
                pygame.Rect(996, 236, 64, 64),
                pygame.Rect(1060, 172, 64, 64),
                pygame.Rect(1124, 108, 64, 64),


                pygame.Rect(164, -212, 64, 64),
                pygame.Rect(228, -148, 64, 64),
                pygame.Rect(292, -84, 64, 64),
                pygame.Rect(356, -276, 64, 64),
                pygame.Rect(420, -340, 64, 64),
                pygame.Rect(484, -340, 64, 64),
                pygame.Rect(548, -340, 64, 64),
                pygame.Rect(612, -340, 64, 64),
                pygame.Rect(804, -340, 64, 64),
                pygame.Rect(868, -340, 64, 64),
                pygame.Rect(932, -340, 64, 64),
                pygame.Rect(996, -340, 64, 64),
                pygame.Rect(1060, -340, 64, 64),
                pygame.Rect(1124, -340, 64, 64),

                pygame.Rect(164, -660, 64, 64),
                pygame.Rect(228, -660, 64, 64),
                pygame.Rect(292, -660, 64, 64),
                pygame.Rect(356, -660, 64, 64),
                pygame.Rect(420, -660, 64, 64),
                pygame.Rect(484, -660, 64, 64),
                pygame.Rect(548, -570, 64, 64),
                pygame.Rect(612, -570, 64, 64),
                pygame.Rect(676, -660, 64, 64),
                pygame.Rect(740, -660, 64, 64),
                pygame.Rect(804, -660, 64, 64),
                pygame.Rect(868, -660, 64, 64),
                pygame.Rect(932, -596, 64, 64),
                pygame.Rect(996, -404, 64, 64),
                pygame.Rect(1060, -468, 64, 64),
                pygame.Rect(1124, -532, 64, 64),
                # --------------------------------------------

            ],
            entities = [
                #monedas pos x, pos y
                utils.makeCoin(500, 150),
                utils.makeCoin(750, -224),
                utils.makeCoin(550, -500),
                utils.makeCoin(700, -403),
                utils.makeCoin(400, -83),
                utils.makeCoin(600, -83),
                utils.makeCoin(550, -720),
                utils.makeCoin(164, -720),
                utils.makeCoin(164, -784),
                utils.makeCoin(228, -720),
                utils.makeCoin(228, -784),
                # enemigos pos x, pos y
                utils.makeEnemy(170, 237),
                utils.makeEnemy(500, 237),
                utils.makeEnemy(814, -83),

                utils.makeEnemy_motor(240, 247),

                globals.player1



            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )
    if levelNumber == 3:
        # cargar nivel 1
        globals.world = Level(
            platforms = [
                # cubo principal-----------------------------------
                # plataforma media(izquierda a derecha)((posX, posY, ancho, alto))
                pygame.Rect(100, 300, 64, 64),
                pygame.Rect(164, 300, 64, 64),
                pygame.Rect(228, 300, 64, 64),
                pygame.Rect(292, 300, 64, 64),
                pygame.Rect(356, 300, 64, 64),
                pygame.Rect(420, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(548, 300, 64, 64),
                pygame.Rect(548, 364, 64, 64),
                pygame.Rect(548, 428, 64, 64),
                pygame.Rect(548, 492, 64, 64),
                pygame.Rect(612, 492, 64, 64),
                pygame.Rect(676, 492, 64, 64),
                pygame.Rect(740, 300, 64, 64),
                pygame.Rect(740, 364, 64, 64),
                pygame.Rect(740, 428, 64, 64),
                pygame.Rect(740, 492, 64, 64),
                pygame.Rect(804, 300, 64, 64),
                pygame.Rect(868, 300, 64, 64),
                pygame.Rect(932, 300, 64, 64),
                pygame.Rect(996, 300, 64, 64),
                pygame.Rect(1060, 300, 64, 64),
                pygame.Rect(1124, 300, 64, 64),
                pygame.Rect(1188, 300, 64, 64),
                # plataforma horizontal arriba
                pygame.Rect(100, -852, 64, 64),
                pygame.Rect(164, -852, 64, 64),
                pygame.Rect(228, -852, 64, 64),
                pygame.Rect(292, -852, 64, 64),
                pygame.Rect(356, -852, 64, 64),
                pygame.Rect(420, -852, 64, 64),
                pygame.Rect(484, -852, 64, 64),
                pygame.Rect(548, -852, 64, 64),
                pygame.Rect(612, -852, 64, 64),
                pygame.Rect(676, -852, 64, 64),
                pygame.Rect(740, -852, 64, 64),
                pygame.Rect(804, -852, 64, 64),
                pygame.Rect(868, -852, 64, 64),
                pygame.Rect(932, -852, 64, 64),
                pygame.Rect(996, -852, 64, 64),
                pygame.Rect(1060, -852, 64, 64),
                pygame.Rect(1124, -852, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # plataforma de la izquierda((posX, posY, ancho, alto))
                pygame.Rect(100, 236, 64, 64),
                pygame.Rect(100, 172, 64, 64),
                pygame.Rect(100, 108, 64, 64),
                pygame.Rect(100, 44, 64, 64),
                pygame.Rect(100, -20, 64, 64),
                pygame.Rect(100, -84, 64, 64),
                pygame.Rect(100, -148, 64, 64),
                pygame.Rect(100, -212, 64, 64),
                pygame.Rect(100, -276, 64, 64),
                pygame.Rect(100, -340, 64, 64),
                pygame.Rect(100, -404, 64, 64),
                pygame.Rect(100, -468, 64, 64),
                pygame.Rect(100, -532, 64, 64),
                pygame.Rect(100, -596, 64, 64),
                pygame.Rect(100, -660, 64, 64),
                pygame.Rect(100, -724, 64, 64),
                pygame.Rect(100, -788, 64, 64),
                pygame.Rect(100, -852, 64, 64),
                # plataforma de la derecha((posX, posY, ancho, alto))
                pygame.Rect(1188, 236, 64, 64),
                pygame.Rect(1188, 172, 64, 64),
                pygame.Rect(1188, 108, 64, 64),
                pygame.Rect(1188, 44, 64, 64),
                pygame.Rect(1188, -20, 64, 64),
                pygame.Rect(1188, -84, 64, 64),
                pygame.Rect(1188, -148, 64, 64),
                pygame.Rect(1188, -212, 64, 64),
                pygame.Rect(1188, -276, 64, 64),
                pygame.Rect(1188, -340, 64, 64),
                pygame.Rect(1188, -404, 64, 64),
                pygame.Rect(1188, -468, 64, 64),
                pygame.Rect(1188, -532, 64, 64),
                pygame.Rect(1188, -596, 64, 64),
                pygame.Rect(1188, -660, 64, 64),
                pygame.Rect(1188, -724, 64, 64),
                pygame.Rect(1188, -788, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # fin cuadro principal-----------------------
                # plataformoas especificas del nivel---------
                pygame.Rect(164, -20, 64, 64),
                pygame.Rect(228, -20, 64, 64),
                pygame.Rect(292, -20, 64, 64),
                pygame.Rect(356, -20, 64, 64),
                pygame.Rect(420, -20, 64, 64),
                pygame.Rect(484, -20, 64, 64),
                pygame.Rect(548, -20, 64, 64),
                pygame.Rect(740, -20, 64, 64),
                pygame.Rect(804, -20, 64, 64),
                pygame.Rect(868, -20, 64, 64),
                pygame.Rect(932, 44, 64, 64),
                pygame.Rect(996, 236, 64, 64),
                pygame.Rect(1060, 172, 64, 64),
                pygame.Rect(1124, 108, 64, 64),

                pygame.Rect(164, -212, 64, 64),
                pygame.Rect(228, -148, 64, 64),
                pygame.Rect(292, -84, 64, 64),
                pygame.Rect(356, -276, 64, 64),
                pygame.Rect(420, -340, 64, 64),
                pygame.Rect(484, -340, 64, 64),
                pygame.Rect(548, -340, 64, 64),
                pygame.Rect(612, -340, 64, 64),
                pygame.Rect(804, -340, 64, 64),
                pygame.Rect(868, -340, 64, 64),
                pygame.Rect(932, -340, 64, 64),
                pygame.Rect(996, -340, 64, 64),
                pygame.Rect(1060, -340, 64, 64),
                pygame.Rect(1124, -340, 64, 64),

                pygame.Rect(164, -660, 64, 64),
                pygame.Rect(228, -660, 64, 64),

                pygame.Rect(356, -660, 64, 64),

                pygame.Rect(484, -660, 64, 64),

                pygame.Rect(612, -660, 64, 64),

                pygame.Rect(740, -660, 64, 64),

                pygame.Rect(868, -660, 64, 64),
                pygame.Rect(932, -596, 64, 64),
                pygame.Rect(996, -404, 64, 64),
                pygame.Rect(1060, -468, 64, 64),
                pygame.Rect(1124, -532, 64, 64),
                # --------------------------------------------
            ],
            entities = [
                #monedas pos x, pos y
                utils.makeCoin(500, 150),
                utils.makeCoin(750, -224),
                utils.makeCoin(550, -500),
                utils.makeCoin(700, -403),
                utils.makeCoin(400, -83),
                utils.makeCoin(600, -83),
                utils.makeCoin(550, -720),
                utils.makeCoin(164, -720),
                utils.makeCoin(164, -784),
                utils.makeCoin(228, -720),
                utils.makeCoin(228, -784),
                # enemigos pos x, pos y
                utils.makeEnemy_3(170, 237),
                utils.makeEnemy_3(500, 237),
                utils.makeEnemy_3(814, -83),
                utils.makeEnemy_3(550, -403),

                utils.makeEnemy_motor(240, 247),

                globals.player1



            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )
    if levelNumber == 4:
        # cargar nivel 2
        globals.world = Level(
            platforms = [
                # cubo principal-----------------------------------
                # plataforma media(izquierda a derecha)((posX, posY, ancho, alto))
                pygame.Rect(100, 300, 64, 64),
                pygame.Rect(164, 300, 64, 64),
                pygame.Rect(228, 300, 64, 64),
                pygame.Rect(292, 300, 64, 64),
                pygame.Rect(356, 300, 64, 64),
                pygame.Rect(420, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(548, 300, 64, 64),
                pygame.Rect(548, 364, 64, 64),
                pygame.Rect(548, 428, 64, 64),
                pygame.Rect(548, 492, 64, 64),
                pygame.Rect(612, 492, 64, 64),
                pygame.Rect(676, 492, 64, 64),
                pygame.Rect(740, 300, 64, 64),
                pygame.Rect(740, 364, 64, 64),
                pygame.Rect(740, 428, 64, 64),
                pygame.Rect(740, 492, 64, 64),
                pygame.Rect(804, 300, 64, 64),
                pygame.Rect(868, 300, 64, 64),
                pygame.Rect(932, 300, 64, 64),
                pygame.Rect(996, 300, 64, 64),
                pygame.Rect(1060, 300, 64, 64),
                pygame.Rect(1124, 300, 64, 64),
                pygame.Rect(1188, 300, 64, 64),
                # plataforma horizontal arriba
                pygame.Rect(100, -852, 64, 64),
                pygame.Rect(164, -852, 64, 64),
                pygame.Rect(228, -852, 64, 64),
                pygame.Rect(292, -852, 64, 64),
                pygame.Rect(356, -852, 64, 64),
                pygame.Rect(420, -852, 64, 64),
                pygame.Rect(484, -852, 64, 64),
                pygame.Rect(548, -852, 64, 64),
                pygame.Rect(612, -852, 64, 64),
                pygame.Rect(676, -852, 64, 64),
                pygame.Rect(740, -852, 64, 64),
                pygame.Rect(804, -852, 64, 64),
                pygame.Rect(868, -852, 64, 64),
                pygame.Rect(932, -852, 64, 64),
                pygame.Rect(996, -852, 64, 64),
                pygame.Rect(1060, -852, 64, 64),
                pygame.Rect(1124, -852, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # plataforma de la izquierda((posX, posY, ancho, alto))
                pygame.Rect(100, 236, 64, 64),
                pygame.Rect(100, 172, 64, 64),
                pygame.Rect(100, 108, 64, 64),
                pygame.Rect(100, 44, 64, 64),
                pygame.Rect(100, -20, 64, 64),
                pygame.Rect(100, -84, 64, 64),
                pygame.Rect(100, -148, 64, 64),
                pygame.Rect(100, -212, 64, 64),
                pygame.Rect(100, -276, 64, 64),
                pygame.Rect(100, -340, 64, 64),
                pygame.Rect(100, -404, 64, 64),
                pygame.Rect(100, -468, 64, 64),
                pygame.Rect(100, -532, 64, 64),
                pygame.Rect(100, -596, 64, 64),
                pygame.Rect(100, -660, 64, 64),
                pygame.Rect(100, -724, 64, 64),
                pygame.Rect(100, -788, 64, 64),
                pygame.Rect(100, -852, 64, 64),
                # plataforma de la derecha((posX, posY, ancho, alto))
                pygame.Rect(1188, 236, 64, 64),
                pygame.Rect(1188, 172, 64, 64),
                pygame.Rect(1188, 108, 64, 64),
                pygame.Rect(1188, 44, 64, 64),
                pygame.Rect(1188, -20, 64, 64),
                pygame.Rect(1188, -84, 64, 64),
                pygame.Rect(1188, -148, 64, 64),
                pygame.Rect(1188, -212, 64, 64),
                pygame.Rect(1188, -276, 64, 64),
                pygame.Rect(1188, -340, 64, 64),
                pygame.Rect(1188, -404, 64, 64),
                pygame.Rect(1188, -468, 64, 64),
                pygame.Rect(1188, -532, 64, 64),
                pygame.Rect(1188, -596, 64, 64),
                pygame.Rect(1188, -660, 64, 64),
                pygame.Rect(1188, -724, 64, 64),
                pygame.Rect(1188, -788, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # fin cuadro principal-----------------------
                # plataformoas especificas del nivel---------
                pygame.Rect(164, -20, 64, 64),
                pygame.Rect(228, -20, 64, 64),
                pygame.Rect(292, -20, 64, 64),
                pygame.Rect(356, -20, 64, 64),


                pygame.Rect(548, -20, 64, 64),
                pygame.Rect(740, -20, 64, 64),
                pygame.Rect(804, -20, 64, 64),
                pygame.Rect(868, -20, 64, 64),
                pygame.Rect(932, 44, 64, 64),
                pygame.Rect(996, 236, 64, 64),
                pygame.Rect(1060, 172, 64, 64),
                pygame.Rect(1124, 108, 64, 64),

                pygame.Rect(164, -212, 64, 64),
                pygame.Rect(228, -148, 64, 64),
                pygame.Rect(292, -84, 64, 64),
                pygame.Rect(356, -276, 64, 64),
                pygame.Rect(420, -340, 64, 64),
                pygame.Rect(484, -340, 64, 64),

                pygame.Rect(612, -340, 64, 64),
                pygame.Rect(804, -340, 64, 64),

                pygame.Rect(932, -340, 64, 64),
                pygame.Rect(996, -340, 64, 64),
                pygame.Rect(1060, -340, 64, 64),
                pygame.Rect(1124, -340, 64, 64),

                pygame.Rect(164, -660, 64, 64),
                pygame.Rect(228, -660, 64, 64),

                pygame.Rect(356, -660, 64, 64),

                pygame.Rect(484, -660, 64, 64),

                pygame.Rect(612, -660, 64, 64),

                pygame.Rect(740, -660, 64, 64),

                pygame.Rect(868, -660, 64, 64),
                pygame.Rect(932, -596, 64, 64),
                pygame.Rect(996, -404, 64, 64),
                pygame.Rect(1060, -468, 64, 64),
                pygame.Rect(1124, -532, 64, 64),
                # --------------------------------------------
            ],
            entities = [
                #monedas pos x, pos y
                utils.makeCoin(500, 150),
                utils.makeCoin(750, -224),
                utils.makeCoin(550, -500),
                utils.makeCoin(700, -403),
                utils.makeCoin(400, -83),
                utils.makeCoin(600, -83),
                utils.makeCoin(550, -720),
                utils.makeCoin(164, -720),
                utils.makeCoin(164, -784),
                utils.makeCoin(228, -720),
                utils.makeCoin(228, -784),
                # enemigos pos x, pos y
                utils.makeEnemy(170, 237),
                utils.makeEnemy_2(500, 237),
                utils.makeEnemy_3(814, -83),
                utils.makeEnemy_3(450, -403),

                utils.makeEnemy_motor(240, 247),

                globals.player1

            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )
    if levelNumber == 5:
        # cargar nivel 1
        globals.world = Level(
            platforms = [
                # cubo principal-----------------------------------
                # plataforma media(izquierda a derecha)((posX, posY, ancho, alto))
                pygame.Rect(100, 300, 64, 64),
                pygame.Rect(164, 300, 64, 64),
                pygame.Rect(228, 300, 64, 64),
                pygame.Rect(292, 300, 64, 64),
                pygame.Rect(356, 300, 64, 64),
                pygame.Rect(420, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(484, 300, 64, 64),
                pygame.Rect(548, 300, 64, 64),
                pygame.Rect(548, 364, 64, 64),
                pygame.Rect(548, 428, 64, 64),
                pygame.Rect(548, 492, 64, 64),
                pygame.Rect(612, 492, 64, 64),
                pygame.Rect(676, 492, 64, 64),
                pygame.Rect(740, 300, 64, 64),
                pygame.Rect(740, 364, 64, 64),
                pygame.Rect(740, 428, 64, 64),
                pygame.Rect(740, 492, 64, 64),
                pygame.Rect(804, 300, 64, 64),
                pygame.Rect(868, 300, 64, 64),
                pygame.Rect(932, 300, 64, 64),
                pygame.Rect(996, 300, 64, 64),
                pygame.Rect(1060, 300, 64, 64),
                pygame.Rect(1124, 300, 64, 64),
                pygame.Rect(1188, 300, 64, 64),
                # plataforma horizontal arriba
                pygame.Rect(100, -852, 64, 64),
                pygame.Rect(164, -852, 64, 64),
                pygame.Rect(228, -852, 64, 64),
                pygame.Rect(292, -852, 64, 64),
                pygame.Rect(356, -852, 64, 64),
                pygame.Rect(420, -852, 64, 64),
                pygame.Rect(484, -852, 64, 64),
                pygame.Rect(548, -852, 64, 64),
                pygame.Rect(612, -852, 64, 64),
                pygame.Rect(676, -852, 64, 64),
                pygame.Rect(740, -852, 64, 64),
                pygame.Rect(804, -852, 64, 64),
                pygame.Rect(868, -852, 64, 64),
                pygame.Rect(932, -852, 64, 64),
                pygame.Rect(996, -852, 64, 64),
                pygame.Rect(1060, -852, 64, 64),
                pygame.Rect(1124, -852, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # plataforma de la izquierda((posX, posY, ancho, alto))
                pygame.Rect(100, 236, 64, 64),
                pygame.Rect(100, 172, 64, 64),
                pygame.Rect(100, 108, 64, 64),
                pygame.Rect(100, 44, 64, 64),
                pygame.Rect(100, -20, 64, 64),
                pygame.Rect(100, -84, 64, 64),
                pygame.Rect(100, -148, 64, 64),
                pygame.Rect(100, -212, 64, 64),
                pygame.Rect(100, -276, 64, 64),
                pygame.Rect(100, -340, 64, 64),
                pygame.Rect(100, -404, 64, 64),
                pygame.Rect(100, -468, 64, 64),
                pygame.Rect(100, -532, 64, 64),
                pygame.Rect(100, -596, 64, 64),
                pygame.Rect(100, -660, 64, 64),
                pygame.Rect(100, -724, 64, 64),
                pygame.Rect(100, -788, 64, 64),
                pygame.Rect(100, -852, 64, 64),
                # plataforma de la derecha((posX, posY, ancho, alto))
                pygame.Rect(1188, 236, 64, 64),
                pygame.Rect(1188, 172, 64, 64),
                pygame.Rect(1188, 108, 64, 64),
                pygame.Rect(1188, 44, 64, 64),
                pygame.Rect(1188, -20, 64, 64),
                pygame.Rect(1188, -84, 64, 64),
                pygame.Rect(1188, -148, 64, 64),
                pygame.Rect(1188, -212, 64, 64),
                pygame.Rect(1188, -276, 64, 64),
                pygame.Rect(1188, -340, 64, 64),
                pygame.Rect(1188, -404, 64, 64),
                pygame.Rect(1188, -468, 64, 64),
                pygame.Rect(1188, -532, 64, 64),
                pygame.Rect(1188, -596, 64, 64),
                pygame.Rect(1188, -660, 64, 64),
                pygame.Rect(1188, -724, 64, 64),
                pygame.Rect(1188, -788, 64, 64),
                pygame.Rect(1188, -852, 64, 64),
                # fin cuadro principal-----------------------
                # plataformoas especificas del nivel---------
                pygame.Rect(164, -20, 64, 64),
                pygame.Rect(228, -20, 64, 64),
                pygame.Rect(292, -20, 64, 64),
                pygame.Rect(356, -20, 64, 64),

                pygame.Rect(548, -20, 64, 64),
                pygame.Rect(740, -20, 64, 64),
                pygame.Rect(804, -20, 64, 64),
                pygame.Rect(868, -20, 64, 64),
                pygame.Rect(932, 44, 64, 64),
                pygame.Rect(996, 236, 64, 64),
                pygame.Rect(1060, 172, 64, 64),
                pygame.Rect(1124, 108, 64, 64),
                pygame.Rect(1124, 65, 64, 64),

                pygame.Rect(164, -212, 64, 64),
                pygame.Rect(164, -250, 64, 64),
                pygame.Rect(228, -148, 64, 64),
                pygame.Rect(292, -84, 64, 64),
                pygame.Rect(356, -276, 64, 64),
                pygame.Rect(420, -340, 64, 64),
                pygame.Rect(484, -340, 64, 64),

                pygame.Rect(612, -340, 64, 64),
                pygame.Rect(804, -340, 64, 64),

                pygame.Rect(932, -340, 64, 64),
                pygame.Rect(996, -340, 64, 64),
                pygame.Rect(1060, -340, 64, 64),
                pygame.Rect(1124, -340, 64, 64),

                pygame.Rect(164, -660, 64, 64),
                pygame.Rect(228, -660, 64, 64),

                pygame.Rect(356, -660, 64, 64),

                pygame.Rect(484, -660, 64, 64),

                pygame.Rect(612, -660, 64, 64),

                pygame.Rect(740, -660, 64, 64),

                pygame.Rect(868, -660, 64, 64),
                pygame.Rect(932, -596, 64, 64),
                pygame.Rect(996, -404, 64, 64),
                pygame.Rect(1060, -468, 64, 64),
                pygame.Rect(1124, -532, 64, 64),
                # --------------------------------------------
            ],
            entities = [
                #monedas pos x, pos y
                utils.makeCoin(500, 150),
                utils.makeCoin(750, -224),
                utils.makeCoin(550, -500),
                utils.makeCoin(700, -403),
                utils.makeCoin(400, -83),
                utils.makeCoin(600, -83),
                utils.makeCoin(550, -720),
                utils.makeCoin(164, -720),
                utils.makeCoin(164, -784),
                utils.makeCoin(228, -720),
                utils.makeCoin(228, -784),
                # enemigos pos x, pos y
                utils.makeEnemy_3(170, 237),
                utils.makeEnemy_2(500, 237),
                utils.makeEnemy(814, -83),
                utils.makeEnemy_2(450, -403),

                utils.makeEnemy_motor(240, 247),

                globals.player1



            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )

    #resetear jugador
    #para entidades en la lista de entidades:
    for entity in globals.world.entities:
        #resetear entidad si no se esta en un nivel
        entity.reset(entity)