class Persona: #las clases en singular y con mayúscula inicial
    def __init__(self, nombre, edad): #init es para inicializar una funcion dentro de la clase. self es para manejar las variables∫ locales
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self): #imprime cadena de caracteres
        return "{} tiene {} años ".format(self.nombre, self.edad)
    
personas = [ #lista personas con las instancias de Personas
    Persona("Juan", 15),
    Persona("Andres", 25),    
    Persona("Nando", 3),
    Persona("Cristina",4)
]

menorEdad = filter(lambda Persona: Persona.edad < 18, personas) #sirve para filtrar elementos. Lambda sirve para iterar 
for menor in menorEdad:
    print(menor)