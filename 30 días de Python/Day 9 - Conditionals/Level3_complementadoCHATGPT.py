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
    

 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, 
 Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
 Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
 
 Asabeneh Yetayeh lives in Finland. He is married.

'''

#C. Validar tipo de programador según habilidades
print('C. Validar tipo de programador según habilidades')


# Diccionario base de la persona
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

# Función para determinar el tipo de desarrollador
def valida_desarrollador(skills_usuario):
    # Diccionario de categorías y sus conjuntos de habilidades
    categorias = {
        'front end developer': {'JavaScript', 'React'},
        'back end developer': {'Node', 'Python', 'MongoDB'},
        'full stack developer': {'React', 'Node', 'MongoDB'}
    }

    skills_usuario = set(skills_usuario)  # Convertir a conjunto

    # Recorremos las categorías
    for titulo, habilidades in categorias.items():
        if habilidades.issubset(skills_usuario):
            return f"He is a {titulo}"

    return 'Unknown title'


# --- Entrada del usuario ---
print("Habilidades disponibles:", ', '.join(person['skills']))

entrada = input("Escribe las habilidades que quieres validar (separadas por coma): ")

# Convertimos la entrada del usuario a lista y limpiamos espacios
skills_usuario = [s.strip() for s in entrada.split(',')]

# Llamamos a la función
resultado = valida_desarrollador(skills_usuario)

print(resultado)


print('****************************************************\n')