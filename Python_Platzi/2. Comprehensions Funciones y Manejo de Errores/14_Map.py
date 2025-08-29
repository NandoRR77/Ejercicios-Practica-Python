#Map se usa para transformación de listas
#Vamos a hacer un ejemplo en donde dada una lista, la vamos a transformar generando una nueva lista con su doble

numbers = [1,2,3,4]
numbers_v2 = []
print(f'Lista inicial {numbers}')

#forma tradicional
for i in numbers:
    numbers_v2.append(i * 2)
print(f'Transformación tradicional con for {numbers_v2}')

#transformación con map y lambda
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(f'Transformación con map y lambda {numbers_v2}')


print('-'*15)
#Ejemplo con dos listas de diferente cantidad de elementos
num_1 = [5,6,7,8]
num_2 = [9,10,11]

print(num_1)
print(num_2)

#resultado va a ser la lista resultante de la iteración de la función map que recibe
#una lambda funcion y esta recibe como argumentos dos numeros y las dos listas a iterar
resultado = list(map(lambda x,y: x+y, num_1, num_2))

#la lista resultado solo va a tener 3 elementos que es la lista mas pequeña que obtuvo como parametros
print(resultado)