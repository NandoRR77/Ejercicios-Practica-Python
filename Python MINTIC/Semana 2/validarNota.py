#Ingresar numero y validar: si está entre 0 y 3: reprobado, entre 3 y 5 aprobado, pero si es negativo o mayor a 5, error

nota = float(input("Ingrese nota: "))

if nota < 0 or nota >5:
    print("ERROR: Ingrese una nota válida")
elif nota >=0 and nota <3:
    print("REPROBADO")
else:
    print("APROBADO")