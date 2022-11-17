# modo de escritura
file = open("nando.txt", "w") #siempre abrimos el archivo y lo guardamos en una variable
file.close() #después de abrir y trabajar el archivo, conviene cerrarlo

# modo de lectura
file = open("nando.txt", "r")
file.close() #después de abrir y trabajar el archivo, conviene cerrarlo

# modo de escritura binaria
file = open("nando.txt", "wb")
file.close() #después de abrir y trabajar el archivo, conviene cerrarlo