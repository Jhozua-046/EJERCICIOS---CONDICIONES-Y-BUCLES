contraseña = "contraseña"

def verificar():
    clave = input("Ingrese la contraseña: ")
    
    if (clave == contraseña):
        print("--------------------------------------")
        print("La contraseña es correcta")
    else:
        print("--------------------------------------")
        print("La contraseña es incorrecta")
        
verificar()