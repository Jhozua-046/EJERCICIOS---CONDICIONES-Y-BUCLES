puntuacion = float(input("Ingrese su puntuacion: "))
print ("--------------------------------")

if puntuacion == 0.0:
    print ("Su rendimiento es INACEPTABLE")
    salario = puntuacion*2400
    print ("Su salario sera: " + str(salario))

if puntuacion == 0.4:
    print ("Su rendimiento es ACEPTABLE")
    salario = puntuacion*2400
    print ("Su salario sera: " + str(salario))

if  0.5 < puntuacion:
    print ("Su rendimiento es MERITORIO")
    salario = puntuacion*2400
    print ("Su salario sera: " + str(salario))
            



    