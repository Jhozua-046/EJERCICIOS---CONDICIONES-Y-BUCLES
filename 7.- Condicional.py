renta = int(input("Ingrese su renta anual: "))
print ("--------------------------------")

if renta < 10000:
    print ("Su tipo de impositivo es 5%")

elif 10000 < renta < 20000:
    print ("Su tipo de impositivo es 15%")

elif 20000 < renta < 35000:
    print ("Su tipo de impositivo es 20%")
            
elif 35000 < renta < 60000:
    print ("Su tipo de impositivo es 30%")
                
elif 60000 < renta:
    print ("Su tipo de impositivo es 45%")


    