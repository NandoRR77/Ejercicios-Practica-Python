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
print()
b = np.array([0,2,3,1,0,6,5,7,0,10,10,13,1,15])
print(np.argwhere(b!=0)) #imprime todos los indices menos donde esté 0 y los ordena


#Crear matriz 3x3x3 con elementos aleatorios
print()
c = np.random.random((3,3))
print(c) 


#crear matriz IDENTIDAD de 6X6 (en la diagonal principal lleva 1)
print()
r = np.identity(6)
print(r)

#Crear una matriz con valores al azar con forma 3*3*3
print()
s = np.random.random((3,3,3))
print(s)

#Encontrar los índices(posición) de los valores mínimos y máximos de la matriz anterior y su valor
print()
print(s.argmin())
print(s.ravel()[s.argmin()])
print()
print(s.argmax())
print(s.ravel()[s.argmax()])

#Crear una matriz de 10X10 con 1's en los bordes y 0 en el interior (con rangos de indices)
print()
z = np.ones((10,10)) #matriz de unos
z[1:-1, 1:-1]=0 #con esto reemplazo los unos de los bordes por ceros
print(z)

#Crear matriz 5x5 con valores en los renglones que vayan de 0 a 4
print()
print(np.tile(np.arange(0,5), 5) .reshape(5,5)) #con np.title le decimos que repita 5 veces la fila 0,1,2,3,4

#Crear dos arreglos al azar AyB y verificar si son iguales
print()
a = np.random.random((4,3))
b = np.random.random((4,3))
print(a == b)