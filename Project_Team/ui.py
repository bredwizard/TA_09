# importar librarias
import utils
import globals

# clase boton de menu
class ButtonUI:
    # empezar a definir
    def __init__(self, keyCode, text, x, y):
        # codigo de tecla
        self.keyCode = keyCode
        # texto del boton
        self.text = text
        # pos x
        self.x = x
        # pos en y
        self.y = y
        # boton presionado es falso
        self.pressed = False
        # boton encendido es falso
        self.on = False
        # cronometro
        self.timer = 20
    # actualizacion
    def update(self, inputStream):
        # si esta presionado el input es de la tecla que se este presionando ene l momemto
        self.pressed = inputStream.keyboard.isKeyPressed(self.keyCode)
        # si esta presionada
        if self.pressed:
            # si esta encendido
            self.on = True
        # si esta encendido
        if self.on:
            # el reloj disminuye 1
            self.timer -= 1
            # si el relog es menor o igual 0
            if self.timer <= 0:
                # el boton no esta encendido
                self.on = False
                # y devolver el timer a 20
                self.timer = 20
    # dibujar en la pantalla
    def draw(self, screen, alpha=255):
        # si esta encendido el boton
        if self.on:
            # su color es verde
            colour = globals.VERDE
        else:
            # y si no su color es blanco
            colour = globals.BLANCO
        # dibujar boton
        utils.drawText(screen, self.text, self.x, self.y, colour, alpha)