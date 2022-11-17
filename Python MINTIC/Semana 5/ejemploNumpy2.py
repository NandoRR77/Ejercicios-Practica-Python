import numpy as np

#Array de 1 dimensión = lista, vector
a1 = np.array([1,2,3,4])
print(a1)
print()

#Array de 2 dimensiones   
a2 = np.array([[1,2,3,4], [5,6,7,8]])
print(a2)
print(a2[1,0]) #imprimir la posición 1,0 o sea, el 5  porque es fila 1 posición 0
print(a2[1][0])#imprimir la posición 1,0 o sea, el 5  porque es fila 1 posición 0
print()

#Array de 3 dimensiones 
a3 = np.array([[[1,2,3], [4,5,6,],[7,8,9],[10,11,12],[13,14,15], [16,17,18]]])
print(a3)
print()

#operaciones con matrices
c = np.array([[1,2,3,4], [5,6,7,8]])
d = np.array([[4,10,13,24], [15,18,17,28]])

print(c + d) #genera una nueva matriz con el resultado de la suma
print()
print(c - d) #genera una nueva matriz con el resultado de la resta
print()
print(c * d) #genera una nueva matriz con el resultado de la multiplicación
print()
print(c / d) #genera una nueva matriz con el resultado de la división
print()
print(c ** 2) #genera una nueva matriz con el resultado de la potencia
print()