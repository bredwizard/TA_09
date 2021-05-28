# importar pygame
import pygame

# clase teclado
class Keyboard:
    # iniciar a definir
    def __init__(self):
        # tecla actual presionada
        self.currentKeyStates = None
        # tecla anterior
        self.previousKeyStates = None
    # ingresar input
    def processInput(self):
        # estadoanterior del tecla = estado actual de tecla
        self.previousKeyStates = self.currentKeyStates
        # estado acutal de tecla = presionar teclas desde pygame
        self.currentKeyStates = pygame.key.get_pressed()
    # tecla abajo
    def isKeyDown(self, keyCode):
        # si es estado de tecla actual es ninguno o si la tecla anterior fue ninguno
        if self.currentKeyStates is None or self.previousKeyStates is None:
            # devolver falso
            return False
        # si no devolver verdades
        return self.currentKeyStates[keyCode] == True
    #si la recla esta presionada
    def isKeyPressed(self, keyCode):
        # si es estado de tecla actual es ninguno o si la tecla anterior fue ninguno
        if self.currentKeyStates is None or self.previousKeyStates is None:
            # devolver falso
            return False
        # si no el estado de la tecla es verdadero  y la del estado de la tecla anterior es falso
        return self.currentKeyStates[keyCode] == True and self.previousKeyStates[keyCode] == False
    # si la tecla es liberada
    def isKeyReleased(self, keyCode):
        # si la tecla actual es ninguna o si la tecla anterior es ninguna
        if self.currentKeyStates is None or self.previousKeyStates is None:
            # devolver falso
            return False
        # si no el estado de la tecla es verdadero  y la del estado de la tecla anterior es falso
        return self.currentKeyStates[keyCode] == False and self.previousKeyStates[keyCode] == True

# clase inputStream
class InputStream:
    # definir
    def __init__(self):
        # definir keyboard
        self.keyboard = Keyboard()
    # proceso de input
    def processInput(self):
        # proceso de input en el teclado
        self.keyboard.processInput()