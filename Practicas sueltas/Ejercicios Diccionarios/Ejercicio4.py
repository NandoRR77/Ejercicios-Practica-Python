'''
Ejercicio 4: Agrupar alumnos por curso

Tienes una lista de alumnos. 

Crea un diccionario vacío llamado cursos. Tu objetivo es recorrer la lista de alumnos y agruparlos 
dentro del diccionario de modo que las claves sean los cursos ('A' o 'B') y los valores sean listas
con los nombres de los alumnos que pertenecen a ese curso.

Estructura de datos:

alumnos = [
    {"nombre": "Ana", "curso": "A"},
    {"nombre": "Carlos", "curso": "B"},
    {"nombre": "Luis", "curso": "A"},
    {"nombre": "Sofía", "curso": "B"}
]

Salida:

cursos = {
    "A": ["Ana", "Luis"],
    "B": ["Carlos", "Sofía"]
}

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

alumnos = [
    {"nombre": "Ana", "curso": "A"},
    {"nombre": "Carlos", "curso": "B"},
    {"nombre": "Luis", "curso": "A"},
    {"nombre": "Sofía", "curso": "B"}
]

#Solución con for

cursos = {
    "A": [],
    "B": []
    }

print(alumnos[0]['curso'])

for alumno in alumnos:
    if alumno['curso'] == "A":
        cursos["A"].append(alumno["nombre"])
    else:
        if alumno['curso'] == "B":
            cursos["B"].append(alumno["nombre"])
print(cursos)