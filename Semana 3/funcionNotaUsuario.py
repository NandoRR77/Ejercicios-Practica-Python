#pedir una nota de 0 a 10 y mostrar de la forma: Insuficiente 0 - 5, Suficiente 6 - 7, Bien 8 - 9, Excelente 9,00001 - 10

def funcionCalificacion(informacion:dict):
    nota = informacion["nota1"]
    
    if (nota < 0 or nota >10):
        return "Ingresó una nota inválida"
    
    elif(nota <= 5):
        return "la calificación es INSUFICIENTE"
    
    elif(nota <= 7):
        return "la calificación es SUFICIENTE"
    
    elif(nota <= 9.00001):
        return "la calificación es BUENA"
    
    else:
        return "la calificación es EXCELENTE"
        
nota1 = float(input("Por favor ingrese su nota: "))

informacion = {"nota1":nota1}

print(funcionCalificacion(informacion)) #utilizo print porque en el proceso de la función, usé return