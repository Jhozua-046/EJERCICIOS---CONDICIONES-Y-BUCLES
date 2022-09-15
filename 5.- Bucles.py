inversion = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese su porcentaje de interes: "))
años = int(input("Cuantos años invertira: "))
print ("----------------------")

for i in range(años):
    inversion *= 1 + interes / 100
    print ("La capital en " + str(i + 1) + " años es: " + str(round(inversion, 2)))

