#Despejar X en ecuación

from re import X


def funcionDespejarX(num1: float, num2: float):
    x = num2 - num1
   
    return "El valor de la X es: {} " .format(x)

num1 = float(input("ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))

print("Para la ecuación ",num1,"+ X =",num2)
print(funcionDespejarX(num1,num2))
