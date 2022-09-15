nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (M/F): ")
print ("--------------------------------")

if genero == "M":
    if nombre.lower() < "M":
        grupo = "A"
    
    else:
        grupo = "B"

else:
    if nombre.lower() > "N":
        grupo = "A"
        
    else:
        grupo = "B"
        
print ("Eres del grupo " + grupo)
   

    