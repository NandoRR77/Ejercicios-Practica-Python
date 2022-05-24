lista = ["Andres","Michael","Noemy","Nando","Cristina"] #para crear una lista se usan []
print(lista) #imprime toda la lista
print(lista[0]) #con esto imprimo la primera posición que empieza en 0
print(len(lista)) #lingitud de la lista
print(lista[-1]) #navegación inversa, voy a navegar de atrás hacia adelante. Desde el último elemento hasta el principio. Siempre empieza en -1
print(lista[0:2]) #imprimir rango, con este se imprimen los dos primeros elementos de la lista

lista[0] = "Edgar" #reemplazo el valor actual de la posición
print(lista)

if "Michael" in lista: #buscar un valor en una lista
    print("Si se encuentra en la lista")
else:
    print("No se encuentra en la lista")
    

for nombres in lista: #iterar información de una lista. En este caso la variable nombres almacena los elementos de la lista sin "" y la imprime linea por linea
    print(nombres)
    
    
lista.append("Juan Manuel") #agregar un elemento al final de la lista
print(lista)


lista.insert(0,"Frank") #agregar un elemento en una posición específica
print(lista)

lista.remove("Michael") #remover un elemento de la lista
print(lista)

lista.pop() #remover el último elemento de la lista
print(lista)

del lista[3] #remover la posición 4 de la lista (recordar que empieza en 0)
print(lista)

lista.clear() #borrar todos los elementos de la lista
print(lista)