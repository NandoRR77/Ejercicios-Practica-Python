#Calcular distancia recorrida
def funcionDistancia(velocidad: float, tiempo: float):
    distancia = velocidad * tiempo
    return "La distancia recorrida es: {} km" .format(distancia)

velocidad = float(input("Por favor ingrese la velocidad en km/h "))
tiempo = float(input("Por favor ingrese el tiempo en segundos "))

print(funcionDistancia(velocidad,tiempo))