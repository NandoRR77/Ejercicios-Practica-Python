'''
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt 
la tabla de multiplicar de ese número, done n es el número introducido.
''' 

def tabla_n():
    num = int(input("Ingrese un número entre 1 y 10: "))
    nom_file = 'tabla-n' + str(num) + '.txt'
    with open(nom_file,'w')as file:
        for i in range(1,11):
            file.write(str(num) + ' X ' + str(i) + ' = ' + str(num*i) + '\n')

tabla_n()