'''
Ejercicio 3: Conversión con condición (Intermedio)Reto: Tienes una lista de 
temperaturas en grados Celsius (algunas positivas y otras negativas). 
Crea una nueva lista donde los números positivos se queden igual, pero 
los números negativos se conviertan a 0.
'''

temperaturas = [35, 28, -5, -10, 19, 26, -2]
print(f'Lista de temperaturas original {temperaturas}')

for indice, i in enumerate(temperaturas):
    if i < 0:
        temperaturas[indice] = 0
print(f'Lista de temperaturas modificada {temperaturas}')

#Con List Comprehesion

temperaturas_2 = [0 if i < 0 else i for i in temperaturas]
print(f'Lista nueva 2 con List comprehesion {temperaturas_2}')