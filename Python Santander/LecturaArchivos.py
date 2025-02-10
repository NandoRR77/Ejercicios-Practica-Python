#Ingresar la ruta completa,cambiando \ por /
archivo = open("C:/Users/sslframirezr/Desktop/Ejercicios-Practica-Python/Python Santander/NuevosHorariosBOT.txt", "r")

#Almacenar el contenido del archivo en una variable
contenido = archivo.read()

#Imprimir la variable para ver el contenido del archivo
print(contenido)

#Cerrar archivo
archivo.close()