niveles = int(input("Introduzca el numero de niveles: "))
print ("----------------------")

for i in range(1, niveles + 1, 2):
    for j in range(i, 0, -2):
        print(j, end = " ")
    print(" ")
