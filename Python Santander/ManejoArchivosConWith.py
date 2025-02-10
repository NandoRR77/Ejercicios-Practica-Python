#Utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.

with open("C:/Users/sslframirezr/Desktop/Ejercicios-Practica-Python/Python Santander/Datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
