'''
Declara una función denominada suma_de_números. Esta función toma un parámetro numérico y suma todos 
los números de ese rango.
'''

def suma_numeros(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

print(suma_numeros(100))