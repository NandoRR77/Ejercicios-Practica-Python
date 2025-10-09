'''
Exercises: Day 8

1. Create an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using items() method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries

'''

#1. Create an empty dictionary called dog
print('# 1. Create an empty dictionary called dog')

dog = {}

print(f'Variable dog is type {type(dog)}')

print('****************************************************\n')


#2. Create an empty dictionary called dog
print('# 2. Add name, color, breed, legs, age to the dog dictionary')

print(f'Agregando clave "name" al diccionario dog')
dog['name'] = 'Cindy'
print(f'Imprimiendo diccionario >= {dog}')

print(f'\nAgregando clave "color" al diccionario dog')
dog['color'] = 'light-brown'
print(f'Imprimiendo diccionario >= {dog}')

print(f'\nAgregando clave "breed" al diccionario dog')
dog['breed'] = 'chow-chow'
print(f'Imprimiendo diccionario >= {dog}')

print(f'\nAgregando clave "legs" al diccionario dog')
dog['legs'] = 4
print(f'Imprimiendo diccionario >= {dog}')

print(f'\nAgregando clave "age" al diccionario dog')
dog['age'] = 8
print(f'Imprimiendo diccionario >= {dog}')


print('****************************************************\n')


#3. Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary

print('# 3. Create a student dictionary')

student = {
    'first_name':'Luis',
    'last_name': 'Ramirez',
    'gender': 'Male',
    'age': 42,
    'marital_status': 'Marriaged',
    'skills': ['SQL, Python, Excel, Data Analytics, RPA'],
    'country': 'Colombia',
    'city': 'Bello',
    'address': 'Carrera 60 64 91 int 201',
}

print(f'Dictionary Student {student}')

print('****************************************************\n')


#4. Get the length of the student dictionary
print('4. Get the length of the student dictionary')

print(f'Dictionary Lenght {len(student)} elements')
print(student.keys())
print(student.values())
print(student.items())

print('****************************************************\n')


#5. Get the value of skills and check the data type, it should be a list
print('5. Get the value of skills and check the data type, it should be a list')

print(f'The values of key "Skills" are: {student["skills"]}')
type_skills = type(student['skills'])
print(f'The type of key "Skills" are: {type_skills} ')


print('****************************************************\n')


#6. Modify the skills values by adding one or two skills
print('6. Modify the skills values by adding one or two skills')

print(f'\nLos valores de la clave "Skills" son: {student["skills"]}')

print(f'\nAgregando valores "Story Telling" y "Power BI" a  clave "skills"')

student['skills'].append('Story Telling') 
student['skills'].append('Power BI') 

print(f'\nNuevos valores agregados a la clave "skills" {student['skills']} ')

print('****************************************************\n')

#7. Get the dictionary keys as a list
print('7. Get the dictionary keys as a list\n')

for i in student:
    keys_list = list(student.keys())
print(f'La lista de keys del diccionario student es: \n{keys_list}')

print('****************************************************\n')

#8. Get the dictionary values as a list
print('8. Get the dictionary values as a list\n')

for i in student:
    values_list = list(student.values())
print(f'La lista de keys del diccionario student es: \n{values_list}')

print('****************************************************\n')


#9. Change the dictionary to a list of tuples using items() method
print('9. Change the dictionary to a list of tuples using items() method\n')

tuplas_student = student.items()

print(f'El diccionario "student" convertido a tuplas es \n{tuplas_student}')

#implementar imprimir las tuplas con lambda
#for i in tuplas_student:
#    print(i)

#imprime_tuplas = list(map(lambda i: print(i), range(len(tuplas_student))))

print('****************************************************\n')


#10. Delete one of the items in the dictionary
print('10. Delete one of the items in the dictionary\n')

print(f'Items originales diccionario "student": \n{student}')
print(f'\nEliminando item "skills" diccionario "student": \n')

del student['skills']

print(f'Diccionario "student" actualizado item "skills" : \n{student}')

print('****************************************************\n')


#11. Delete one of the dictionaries
print('11. Delete one of the dictionaries\n')

print(f'Diccionario "student": \n{student}')
print(f'\nEliminando diccionario "student": \n')

del student

print(f'Diccionario "student" eliminado')

print('****************************************************\n')