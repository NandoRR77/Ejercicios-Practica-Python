person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

print(person)

person['twitter'] = '@nicobytes'  
person['twitter'] = '@nicobytes'   
person['name'] = 'Felipe'
del person['age']
print(person.keys())
print(person.values())
print(person)