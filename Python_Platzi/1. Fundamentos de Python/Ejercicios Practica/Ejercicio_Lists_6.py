'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario 
tiene que repetir.
'''

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
perdidas = []

for asignatura in asignaturas:
    nota = float(input(f'Ingrese la nota para {asignatura} => \n'))
    if nota < 0 or nota > 5:
        print(f'La nota {nota} ingresada no es válida.')
        print(f'El programa ha finalizado')
        break
    elif nota <= 3:
        perdidas.append(asignatura)
        continue
for asignatura in perdidas:
    asignaturas.remove(asignatura)

print(f'Las asignaturas a repetir son {asignaturas}')