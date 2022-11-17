numeros = []

for i in range(10):
    numero = (int(input(f"Por favor ingrese los numeros {i + 1} del 1 al 10: ")))
    while numero > 10 or numero <=0:
        print("Por favor ingrese un número entre 1 y 10")
        numero = (int(input(f"Por favor ingrese los numeros {i + 1} del 1 al 10: ")))
    numeros.append(numero)
    numeros.sort(reverse = True)
    
print(f"Los números ingresados y ordenados de mayor a menor son: {numeros}")