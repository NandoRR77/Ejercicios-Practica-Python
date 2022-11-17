print("Algoritmo para comparar números")
num1 = float(input(("Digite el primer número: "))) #captura el numero directamente del input
print("Digite el segundo número: ") # pide el número y luego lo almacena en la variable num2
num2 = float(input())

if num1<num2:
    print("El número", num1, " es menor que el número", num2)    
elif num1>num2: #elif es el sino del if principal
    print("El número", num1, " es mayor que el número", num2)
else:
    print("Los números son iguales")