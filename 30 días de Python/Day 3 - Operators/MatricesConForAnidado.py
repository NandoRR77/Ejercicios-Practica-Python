'''
#Matriz unidimensional de 6 filas
print ('Matriz unidimensional de 6 filas')
for i in range (1,7):
    print(i)    
print ('\n')

#Matriz unidimensional de 6 columnas
print ('Matriz unidimensional de 6 columnas')
for i in range (1,7):
    print(i, end = '  ')

print ('\n')

#Matriz bidimensional de ceros de 6 x 6
#for anidado
print ('Matriz bidimensional de ceros de 6 x 6')
for i in range(1,7): # imprime filas
    for j in range(1,7): # imprime columnas
        print(0, end = '   ') # imprime 6 columnas con 0 separados con 3 espacios 
    print('')#con esto deja un espacio cada que imprime una fila
print ('\n')


#Matriz bidimensional con coordenadas de i y j de 6 x 6
#for anidado
print ('Matriz bidimensional con coordenadas de i y j de 6 x 6')
for i in range(1,7): # imprime filas
    for j in range(1,7): # imprime columnas
        print(f'({i},{j})' , end = '   ')# imprime en cada columna, las coordenadas de i y j
    print('')#con esto deja un espacio cada que imprime una fila
'''
    
#Matriz bidimensional con 1 en diagonal principal de 6 x 6 
#for anidado
print ('Matriz bidimensional con 1 en diagonal principal de 6 x 6')
for i in range(1,7): # imprime filas
    for j in range(1,7): # imprime columnas
        if (i==j): #preguntamos si en la coordenada la i y la j es igual, esto indica que es la diagonal y ponemos 1
            print(1, end = '   ') #imprime 1 en cada columna, cuando las coordenadas de i y j son iguales
        else:
            print(0, end = '   ')# imprime 0 en cada columna, cuando las coordenadas de i y j no son iguales
    print('')#con esto deja un espacio cada que imprime una fila