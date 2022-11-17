#vamos abrir el archivo e imprimir sus lineas como lista
print("Todas las líneas en una lista")
file = open("nando.txt","r")
linea = file.readlines() #sirve para saber las lineas (con salto de linea) que tiene el archivo y lo devuelve como lista
print(linea) # al final de cada linea tiene el separador \n
file.close


#con este for, podemos imprimir cada linea independiente
print("\nCon ciclo for para imprimir cada linea")
file = open("nando.txt","r")
for lineas in file:
    print(lineas)

file.close()