def main(): #funcion principal
    print("Digite si, para continuar con el programa")
    respuesta = input("Desea continuar con el programa?: ")
    
    while respuesta == "si":
        respuesta = input("Desea continuar con el programa?: ")
        
    print("ha terminado el programa")
    
if __name__ == "__main__": #cuando se trabaja una funcion principal como main() y un while, la manera de invocarla es con __name__ y el nombre de la función
    main()