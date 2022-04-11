print ("------------ejercicio numero 1:-------------")

edad = int(input("¿que edad tienes?: "))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("no eres mayor de edad")


print ("------------ejercicio numero 2:-------------")

nombre_clave = input("introduce tu contraseña: ")
if nombre_clave == "contraseña":
    print("tu contraseña es correcta")
else:
    print("tu contraseña es incorrecta")


print ("------------ejercicio numero 3:-------------")

x = int(input("introduce el dividendo: "))
y = int(input("introduce el divisor: "))
if y == 0:
    print("error")
else:
    print(x/y)