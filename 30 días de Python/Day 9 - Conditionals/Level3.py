'''
Exercises: Day 8

Exercises: Level 3

1. Here we have a person dictionary. Feel free to modify it!
    person={
    
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }
    

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, 
 Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
 Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
 
 Asabeneh Yetayeh lives in Finland. He is married.

'''



#1. Validaciones en diccionario person
print('# 1. Validaciones en diccionario person')

person = {
    
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
}



#A. Validar elemento del medio de la lista skills
print('A. Validar elemento del medio de la lista skills')

clave = 'skills'

def validar_skills(clave):
    for habilidad, resultado in person.items():
        if clave in habilidad:
            mid = (len(resultado)//2)
            return f'El valor medio de la lista {resultado} es {(resultado[mid])}'
    return f'Habilidad no existe en el diccionario'

print(validar_skills(clave))

print('****************************************************\n')


#B. Validar si el elemento Python existe en la lista skills
print('B. Validar si el elemento Python existe en la lista skills')

clave = 'skills'
valor = 'Python'

def validar_skill_python(clave,valor):
    for habilidad, resultado in person.items():
        if clave in habilidad and valor in resultado:
            return f'El elemento {valor} se encuentra en la lista de habilidades {resultado} '
    return f'El elemento {valor} no existe en el diccionario'

print(validar_skill_python(clave,valor))

print('****************************************************\n')


#C. Validar tipo de programador según habilidades
print('C. Validar tipo de programador según habilidades')


def valida_desarrollador(skills):
      
    skills = set(person['skills']) #Convertir la lista a un set

    # Agrupar en sets las diferentes habilidades para operar con sets
    skills_frontend = {'JavaScript', 'React'}
    skills_backend = {'Node', 'Python', 'MongoDB'}
    skills_fullstack = {'React', 'Node', 'MongoDB'}
    
    
    if skills_frontend.issubset(skills):
        return 'He is a front end developer'
    elif skills_backend.issubset(skills):
        return 'He is a backend developer'
    elif skills_fullstack.issubset(skills):
        return 'He is a fullstack developer'
    else:
        return 'unknown title'

print(valida_desarrollador(person['skills']))

print('****************************************************\n')


#D. Validar If the person is married and if he lives in Finland imprimir Asabeneh Yetayeh lives in Finland. He is married.
print('D. Validar If the person is married and if he lives in Finland')

if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')}. He is married')


print('****************************************************\n')