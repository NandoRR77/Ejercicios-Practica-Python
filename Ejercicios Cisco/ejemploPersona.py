class Persona:
    def __init__(self, nombre, apellido):
        self.nombre =  nombre
        self.apellido =  apellido
        
    #Crear método que permita imprimir la persona
    def imprimirPersona(self):
        return f"La nueva persona es {self.nombre} {self.apellido}"

nombre = str(input("Por favor ingrese su nombre: "))
apellido = str(input("Por favor ingrese su apellido: "))
    
persona1=Persona(nombre, apellido)
print(persona1.imprimirPersona())
