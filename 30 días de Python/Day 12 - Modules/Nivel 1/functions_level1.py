import random
import string


#1. Escriba una función que genere un id de usuario__ales_al_de seis dígitos/caracter.

def random_user_id():
    aleatorio = string.ascii_letters + string.digits
    id_aleatorio = ''.join(random.choice(aleatorio) for i in range(6))
    return id_aleatorio

print(random_user_id())

'''
2. Modifica la tarea anterior. Declara una función llamada user_id_gen_by_user. 
No toma ningún parámetro, pero toma dos entradas usando input(). 
Una de las entradas es el número de caracteres y la segunda entrada es el número de 
ID que se supone que se generan.
'''

def user_id_gen_by_user():
    
    num_caracteres = int(input('Ingrese la cantidad de caracteres que tendrá su id: '))
    num_ids = int(input('Ingrese la cantidad de ids que quiere generar: '))
    
    aleatorio_2 = string.ascii_letters + string.digits
    list_ids = []
    
    for x in range(num_ids):
        aleatorio_2 = ''.join(random.choice(aleatorio_2) for i in range(num_caracteres))
        list_ids.append(aleatorio_2)
    return list_ids

lista = user_id_gen_by_user()

for elemento in lista:
    print(elemento, end= '\n')