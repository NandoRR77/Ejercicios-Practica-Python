# Paso 1 :  Crear diccionario con datos que estén creados
estudiantesActivos = {1:["Fernando Ramirez"], 2:["Camila Ramirez"], 3:["Juan Sierra"], 4:["Cristina Mejia"]} #con value en [] lo hago tipo item para luego imprimir con este método

# Paso 2 :  pedir información del usuario
print("Cargar estudiante")

identificacionEstudiante = int(input("Digite el ID del estudiante: "))
nombreEstudiante = str(input("Digite el nombre del estudiante: "))

# Paso 3 : Crear funciones de cargar  estudiantes e imprimir listado total de estudiantes

#funcion cargar estudiantes
#en las funciones, los parametros tiene que tener un nombre diferente pero similar a lo que por ejemplo, capturo para alimentar el diccionario
def cargarEstudiante(identificacion: int, nombre: str):
    estudiantesActivos[identificacion]=[nombre] #el = en este caso indica que en el dieccionario va a cargar identi y nombre 
    print("La información ha sido cargada con éxito")
    return estudiantesActivos

#funcion imprimir listado de estudiantes
def imprimirListadoEstudiantes(estudiantes):
    estudiantesActivos = estudiantes
    for identificacion, datos in estudiantes.items(): #con el metodo items puedo trabajar las listas que están dentro de un diccionario de manera separada
        print(f"El ID del estudiante es : {identificacion}")
        print(f"El nombre del estudiante es : {datos[0]}") #con la variable datos estoy tomando el nombre apellido como una lista en el diccionario en la posición 0
        print("  -------------------------------------  ")
        
estudiantesActivos = cargarEstudiante(identificacionEstudiante, nombreEstudiante)

#paso 4 : invocar la función
imprimirListadoEstudiantes(estudiantesActivos)