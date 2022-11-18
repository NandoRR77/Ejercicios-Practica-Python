import numpy as np
#Suma,resta y multiplicación de matrices

m1 = np.array([[5, 12, 6],[-3, 0, 14]])
m2 = np.array([[9, 8, 7],[1, 3, -5]])

print("Suma: \n", (m1 + m2))
print("------------------------")

print("Resta: \n", (m1 - m2))
print("------------------------")

print("Multiplicacion: \n", (m1 * m2))
print("------------------------")

#Suma de escalar a una matriz, en python se permite
m1 + 2 


#Transpuesta de una matriz
mt = m2.T
print("La matriz transpuesta de: \n", m2 ,"\n es: \n", mt)
