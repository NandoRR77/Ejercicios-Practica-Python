#Pedir una edad y validar si es valida, si es mayor o menor de edad y que no sea mayor 90 años

edad = int(input("Por favor digite su edad: "))

if edad > 0 and edad <= 90:
    print("La edad es válida\n")
    if edad >= 18:
        print("La persona es mayor de edad\n")
    else:
        print("La persona es menor de edad\n")
else:
    print("La edad ingresada no es válida!\n")