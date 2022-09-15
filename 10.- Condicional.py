print ("Bienvenidos a la pizzeria Bella Napoli")
print ("vegetariano 1/no_vegetariano 2")
print (" ")
tipo = int(input("Elija su tipo de pizza: "))
print ("--------------------------------")

if tipo == 1:
    print ("Usted eligio una pizza vegetariana")
    print ("Pimiento 1/ Tofu 2")
    print (" ")
    ingrediente = int(input("Que ingrediente le va a poner a su pizza: "))
    print ("--------------------------------")
    
    if ingrediente == 1:
        print ("Su pizza tiene: ")
        print ("- Tomate")
        print ("- Mozzarella")
        print ("- Pimiento")
    
    elif ingrediente == 2:
        print ("Su pizza tiene: ")
        print ("- Tomate")
        print ("- Mozzarella")
        print ("- Tofu")
    
    
elif tipo == 2:
    print ("Usted eligio una pizza no vegetariana")
    print ("Peperoni 1/ Jamon 2/ Salmon 3")
    print (" ")
    ingrediente = int(input("Que ingrediente le va a poner a su pizza: "))
    print ("--------------------------------")
   
    if ingrediente == 1:
        print ("Su pizza tiene: ")
        print ("- Tomate")
        print ("- Mozzarella")
        print ("- Peperoni")
    
    elif ingrediente == 2:
        print ("Su pizza tiene: ")
        print ("- Tomate")
        print ("- Mozzarella")
        print ("- Jamon")
        
    elif ingrediente == 3:
        print ("Su pizza tiene: ")
        print ("- Tomate")
        print ("- Mozzarella")
        print ("- Salmon")



            



    