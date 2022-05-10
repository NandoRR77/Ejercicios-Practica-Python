#Hallar IMC
from tokenize import PseudoExtras


print("HALLAR INDICE DE MASA CORPORAL")
print("Ingrese su estatura en MTS: ")
altura = float(input())
print("Ingrese su peso en KG: ")
peso = float(input())
imc = round((peso/(altura ** 2)),2)
print("Su índice de masa corporal es: ", imc,"%")
