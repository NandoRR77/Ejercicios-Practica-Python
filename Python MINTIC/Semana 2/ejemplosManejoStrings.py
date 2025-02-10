#Ejemplo 1 - manejo de string como vector, longitud del vector, posiciones
fruta = "aguacate"              #toda variable string es una cadena de caracteres, es decir un vector y sus posiciones comienzan desde el 0 (cero)
letra = fruta[6]                #con esto estamos capturando la letra t de la variable fruta, recordar que empieza a numerarse desde el 0 (cero)
longitud = len(fruta)           #len mide la longitud del vector fruta
ultimo = fruta[longitud - 1]    #imprime la última letra de la variable fruta.
print(letra)
print(longitud)
print(ultimo)


#Ejemplo 2 - Imprimir posición específica del vector
mensaje = "Hoy es viernes"
longitud2 = len(mensaje)
print(longitud2)
print(mensaje[7:14])             #con [n:m] le doy las coordenadas de lo que quiero escribir. Para la última posición le debo sumar 1, si quiero escribir viernes, las coordenadas serìan [7:15] porque la longitud total es 14+1


#Ejemplo 3 - concatenación cadenas, tipo de dato, métodos para manejo de cadenas
saludo = "Hola como estás? "
saludo2 = "Bien gracias"
print(saludo + saludo2)             #concatenar dos variables de cadena
print(f"{saludo} ,bien y vos")      #concatenar con format y variable
print(type(saludo))                 #imprime el tipo de dato de la variable
print(dir(saludo2))                 #imprime el listado de todos los métodos disponibles para el objeto/variable 


#Ejemplo 4 - manejo de mayusculas y minúsculas
mensaje2 = "fernando ramirez"
mensaje3 = "CAMILA RAMIREZ"
mayuscula = mensaje2.upper()        #convierte un string a mayúsculas
minuscula = mensaje3.lower()        #convierte un string a minúsculas
print(mayuscula)
print(minuscula)


#Ejemplo 5 - búsqueda en una cadena
mensaje3 = "Cuántas a hay en esta cadena"
buscar = mensaje3.find("a")
print(f"En la cadena {mensaje3} hay {buscar} letras a ")


#Ejemplo 6 - eliminar espacios en blanco o tabulaciones antes del primer caracter
mensaje4 = "          Ingrese nombre"
limpiar = mensaje4.strip()
print(limpiar)
print(mensaje4)


#Ejemplo 7 - buscar si comienza o termina una cadena en otra
mensaje5 = "Ingrese nombre"
buscaComienza = mensaje5.startswith("Ingrese")  #como lo buscado es "Ingrese" es con lo que comienza la cadena mensaje5, devuelve true
buscaTermina = mensaje5.endswith("nombre")      #como lo buscado es  "nombre "es con lo que termina la cadena mensaje5, devuelve true
print(buscaComienza)
print(buscaTermina)


#Ejemplo 7 - concatenar una cadena con una variable numérica
mensaje6 = 39
print("El próximo domingo cumples %d años" %mensaje6)       


#Ejemplo 8 - buscar y contar una cadena en otra
mensaje7 = "Para ganar el curso de python debes estar siempre en modo onfire"
print(mensaje7.count("on"))                     #voy a buscar y contar la cadena "on" en la cadena mensaje7, encontrará 2 en pythON y ONfire
print(mensaje7.count("on",28))                  #voy a buscar y contar la cadena "on" en la cadena mensaje7 después de la posición 28, encontrará 1 ONfire
print(mensaje7.count("on",0,28))                #voy a buscar y contar la cadena "on" en la cadena mensaje7 entre la posición 0 y 28, encontrará 0


#Ejemplo 9 - buscar y reemplazar una cadena en otra
mensaje8 = "Para ganar el curso de python debes estar siempre en modo onfire"
print(mensaje8.replace("on","NANDO"))               #voy a buscar "on" en la cadena mensaje7 y reemplzaralo por "NANDO", nuevo texto "Para ganar el curso de pythNANDO debes estar siempre en modo NANDOfire"