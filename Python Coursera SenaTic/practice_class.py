'''Objetivo: Crear una clase que represente a una persona con nombre y edad, 
y un método para mostrar su información.'''

class Persona():
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f'El  nombre de la pesona es: {self.nombre} y su edad es: {self.edad}')
        
p1 = Persona("Nando", 42)
p1.mostrar_informacion()