###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

print('Ejercicio 1:')
numbers = [1,2,3,4,5]
print(f'Lista números original {numbers}')

#Agregar número 6 con append
numbers.append(6)
print(f'Agregar el número 6 al final de la lista números {numbers}')

#Inserta el número 10 en la posición 2 usando insert()
numbers.insert(1,10)
print(f'Inserta el número 10 en la posición 2 usando insert() lista números {numbers}')

#Modifica el primer elemento de la lista para que sea 0.
numbers[0] = 0
print(f'odifica el primer elemento de la lista para que sea 0 en lista números {numbers}')


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

print('\nEjercicio 2:')
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

# Extiende lista_a con lista_b usando extend().
lista_a.extend(lista_b)
print(f'*Extiende lista_a con lista_b usando extend() {lista_a}')

# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
print(f'*Elimina la primera aparición del número 1 en lista_a usando remove(). {lista_a}')

# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
borrado = lista_a.pop(3)
print(f'*Elemento eliminado {borrado}. Nueva lista {lista_a}')

# Limpia completamente lista_b usando clear().
lista_b.clear()
print(f'*Limpia completamente lista_b usando clear(). \nLa lista queda con los siguientes elementos:{lista_b}')


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print('\nEjercicio 3:')
# Crea una lista con los números del 1 al 10.
lista = [i for i in range(1,11)]
print(f'*Crea una lista con los números del 1 al 10. {lista}')

# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
del lista[2:5]
print(f'*Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).')
print(f' Nueva Lista {lista}')

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print('\nEjercicio 4:')
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
numeros = [5, 2, 8, 1, 9, 4, 2]
print(f'*Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2] {numeros}')

# Ordena la lista de forma ascendente usando sort().
numeros.sort()
print(f'*Ordena la lista de forma ascendente usando sort().\n{numeros}') 

# Cuenta cuántas veces aparece el número 2 en la lista usando count().
conteo = numeros.count(2)
print(f'*Cuenta cuántas veces aparece el número 2 en la lista usando count().\n El número 2 aparece {conteo} veces en la lista {numeros}') 

# Comprueba si el número 7 está en la lista usando in.
print(f'*Comprueba si el número 7 está en la lista usando in..\n El número 7 aparece en la lista {numeros}?  => {7 in numeros}') 


