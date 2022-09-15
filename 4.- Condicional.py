numero = int(input("Ingrese un numero: "))
print ("-----------------------------------------------")
div = 2

while numero%div != 0:
    div = div + 1 

if div == numero:
    print("El numero " + str(numero) + " es primo")

else:
    print("El numero " + str(numero) + " es par")
    