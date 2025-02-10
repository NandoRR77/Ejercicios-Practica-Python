def funcion_Salario(numHora: int, valHora:float):
    salario = numHora * valHora
    return "El valor de su salario es : ${} " .format(salario)

numHora = int(input("Ingrese la cantidad de horas laboradas: "))
valHora = float(input("Ingrese el valor de la hora en $: "))

print(funcion_Salario(numHora,valHora))  