asignaturas = ["matematicas","fisica","quimica","historia","lengua"]
notas = []

for asignatura in asignaturas: #la variable asignatura va a guardar cada elemento de la lista asignaturas
    nota = float(input(f"digite la nota {asignatura} "))
    notas.append(nota)
print("Ya no hay mas notas para ingresar")

for i in range(len(asignaturas)):
    print(f"En la asignatura {asignaturas[i]} usted ha sacado {notas[i]}")