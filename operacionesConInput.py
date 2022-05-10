print("Ingrese número 1: ")
num1 = float(input()) #Debemos especificar que sea float para que tome decimales y enteros
print("Ingrese número 2: ")
num2 = float(input())

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
divEntera = num1 // num2 #solo muestra la parte entera de la division
potencia = num1 ** num2
residuo = num1 % num2

print("La suma de los números ", num1 , "+" , num2 ,"es: " , suma)
print("La resta de los números ", num1 , "-" , num2 ,"es: " , resta)
print("El producto de los números ", num1 , "*" , num2 ,"es: " , multiplicacion)
print("La división entre los números ", num1 , "/" , num2 ,"es: " , division)
print("La división entera entre los números ", num1 , "/" , num2 ,"es: " , divEntera)
print("La potencia de los números ", num1 , "^" , num2 ,"es: " , potencia)
print("El residuo de los números ", num1 , "mod" , num2 ,"es: " , residuo)