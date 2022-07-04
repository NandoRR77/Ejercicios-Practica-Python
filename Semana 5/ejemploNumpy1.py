import numpy as np #importamos numpy y creamos un alias

a = np.arange(10,51) #generar un rango de 10 a 50
print()
print(a) #imprime la lista 

#navegación inversa
print()
print(a[-1]) 

#imprime lista invertida
print()
print(a[::-1]) 

#imprime un arreglo de 0 a 9 y redristribuyalo en una matriz 3x3
print()
print(np.arange(0,9).reshape(3,3)) 

#imprime un arreglo de 0 a 9 y redristribuyalo en una matriz 3x3
print()
print(np.arange(0,16).reshape(4,4)) 

#Genera impresion ordenada de un array
b = np.array([0,2,3,1,0,6,5,7,0,10,10,13,1,15])
print(np.argwhere(b!=0)) #imprime todos los indices menos donde esté 0 y los ordena

#Crear matriz 3x3x3 con elementos aleatorios
c = np.random.random((3,3))
print(c) 

#Encontrar los índices de los valores mínimo y máximos de la matriz anterior
print(c.argmax())
print(c.ravel()[c.argmax()])
print()
print(np.unravel_index(c.argmax(), c.shape))
print(c[np.unravel_index(c.argmax(), c.shape)])