
estudiantesActivos = {1:["Fernando Ramirez"], 2:["Camila Ramirez"], 3:["Juan Sierra"], 4:["Cristina Mejia"]} #con value en [] lo hago tipo item para luego imprimir con este método

def numeroEstudiante(estudiantes, nombre):
    for identificacion, nombre in estudiantes.items():
        if nombre[0].lower() == nombreEstudiante.lower():
            return identificacion
        return 0

#funcion imprimir listado de estudiantes
def imprimirListadoEstudiantes(estudiantes):
    estudiantesActivos = estudiantes
    for identificacion, datos in estudiantes.items(): #con el metodo items puedo trabajar las listas que están dentro de un diccionario de manera separada
        print(f"El ID del estudiante es : {identificacion}")
        print(f"El nombre del estudiante es : {datos[0]}") #con la variable datos estoy tomando el nombre apellido como una lista en el diccionario en la posición 0
        print("  -------------------------------------  ")
        
print("Eliminar información")
eliminarEstudiante = int(input("Digite el ID delestudiante: "))
if eliminarEstudiante in estudiantesActivos:
    nombreEstudiante = estudiantesActivos[eliminarEstudiante][0]
    eliminarEstudiante = numeroEstudiante(estudiantesActivos, nombreEstudiante)
    del estudiantesActivos[eliminarEstudiante]
    print(f"el estudiante {nombreEstudiante} ha sido eliminado con éxito")
    imprimirListadoEstudiantes(estudiantesActivos)  
else:
    print("El estudiante no se encuentra registrado")