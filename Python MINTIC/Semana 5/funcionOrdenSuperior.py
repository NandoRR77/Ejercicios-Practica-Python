def conversor(sis): #funcion de orden superior (conversos) y parametro de orden superior (sis)
    
    def sis_bin(numero):
        print(f"El número decimal {numero}, en binario es {bin(numero)}")
    
    def sis_oct(numero):
        print(f"El número decimal {numero}, en octal es {oct(numero)}")
        
    def sis_hex(numero):
        print(f"El número decimal {numero}, en hexadecimal es {hex(numero)}")
    
    sisFun = {"bin":sis_bin , "oct":sis_oct , "hex":sis_hex} #diccionario con el nombre de la funciòn y llama/ejecuta la funciono asociada
    return sisFun[sis]

#convertir un número decimal a binario
numeroCon = int(input("Por favor ingrese el número: ")) #numeroCon es la variable global, la variable numero es la local de las funciones, siempre debemos trabajar variables locales diferentes pero similares en nombre a las globales
conversor("bin")(numeroCon)
conversor("oct")(numeroCon)
conversor("hex")(numeroCon)
