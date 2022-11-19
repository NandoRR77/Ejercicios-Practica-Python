#Matriz con elementos en blanco

a = [] #lista vacía
m = 3 #filas
n = 2 #columnas

#crear la estructura de la matriz en memoria con valores vacíos None
for f in range(m):
    a.append([])
    for c in range(n):
        a[f].append(None)
        
# llenamos la matriz creada en el punto anterior
for f in range(m):
    a.append([])
    for c in range(n):
        print(a[f][c], end = '   ')
    print(' ')