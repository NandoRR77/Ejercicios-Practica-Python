estudiantesActivos = {1:["Fernando Ramirez"], 2:["Camila Ramirez"], 3:["Juan Sierra"], 4:["Cristina Mejia"]} #con value en [] lo hago tipo item para luego imprimir con este método

print("Actualizar estudiante")
numeroEstudiante = int(input("Digite el ID del estudiante: "))
estudiantesActivos[numeroEstudiante][0]=str(input("Ingrese el nuevo nombre: "))
print(f"estudiante: {estudiantesActivos[numeroEstudiante][0]}, ha sido modificado con éxito")
print(" ------------------------------------ ")

#se puede mejorar este crud validando si el ID no existe, para crearlo

def imprimirListadoEstudiantes(estudiantes):
    for identificacion, datos in estudiantes.items(): #con el metodo items puedo trabajar las listas que están dentro de un diccionario de manera separada
        print(f"El ID del estudiante es : {identificacion}")
        print(f"El nombre del estudiante es : {datos[0]}") #con la variable datos estoy tomando el nombre apellido como una lista en el diccionario en la posición 0
        print("  -------------------------------------  ")
        
imprimirListadoEstudiantes(estudiantesActivos)