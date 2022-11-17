#Programa digite 3 números y diga cual es mayor

num1 = float(input("Por favor ingrese el primer número: "))
num2 = float(input("Por favor ingrese el segundo número: "))
num3 = float(input("Por favor ingrese el tercer número: "))


if (num1>num2 and num1>num3):
    print(f"El numero mayor es: {num1}")
elif (num2>num3):
    print(f"El numero mayor es: {num2}")
elif (num3>num2):
    print(f"El numero mayor es: {num3}")
elif (num1 == num2 and num2 == num3 and num1 == num3):
    print("Los números son iguales")
