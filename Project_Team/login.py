# INPORTAR LIBRERIAS
from tkinter import *
# tkinter es una libraria especializada en interfaces graficas
import tkinter as tk
# sirve para editar imagnes desde imageTkinter
from PIL import ImageTk, Image
# sirve para abrir ventanas de mensajes
from tkinter import messagebox as mb
# importar sqlite3 que sirve para crear y conectar bases de datos
import sqlite3

# crear ventana en tkinter
ventana = tk.Tk()
# titulo de la ventana
ventana.title("Registro y login Project Team")
# tamaño de la ventana principal (tamaño en x, tamaño en y, posicion en la pantalla en x, posicion en la pantalla en y)
ventana.geometry("440x600+300+250")

# Codigo HEX del color de fondo usado (#575757 es un gris oscuro)
color = '#575757'
# Definir la ventana ventana bg con el valor del color
ventana['bg'] = color

# mostrar texto superior "login" (label sirve para colocar imagen o texto)
Label(ventana, bg=color, text="Login", font=("Arial Black", 16)).pack()

# Abrir imagen para ventana principal llamada "logo"
imagen = Image.open("Project_Team/assets/logeo/logo_pt.png")
# Redimensionnar la imagen a 180*180
imagen = imagen.resize((180, 180), Image.ANTIALIAS)
# cambiar nombre a la  imagen redimensionada (photoImg)
photoImg = ImageTk.PhotoImage(imagen)
# Mostrar la imagen en la ventana(label sirve para colocar imagen o texto)
panel = tk.Label(ventana, image=photoImg).pack()
# Abrir imagen para ventana de registro
img_reg = Image.open("Project_Team/assets/logeo/logo2.png")
# Redimensionar imagen a 100*220
img_reg = img_reg.resize((100, 220), Image.ANTIALIAS)
# poner nombre la imagen redimensionada (photo_reg)
photo_reg = ImageTk.PhotoImage(img_reg)
# Cajas la ventana Principal
# Texto Usuario: con fuent arial black tamaño 10
Label(ventana, text="Usuario : ", bg=color, font=("Arial Black", 10)).pack()
# Crear una caja de texto caja1 (ventana, fuente arial tamaño 10
caja1 = Entry(ventana, font=("Arial", 10))
# Posicion de la caja1
caja1.pack()
# Texto "Contraseña:" con fuent arial black tamaño 10
Label(ventana, text="Contraseña : ", bg=color, font=("Arial Black", 10)).pack()
# Crear la caja2 (contraseña)
caja2 = Entry(ventana, show="*")
# Posicion de caja2
caja2.pack()

# conectar a la  base de datos "login.db" por medio de sqlite
db = sqlite3.connect('login.db')
# Establecer un cursor dentro de la base de datos
c = db.cursor()

# Funcion login para  comprobar el usuario y contraseña en la base de datos
def login():
	# Obtener el valor de la caja1 (usuario)
	usuario = caja1.get()
	# Obtener el valor de la caja2 (contraseña)
	contr = caja2.get()
	# Seleccionar datos (usuario,contr)
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?', (usuario, contr))

    # si todos los datos (fetchall)
	if c.fetchall():
		# Mostrar mensaje
		mb.showinfo(title="Login Correcto", message="BIENVENIDO A PROJECT TEAM :D para acceder al nivel secreto presiona 'QWERTY' todas a la vez en el selector de niveles")
	# de lo contrario
	else:
		# Mostrar "Login incorrecto"
		mb.showerror(title="Login incorrecto", message="Usuario o contraseña incorrecto")
	# c.close()

