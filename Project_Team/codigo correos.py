dominio = input("ingrese un dominio de correo: ")
cuentas = []
numeros = ["1","2","3","4","5"]
DictUsuario = {}


sufijos = []
for h in numeros:
    for j in numeros:
        for i in numeros:
            for z in numeros:
             texto = h+j+i+z
             sufijos.append(texto)

digitos = ["1","2","3","a","b"]
claves = []
for a in digitos:
    for b in digitos:
        for c in digitos:
            for d in digitos:
                for e in digitos:
                 suma = a+b+c+d+e
                 claves.append(suma)


for i in range(3):
    cantidad="usuario"+str(i)

    nombre = input("ingrese su primer nombre: ")
    apellido = input("ingrese sus apellido: ")
    print("datos ingresados: ", "dominio: ", dominio, "nombre: ", nombre, "apellido: ", apellido)

    usuario = nombre[0:2] + apellido[0:3]+sufijos[0]
    random = claves[(len(nombre)+len(apellido))]

    if usuario not in cuentas:
        cuentas.append(usuario)
    else:
        for m in sufijos:
            usuario = nombre[0:2] + apellido[0:3] + m
            if usuario in cuentas:
                continue
            else:
                cuentas.append(usuario)
                break
    print(usuario, random)
    DictUsuario[cantidad] = [usuario, random, nombre, apellido]


print(cuentas)
print(DictUsuario)
print(claves)