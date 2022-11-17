#Pedir 3 números y ordenarlos de mayor a menor

def funcionNumeroMayor(informacion:dict) -> dict(): #Defino la funcion y como parametro tiene un diccionario. -> dict() indica que es un diccionario pero no es necesario
    
    a = informacion["Numero1"] # la variable a contiene el valor de la clave "Numero1" y la utilizo para las comparaciones en la función
    b = informacion["Numero2"] # la variable b contiene el valor de la clave "Numero2" y la utilizo para las comparaciones en la función
    c = informacion["Numero3"] # la variable c contiene el valor de la clave "Numero3" y la utilizo para las comparaciones en la función
    
    if (a > b and b > c):
        print(f"El orden de los números de mayor a menor es: {a}, {b}, {c}")
        
    elif(a > c and b > c):
        print(f"El orden de los números de mayor a menor es: {a}, {c}, {b}")  
    
    elif(b > a and a > c):
        print(f"El orden de los números de mayor a menor es: {b}, {a}, {c}")
        
    elif (b > c and c > a):  
        print(f"El orden de los números de mayor a menor es: {b}, {c}, {a}")
    
    elif (c > a and a > b ):
        print(f"El orden de los números de mayor a menor es: {c}, {a}, {b}")
        
    elif (c > b and b > a):
        print(f"El orden de los números de mayor a menor es: {c}, {b}, {a}")
        
    else:
        print(f"Alguno de los números son iguales")   
        
numero1 = int(input("Ingrese el número 1: ")) #solicito a los usuarios información de los números y los convierto en enteros
numero2 = int(input("Ingrese el número 2: ")) #solicito a los usuarios información de los números y los convierto en enteros
numero3 = int(input("Ingrese el número 3: ")) #solicito a los usuarios información de los números y los convierto en enteros
          
informacion = {"Numero1":numero1, "Numero2":numero2, "Numero3":numero3} #asigno valores a las claves de acuerdo a lo ingresado por el usuario

funcionNumeroMayor(informacion) #invoco la funcion y como parametro paso el diccionario. Como use prints en el proceso de la función, en esta parte no lo pongo.