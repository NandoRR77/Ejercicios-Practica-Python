'''
Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números pares 
y la suma de todos los números impares.
'''

sum_pares = 0
sum_impares = 0
for x in range(101):
    if x % 2 == 0:
        sum_pares += x

    else:
        sum_impares += x
print(f'La suma de los números pares del 0 al 100 es => {sum_pares} y \nLa suma de los números impares del 0 al 100 es => {sum_impares}')

    