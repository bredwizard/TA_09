import pygame

import engine
import utils
import globals

class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm):
        pass
    def update(self, sm):
        pass
    def draw(self, sm, screen):
        pass

class MainMenuScene(Scene):
    def input(self, sm):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RETURN]:
            sm.push(FadeTransitionScene([self], [LevelSelectScene()]))
        if teclas[pygame.K_z]:
            sm.pop()
    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        utils.drawText(screen, "Main Menu.   Enter = Levels, Z = quit", 50, 50,globals.BLANCO, 255)

class LevelSelectScene(Scene):
    def input(self, sm):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_1]:
            #escoger nivel 1
            globals.world = globals.levels[1]
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if teclas[pygame.K_2]:
            #escoger nivel 2
            globals.world = globals.levels[2]
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if teclas[pygame.K_3]:
            # escoger nivel 3
            globals.world = globals.levels[3]
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if teclas[pygame.K_4]:
            # escoger nivel 4
            globals.world = globals.levels[4]
            sm.push(FadeTransitionScene([self], [GameScene()]))
        if teclas[pygame.K_ESCAPE]:
            sm.pop()
            sm.push(FadeTransitionScene([self], []))
    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        utils.drawText(screen, "level select. 1,2,3,4 = elige un nivel, esc=quit", 50, 50,globals.BLANCO, 255)

class GameScene(Scene):
    def __init__(self):
        self.cameraSystem = engine.CameraSystem()
    def input(self, sm):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene([self], []))
        if globals.world.isWon():
            sm.push(WinScene())
        if globals.world.isLost():
            sm.push(LoseScene())
    def draw(self, sm, screen):
        # background y color
        screen.fill(globals.GRIS)
        self.cameraSystem.update(screen)


class WinScene(Scene):
    def __init__(self):
        self.alpha = 0
    def update(self, sm):
        self.alpha = min(255, self.alpha + 1)
    def input(self, sm):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            sm.set([FadeTransitionScene([GameScene(),self], [MainMenuScene(), LevelSelectScene()])])
    def draw(self, sm, screen):
        if len(sm.scenes) > 1:
            sm.scenes[-2].draw(sm, screen)

        # DIBUJAR UN BacgroundG
        bgSurf = pygame.Surface((1000, 560))
        bgSurf.fill((globals.NEGRO))
        utils.blit_alpha(screen, bgSurf, (0,0), self.alpha * 0.7)

        utils.drawText(screen, "GANASTE, dale a la x", 250, 250,globals.BLANCO, self.alpha)

class LoseScene(Scene):
    def __init__(self):
        self.alpha = 0
    def update(self, sm):
        self.alpha = min(255, self.alpha + 1)
    def input(self, sm):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            sm.set([FadeTransitionScene([GameScene(), self], [MainMenuScene(), LevelSelectScene()])])
    def draw(self, sm, screen):
        if len(sm.scenes) > 1:
            sm.scenes[-2].draw(sm, screen)

        # DIBUJAR UN Bacground opaco
        bgSurf = pygame.Surface((1000, 560))
        bgSurf.fill((globals.NEGRO))
        utils.blit_alpha(screen, bgSurf, (0,0), self.alpha * 0.7)

        utils.drawText(screen, "PERDISTE, dale a la x", 250, 250,globals.BLANCO, self.alpha)

class TransitionScene(Scene):
    def __init__(self, fromScenes, toScenes):
        self.currentPercentage = 0
        self.fromScenes = fromScenes
        self.toScenes = toScenes
    def update(self, sm):
        self.currentPercentage += 5
        if self.currentPercentage >= 100:
            sm.pop()
            for s in self.toScenes:
                sm.push(s)


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
    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)
    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)
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