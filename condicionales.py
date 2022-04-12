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


print ("------------ejercicio numero 6:-------------")

edad = int(input("¿cual es tu edad?: "))
ingresos_mensuales = int(input("¿cuales son tus ingresos mensuales?: "))
if edad > 16 and ingresos_mensuales >= 1000:
    print("debes de cotizar")
else:
    print("no debes cotizar")