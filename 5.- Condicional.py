n1 = int(input("Ingrese su edad: "))
n2 = int(input("Ingrese su ingreso mensual: "))
print ("-----------------------------------------------")

while n1 > 16 & n2 > 999:
    print("Si puede tributar")

if n1 > 16:
    print("Es mayor de edad")
    print("Si puede tributar")

else:
    print("Edad no admitida")
    print("No puede tributar")
    
if n2 > 999:
    print("Sus ingresos son altos")
    print("Si puede tributar")

else:
    print("Ingresos insuficientes")
    print("No puede tributar")
    