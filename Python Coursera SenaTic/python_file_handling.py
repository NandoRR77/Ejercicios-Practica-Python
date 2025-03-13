#mode = r - > lectura
#mode = rb - > lectura (formato binario)
#mode = r+ - > lectura y escritura
#mode = rb+ - > lectura y escritura (formato binario)
#mode = w - > escritura (sobreescribe)
#mode = wb - > escritura (formato binario)
#mode = a - > editar y agregar datos
#mode = ab - > editar y agregar datos (formato binario)

file = open('/Users/nandoramirez/Desktop/Ejercicios-Practica-Python/Python Coursera SenaTic/test.txt', mode = 'r') #mode = 'r' es para lectura

data = file.readline() #lee la primera linea

print(data)

file.close()

