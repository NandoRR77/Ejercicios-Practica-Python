#Función para calcular velocidad

def vel(tiempo: int, distancia: int):
    
    velocidad = tiempo / distancia
    return "La velocidad es: {} metros/segundos" .format(velocidad)

tiempo = int(input("Digite el tiempo (en segundos): "))
distancia = int(input("Digite la distancia (en metros): "))

print(vel(tiempo,distancia)) 