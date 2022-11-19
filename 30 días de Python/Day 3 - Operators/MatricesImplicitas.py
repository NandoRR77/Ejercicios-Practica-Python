matriz = [[1,2],[3,4],[4,5]] #lista de listas

for filas in range(3): #3 filas
    for columnas in range(2): #2 columnas
        print(matriz[filas][columnas], end = '   ')
    print()