#Calcular el perímetro y área del triangulo

def funcionTrigangulo(base:float, lado:float, altura: float):
    perimetro = base + lado + altura
    area = (base * altura) / 2
    return "El perimetro del triangulo es: {} cms y el área es: {} cms" .format(perimetro,area) #con esto relaciono las dos variables de la formula de la funcion y las formateo
    return "El área del triangulo es: {}, " .format(area)

base = float(input("Ingrese la base del triangulo: "))
lado = float(input("Ingrese los lados del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

print(funcionTrigangulo(base,lado,altura))
