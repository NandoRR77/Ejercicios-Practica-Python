#Pedir al usurio que digite dos valores y despues qu escoja la operación a 
#ejecutar S-s = suma, R-r = resta, M-m = multiplicación, D-d = División

num1 = float(input("Por favor ingrese el primer valor: "))
num2 = float(input("Por favor ingrese el segundo valor: "))

operacion = input("Por favor digite la operación a realizar:\n S=suma\n R=resta\n M=multiplicación\n D=División\n") .upper() #si es upper() la comparación de los valores es en mayúscula, si es lower() la comparación es en minúscula

if (operacion == "S"):
    suma = num1 + num2
    print(f"La operación seleccionada fue Suma y el resultado de sumar {num1} y {num2} es= {suma}")

elif (operacion == "R"):
    resta = num1 - num2
    print(f"La operación seleccionada fue Resta y el resultado de restar {num1} y {num2} es= {resta}") 

elif (operacion == "M"):
    multiplicacion = num1 * num2
    print(f"La operación seleccionada fue Multiplicación y el resultado de multiplicar {num1} y {num2} es= {multiplicacion}") 

elif (operacion == "D"):
    if num2 == 0:
        print("ERROR: El divisor no puede ser cero")
    else:
        division = num1 / num2
        print(f"La operación seleccionada fue División y el resultado de dividir {num1} entre {num2} es= {division}")

else:
    print(f"ERROR: El valor ingresado ({operacion}) no es válido")