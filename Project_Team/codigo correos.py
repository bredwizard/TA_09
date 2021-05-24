usuarios = []
for i in range(1):
  datos = []
  nombre = input("ingrese un nickname: ")
  datos.append(nombre)
  correo = input("ingrese un email: ")
  datos.append(correo)
  contraseña = input("ingrese una contraseña: ")
  datos.append(contraseña)
  usuarios.append(datos)
print(usuarios)

h = open("correos.txt","r")
for x in h:
  z = x[:-1]
  usuarios.append(z.split(", "))
print(usuarios)

if nombre in "correos.txt":
  print("usuario ya registrado")
else:
  print("usuario registrado")

h.close()
f = open("correos.txt","w")
for usuario in usuarios:
  print(usuario)
  print(", ".join(usuario))
  f.write(", ".join(usuario) + "\n")
f.close()



