nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

personas = {"nombre":nombre, "apellido":apellido, "edad":edad, "anio_nacimiento":0}

def funcionEdadAlta(personas:dict):
    name = personas["nombre"]
    lastName = personas["apellido"]
    age = personas["edad"]
    year = personas["anio_nacimiento"]
    
    if age >= 0 and age < 18:
        year = 2022 - age #calcular el tiempo que le falta para ser mayor de edad
        mayorEdad = year + 18 #calcular el año en que sería mayor de 18
        
        return name, lastName, "Eres menor de edad, no podemos darte de alta hasta el año", mayorEdad
    
    elif age > 18 and age < 25:
        return "tienes un 10% de descuento"
    
    elif age > 25 and age < 100:
        return "Lo sentimos pero no tienes descuento"
    
    elif age == 18 or age == 25:
        return "Premio, tienes un descuento especial del 20%"
    
    elif age < 0:
        return "no se puede calcular la edad"
    
    elif age > 100:
        return "¿Sigue vivo?"  
    else:
        return "Dato no válido"
   
print(funcionEdadAlta(personas))