# Funcion nuevaVentana para el registro de nuevos usuarios
def nuevaVentana():
	# Definir "newVentana"
	newVentana = tk.Toplevel(ventana)
	# titulo Registro de Usuario
	newVentana.title("Registro de Usuario")
	# Tamaño de la ventana ancho, alto, pos en pantalla en x, pos en pantalla en y
	newVentana.geometry("300x290+800+250")
	# Definir newVentana bg con el valor de color
	newVentana['bg'] = color

	# Texto "Registro"
	labelExample = tk.Label(newVentana, text="Registro : ", bg=color, font=("Arial Black", 12)).pack(side="top")
	# Mostrar la imagen en la posicion "left"
	panel_reg = tk.Label(newVentana, image=photo_reg).pack(side="left")

	# Texto Nombre:
	Label(newVentana, text="Nombre : ", bg=color, font=("Arial Black", 10)).pack()
	# Creamos caja3 (ingresar Nombre)
	caja3 = Entry(newVentana)
	caja3.pack()
	# Texto Apellidos
	Label(newVentana, text="Apellidos : ", bg=color, font=("Arial Black", 10)).pack()
	# Creamos caja4 (ingresar Apellidos)
	caja4 = Entry(newVentana)
	caja4.pack()
	# Texto Usuario
	Label(newVentana, text="Usuario : ", bg=color, font=("Arial Black", 10)).pack()
	# Creamos caja5 (ingresar Usuario)
	caja5 = Entry(newVentana)
	caja5.pack()
	# Texto Contraseña
	Label(newVentana, text="Contraseña : ", bg=color, font=("Arial Black", 10)).pack()
	# Creamos caja6 (ingresar Contraseña y que los caracteres se vean como *)
	caja6 = Entry(newVentana, show="*")
	caja6.pack()
	# Texto Repita la Contraseña
	Label(newVentana, text="Repita la Contraseña : ", bg=color, font=("Arial Black", 10)).pack()
	# Creamos caja7 (volver a ingresar la Contraseña y que los caracteres se vean como *)
	caja7 = Entry(newVentana, show="*")
	caja7.pack()

	# Funcion registro para escribir los datos a nuestra base de datos
	def registro():
		# Obtener el valor de caja3
		Nombre = caja3.get()
		# Obtener el valor de caja4
		Apellido = caja4.get()
		# Obtener el valor de caja5
		Usr_reg = caja5.get()
		# Obtener el valor de caja6
		Contra_reg = caja6.get()
		# Obtener el valor de caja7
		Contra_reg_2 = caja7.get()
		# " si la contraseña es igual a la confirmacion de la contraseña"
		if Contra_reg==Contra_reg_2:
			# insertar los datos obtenidos en el registro
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			# Confirmamos los datos
			db.commit()
			# mostrar informacion en ventana "registro correcto, hola nombre apellido, el registro sue exitoso"
			mb.showinfo(title="Registro Correcto", message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			# cerrar ventana de registro
			newVentana.destroy()
		# de lo contrario se ejecutara si las contraseñas no coinciden
		else:
			#  mostrar error en ventana "contrasela incorrecta, las contraseñas no soinciden"
			mb.showerror(title="Contraseña Incorrecta", message="Error¡¡¡ \nLas contraseñas no coinciden.")
		# c.close()		#Nos permite cerrar el cursor ...
		# db.close()
	# llamar a la funcion registro con el boton registrar
	buttons = tk.Button(newVentana, text="Registrar ¡", command=registro, bg=color, font=("Arial Rounded MT Bold", 10)).pack(side="bottom")

# linea vacia de separacion
Label(ventana, text=" ", bg=color, font=("Arial", 10)).pack()
# boton para la funcion de login
Button(text=" ENTRAR ", command=login, bg='#a6d4f2', font=("Arial Rounded MT Bold", 10)).pack()
# texto en ventana con fuente arial black tamaño 10
Label(ventana, text=" ", bg=color, font=("Arial Black", 10)).pack()
# texto en ventana con fuente arial black tamaño 10
Label(ventana, text="No tienes una cuenta ?", bg=color, font=("Arial Black", 10)).pack()
# boton para ir a la ventana de registro
boton1 = Button(ventana, text="REGISTRO", bg='#a6d4f2', command=nuevaVentana, font=("Arial Rounded MT Bold", 10)).pack()

ventana.mainloop()