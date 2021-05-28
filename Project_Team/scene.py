#im portar librarias
import pygame
import ui
import engine
import utils
import globals
import nivel

# clase escena
class Scene:
    # empezar a definir
    def __init__(self):
        pass
    # definir entrar
    def onEnter(self):
        pass
    # definir salir
    def onExit(self):
        pass
    # definir input
    def input(self, sm, inputStream):
        pass
    # definir actualizacion
    def update(self, sm, inputStream):
        pass
    # definir dibujar
    def draw(self, sm, screen):
        pass

# menu princial
class MainMenuScene(Scene):
    # comenzar a definir
    def __init__(self):
        # entrar seleccion de niveles con boton enter en posicion x y y
        self.enter = ui.ButtonUI(pygame.K_RETURN, "[ENTER = next]", 50, 200)
        # salir con boton escape en posicion x y y
        self.esc = ui.ButtonUI(pygame.K_ESCAPE, "[ESC = quit]", 50, 250)
        # entrar creditos con boton c en posicion x y y
        self.c = ui.ButtonUI(pygame.K_c, "[C = creditos]", 50, 300)
    # definir input
    def input(self, sm, inputStream):
        # si se prsioan enter
        if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
            # cambiar a level select
            sm.push(FadeTransitionScene([self], [LevelSelectScene()]))
        # si se presiona escape
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            # cerrar
            sm.pop()
        # si ce presiona c
        if inputStream.keyboard.isKeyPressed(pygame.K_c):
            # entrar a los creditos
            sm.push(FadeTransitionScene([self], [Credits()]))
    # definir actualizacion
    def update(self, sm, inputStream):
        #para enter
        self.enter.update(inputStream)
        # para escape
        self.esc.update(inputStream)
        # para c
        self.c.update(inputStream)
    # dibujar en pantalla
    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        utils.drawText(screen, "MENU PRINICIPAL", 50, 50,globals.BLANCO, 255)
        # dibujar  al entrar enter
        self.enter.draw(screen)
        # dibujar dibujar al salir con escape
        self.esc.draw(screen)
        # dibujar creditos
        self.c.draw(screen)

# LO MISMO SE APLICARIA CON LEVEL SELECT Y CREDITOS

class Credits(Scene):
    def __init__(self):
        self.cr1 = ui.ButtonUI(pygame.K_RETURN, "sprite de coin por DasBilligeAlien", 50, 100)
        self.cr1_1 = ui.ButtonUI(pygame.K_RETURN, "https://opengameart.org/content/rotating-coin-0", 50, 130)
        self.cr2 = ui.ButtonUI(pygame.K_ESCAPE, "sprite de corazon por BenBushnell", 50, 200)
        self.cr2_1 = ui.ButtonUI(pygame.K_RETURN, "https://pixabay.com/es/illustrations/pixel-corazón-corazón-píxeles-2779422", 50, 230)
        self.cr3 = ui.ButtonUI(pygame.K_c, "degradado de escena y letras por nerdparadise", 50, 300)
        self.cr3_1 = ui.ButtonUI(pygame.K_RETURN, "https://nerdparadise.com/programming/pygameblitopacity", 50, 330)
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
    def update(self, sm, inputStream):
        self.cr1.update(inputStream)
        self.cr2.update(inputStream)
        self.cr3.update(inputStream)
        self.cr1_1.update(inputStream)
        self.cr2_1.update(inputStream)
        self.cr3_1.update(inputStream)

    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        utils.drawText(screen, "CREDITOS", 50, 50,globals.BLANCO, 255)
        self.cr1.draw(screen)
        self.cr2.draw(screen)
        self.cr3.draw(screen)
        self.cr1_1.draw(screen)
        self.cr2_1.draw(screen)
        self.cr3_1.draw(screen)


class LevelSelectScene(Scene):
    def __init__(self):
        self.b1 = ui.ButtonUI(pygame.K_1, "[Nivel 1]", 50, 200)
        self.b2 = ui.ButtonUI(pygame.K_2, "[Nivel 2]", 50, 250)
        self.b3 = ui.ButtonUI(pygame.K_3, "[Nivel 3]", 50, 300)
        self.b4 = ui.ButtonUI(pygame.K_4, "[Nivel 4]", 50, 350)
        self.b5 = ui.ButtonUI(pygame.K_SPACE, "[nivel secreto] registrate para saber como desbloquear por solo $19.99 ", 50, 400)
        self.esc = ui.ButtonUI(pygame.K_ESCAPE, "[ESC = quit]", 50, 450)

    def update(self, sm, inputStream):
        self.b1.update(inputStream)
        self.b2.update(inputStream)
        self.b3.update(inputStream)
        self.b4.update(inputStream)
        self.b5.update(inputStream)
        self.esc.update(inputStream)

    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_1):
            #escoger nivel 1
            nivel.loadLevel(1)
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if inputStream.keyboard.isKeyPressed(pygame.K_2):
            #escoger nivel 2
            nivel.loadLevel(2)
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if inputStream.keyboard.isKeyPressed(pygame.K_3):
            # escoger nivel 3
            nivel.loadLevel(3)
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if inputStream.keyboard.isKeyPressed(pygame.K_4):
            # escoger nivel 4
            nivel.loadLevel(4)
            sm.push(FadeTransitionScene([self], [GameScene()]))
        # CODIGO PARA DEBLOQUAR NIVEL SCRETO ES QWERTY
        if inputStream.keyboard.isKeyDown(pygame.K_q) and inputStream.keyboard.isKeyDown(pygame.K_w) and inputStream.keyboard.isKeyDown(pygame.K_e) and inputStream.keyboard.isKeyDown(pygame.K_r) and inputStream.keyboard.isKeyDown(pygame.K_t) and inputStream.keyboard.isKeyDown(pygame.K_y):
            # escoger nivel 5
            nivel.loadLevel(5)
            sm.push(FadeTransitionScene([self], [GameScene()]))
        # SALIR del level select
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene([self], []))
    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        utils.drawText(screen, "level select", 50, 50,globals.BLANCO, 255)
        self.b1.draw(screen)
        self.b2.draw(screen)
        self.b3.draw(screen)
        self.b4.draw(screen)
        self.b5.draw(screen)
        self.esc.draw(screen)



class GameScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
        self.collectionSystem = engine.CollectionSystem()
        self.battleSystem = engine.BattleSystem()
        self.inputSystem = engine.InputSystem()
        self.physicsSystem = engine.PhysicsSystem()
        self.animationSystem = engine.AnimationSystem()
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.pop()
            sm.push(FadeTransitionScene([self], []))
        if globals.world.isWon():
            sm.push(WinScene())
        if globals.world.isLost():
            sm.push(LoseScene())
    def update(self, sm, inputStream):
        self.inputSystem.update(inputStream=inputStream)
        self.collectionSystem.update()
        self.battleSystem.update()
        self.physicsSystem.update()
        self.animationSystem.update()
    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        self.cameraSystem.update(screen)


class WinScene(Scene):
    def __init__(self):
        self.alpha = 0
        self.esc = ui.ButtonUI(pygame.K_ESCAPE, "[ESC = quit]", 250, 10)
    def update(self, sm, inputStream):
        self.alpha = min(255, self.alpha + 10)
        self.esc.update(inputStream)
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.set([FadeTransitionScene([GameScene(),self], [MainMenuScene(), LevelSelectScene()])])
    def draw(self, sm, screen):
        if len(sm.scenes) > 1:
            sm.scenes[-2].draw(sm, screen)

        # DIBUJAR un Background translucido
        bgSurf = pygame.Surface((1000, 560))
        bgSurf.fill((globals.NEGRO))
        utils.blit_alpha(screen, bgSurf, (0,0), self.alpha * 0.7)

        utils.drawText(screen, "GANASTE", 250, 250,globals.BLANCO, self.alpha)
        self.esc.draw(screen , alpha = self.alpha)

class LoseScene(Scene):
    def __init__(self):
        self.alpha = 0
        self.esc = ui.ButtonUI(pygame.K_ESCAPE, "[ESC = quit]", 250, 10)
    def update(self, sm, inputStream):
        self.alpha = min(255, self.alpha + 10)
        self.esc.update(inputStream)
    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
            sm.set([FadeTransitionScene([GameScene(), self], [MainMenuScene(), LevelSelectScene()])])
    def draw(self, sm, screen):
        if len(sm.scenes) > 1:
            sm.scenes[-2].draw(sm, screen)

        # DIBUJAR UN Bacground opaco
        bgSurf = pygame.Surface((1000, 560))
        bgSurf.fill((globals.NEGRO))
        utils.blit_alpha(screen, bgSurf, (0,0), self.alpha * 0.7)

        utils.drawText(screen, "PERDISTE", 250, 250, globals.BLANCO, self.alpha)
        self.esc.draw(screen, alpha = self.alpha)

class TransitionScene(Scene):
    def __init__(self, fromScenes, toScenes):
        self.currentPercentage = 0
        self.fromScenes = fromScenes
        self.toScenes = toScenes
    def update(self, sm, inputStream):
        self.currentPercentage += 5
        if self.currentPercentage >= 100:
            sm.pop()
            for s in self.toScenes:
                sm.push(s)
        for scene in self.fromScenes:
            scene.update(sm, inputStream)
        if len(self.toScenes) > 0:
            for scene in self.toScenes:
                scene.update(sm, inputStream)
        else:
            if len(sm.scenes) > 1:
                sm.scenes[-2].update(sm, inputStream)

class FadeTransitionScene(TransitionScene):
    def draw(self, sm, screen):
        if self.currentPercentage < 50:
            for s in self.fromScenes:
                s.draw(sm, screen)
        else:
            if len(self.toScenes) == 0:
                if len(sm.scenes) > 1:
                    sm.scenes[-2].draw(sm, screen)
            else:
                for s in self.toScenes:
                    s.draw(sm, screen)

        # overlay del degradado
        overlay = pygame.Surface((1000, 560))
        # que tan negro es el maximo del degradado de la transicion (transparente =0 , negro puro >= 255)
        # 0% =0, 50% = 255, 100% = 0
        alpha = int(abs((255 - (255/50)*self.currentPercentage)))
        # poner el valor de negro en el overlay
        overlay.set_alpha(255- alpha)
        # el color del degradado sera la variable NEGRO
        overlay.fill(globals.NEGRO)
        #dibujar overlay desde las cordenadas (0,0)
        screen.blit(overlay, (0,0))

class SceneManager:
    def __init__(self):
        self.scenes = []
    def isEmpty(self):
        return len(self.scenes) == 0
    def enterScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()
    def exitScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
    def input(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self, inputStream)
    def update(self, inputStream):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self, inputStream)
    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        # pantalla actual
        pygame.display.flip()
    def push(self, scene):
        self.exitScene()
        self.enterScene()
        self.scenes.append(scene)
    def pop(self):
        self.exitScene()
        self.enterScene()
        self.scenes.pop()
    def set(self, scenes):
        # pop a todas las escenas
        while len(self.scenes) > 0:
            self.pop()
        # agregar una escena
        for s in scenes:
            self.push(s)