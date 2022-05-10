print("Ingrese el primer número")
num1 = float(input())
print("Ingrese el segundo número")
num2 = float(input())

if num1<num2:
    print("El número", num1, " es menor que el número", num2)    
elif num1>num2: #elif es el sino del if principal
    print("El número", num1, " es mayor que el número", num2)
else:
    print("Los números son iguales")
