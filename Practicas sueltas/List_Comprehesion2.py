'''
Ejercicio 2: Filtrar nombres cortos (Intermedio-Bajo)Reto: 
Dada una lista de nombres de frutas (por ejemplo: "manzana", "pera", 
"platano", "uva", "kiwi"), 
genera una nueva lista que solo incluya las frutas que tienen 4 letras o 
menos.
'''

frutas = ["manzana", "pera", "platano", "uva", "kiwi"]
print(f'Lista original {frutas}')

frutas_2 = []
for fruta in frutas:
    if len(fruta) <= 4:
        frutas_2.append(fruta)
print(f'Lista nueva {frutas_2}')

#Con List comprehesion
frutas_3 = [fruta for fruta in frutas if len(fruta) <= 4]
print(f'Lista nueva 2 con List comprehesion {frutas_3}')