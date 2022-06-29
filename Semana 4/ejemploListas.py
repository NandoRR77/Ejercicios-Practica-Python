asignaturas = ["matematicas","fisica","quimica","historia","lengua"]
aprobado = []

for asignatura in asignaturas: #la variable asignatura va a guardar cada elemento de la lista asignaturas
    nota = float(input(f"digite la nota {asignatura} ")) #captura una nota y la asocia a la asignatura
    
    while nota > 5 or nota <0:
        print("Ingrese una nota entre 0 y 5")
        nota = float(input(f"digite la nota {asignatura} "))        
    else:
        if nota >=3: 
            aprobado.append(asignatura) #si la nota es mayor o igual a 3, almacena la asignatura en la lista aprobado
print("Ya no hay mas notas para ingresar")

for asignatura in aprobado: 
    asignaturas.remove(asignatura)
print(f"Tiene que repetir las siguientes asignaturas: {asignaturas}")
