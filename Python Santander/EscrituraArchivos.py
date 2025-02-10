'''Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). 
Si el archivo no existe, se creará automáticamente. 
Si el archivo ya existe, su contenido se sobrescribirá.
'''

#Abrir archivo
archivo = open("C:/Users/sslframirezr/Desktop/Ejercicios-Practica-Python/Python Santander/PruebaEscritura.txt", "w")

#sobreescribir o crear archivo con el texto "Hola, mundo!"
archivo.write("Hola, mundo!")

#Abrir archivo creado
archivo = open("C:/Users/sslframirezr/Desktop/Ejercicios-Practica-Python/Python Santander/PruebaEscritura.txt", "r")

#Almacenar contenido del archivo en una variable e imprimirlo
contenido = archivo.read()
print(contenido)

#Cerrar archivo
archivo.close()

