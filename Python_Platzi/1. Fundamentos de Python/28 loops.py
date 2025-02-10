matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[0]) #Imprime primera posición de una lista que es una lista
print(matriz[0][1]) #imprime primera posición de una lista que es una lista y el segundo elemento

for row in matriz: #Recorre las filas de la matriz
    print(row) #Imprime la fila
    for column in row: #Recorre las columbas de la columna
        print(column) #Imprime la columna
        