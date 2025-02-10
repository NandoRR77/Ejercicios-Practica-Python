#Calcular área de un círculo
def funcionAreaCirculo(radio: float):
    area = (3.1416 * (radio ** 2))
    return "El área del circulo {} es: ," .format(area)

radio = float(input("Ingrese el radio del círculo: "))
print(funcionAreaCirculo(radio))