'''
Utilice bucles anidados para crear lo siguiente:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''

'''
#Solución 1
print('Solución 1 => ')
string = '# # # # # # # #'

for i in range(8):
    print(string)
'''
    
#Solución 2
print('\nSolución 2 => ')

matriz = [
    '# # # # # # # #',
    '# # # # # # # #',
    '# # # # # # # #',
    '# # # # # # # #',
    '# # # # # # # #',
    '# # # # # # # #',
    '# # # # # # # #',
    '# # # # # # # #'
]

for row in matriz: #obtengo cada fila de la matriz = 8
    for x in range(1): #itero 1 vez
        print(row)      #imprimo la variable row que son 8 filas con #