palabraSalida = "chupacabra"
palabraEntrada = input("Por favor ingresa la palabra secreta: ")

while True:
    if palabraEntrada != palabraSalida:
        palabraEntrada = input("Por favor ingresa la palabra secreta: ")
    if palabraEntrada == palabraSalida:
        print("¡Has dejado el bucle con éxito")
        break
    
    
from platform import processor

print(processor())