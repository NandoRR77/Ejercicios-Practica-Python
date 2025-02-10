#Realizar un programa que compruebe si dos números son múltiplos

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

numeros = {"numero1":numero1, "numero2":numero2}

def funcionMultiplos(numeros:dict):
    num1 = numeros["numero1"]
    num2 = numeros["numero2"]
    
    if (num1 >= num2 and num1 % num2 != 0):
        return num1, "no es multiplo de " , num2
    elif (num1 >= num2 and num1 % num2 == 0):
        return num1, "es multiplo de " , num2
    elif (num2 >= num1 and num2 % num1 != 0):
        return num2, "no es multiplo de " , num1
    else:
        return num2, "es multiplo de " , num1
    
print(funcionMultiplos(numeros))
        