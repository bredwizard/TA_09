#importar sqlite3 que sirve para bases de datos
import sqlite3

# crear y conectar sqlite con la base de datos
conn=sqlite3.connect('Project_Team/login.db')
# conectar con el curso
c=conn.cursor()

# definir crear tabla
def create_table():
	#ejecutar y crea una tabla (sino existe) con las variables nombre, apellido, usuario, y contraseña (password) en formato .db
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Pass TEXT)")
	# guardar cambios en la base de datos
	conn.commit()
	# cerrar
	c.close()
	# guardar al cerrar
	conn.close()

#crear trabla
create_table()