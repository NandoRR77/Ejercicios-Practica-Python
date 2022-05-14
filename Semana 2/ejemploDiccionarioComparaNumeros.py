''' Escribir un programa que me compare dos numeros y me diga cual es mayor, los numeros deben ser almacenados en un diccionario '''

numero1 = float(input("Ingrese por favor el primer número: "))
numero2 = float(input("Ingrese por favor el segundo número: "))

numerosDicc = {"Numero 1":numero1 , "Numero 2":numero2}

if numerosDicc["Numero 1"] == numerosDicc["Numero 2"]:
    print("Los números ", numerosDicc["Numero 1"], "y" , numerosDicc["Numero 2"], "son iguales")
elif numerosDicc["Numero 1"] > numerosDicc["Numero 2"]:
    print("el número ", numerosDicc["Numero 1"], "es mayor que el número ", numerosDicc["Numero 2"])

else:
    print("el número ", numerosDicc["Numero 1"], "es menor que el número ", numerosDicc["Numero 2"])
