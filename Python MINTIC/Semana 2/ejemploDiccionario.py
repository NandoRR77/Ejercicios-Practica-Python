colores = {"verde":"green","blanco":"white","negro":"black"} #Los diccionarios se definen con {} y los elementos con []
print(type(colores))            #imprime la clase diccionario
print(colores)                  #imprime todos los elementos del diccionario
print(colores["verde"])         #imprime el valor designado para la clave principal, siempre el primer valor es la clave("verde") y el segundo el valor("green") en el elemento "verde":"green" y siempre debemos llamar la clave
print(colores["blanco"])        #imprime white

colores["amarillo"] = "yellow"  #agrego una nueva clave y valor al diccionario colores
print(colores)                  #imprimo nuevamente el diccionario para ver todos los elementos

colores["amarillo"] = "red "    #cambio/sobreescribo el valor de la clave amarillo
print(colores)                  #imprimo nuevamente el diccionario para ver todos los elementos
