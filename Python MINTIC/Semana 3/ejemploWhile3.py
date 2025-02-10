#Bucle que se ejecute mientras un número sea positivo y calcule la raiz cuadrada

import math #importar la librerìa math donde està para hacer la raiz cuadrada

numero = int(input("Por favor ingrese el número: "))

while (numero < 0):
    print("El número ingresado es negativo")
    numero = int(input("Debe ingresar un número positivo: "))

print(f"La raiz cuadrada de {numero} es: {(math.sqrt(numero)): .2f}") # .2f es formato de dos decimales