meses = ("enero","febrero","marzo","abril","mayo","junio","julio",
         "agosto","septiembre","octubre","noviembre","diciembre")

salir = False
while(not salir):
    
    numero = int(input("Digite un número: "))
    
    if(numero == 0):
        print("Ha terminado el programa")
        salir = True
    else:
        if(numero>=1 and numero<= len(meses)):
            print(meses[numero-1]) #imprime el valor ingresado por el usuario menos un para que coincida con el indice en la tupla
        else:
            print(f"Digite un número 1 y {len(meses)}")