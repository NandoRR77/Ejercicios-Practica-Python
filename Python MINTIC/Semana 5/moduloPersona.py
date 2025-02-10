class Persona: #las clases en singular y con mayúscula inicial
    def __init__(self, nombre, edad): #init es para inicializar una funcion dentro de la clase. self es para manejar las variables locales
        self.__nombre = nombre
        self.__edad = edad
        
    def __str__(self): #imprime cadena de caracteres
        return "El nombre es: " + self.__nombre + "y su edad es: " + str(self.__edad) #str(self.__edad) convierte la edad que es entero en str