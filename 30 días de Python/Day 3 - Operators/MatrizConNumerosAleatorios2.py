from random import randint #importar libreria randint para enteros aleatorios
fila = 3
columna = 3
matriz = [[randint(1,100) for i in range(fila)] for j in range (columna)]

for f in matriz:
    print(f)
    
