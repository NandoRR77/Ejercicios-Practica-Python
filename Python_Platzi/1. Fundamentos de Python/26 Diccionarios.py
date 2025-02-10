my_dict = {}
print(type(my_dict))

my_dict = {
    'avión': 'bla bla bla',
    'name' : 'Fernando',
    'last_name' : 'Ramirez',
    'age' : 41 
}

print(my_dict)
print(len(my_dict)) #conocer la cantidad de elementos que tiene el diccionario

print(my_dict['name']) #Leer una valor ingresando la llave 'name'
print(my_dict.get('age')) #otra forma de leer un valor con el método .get()
print(my_dict.get('escolaridad')) #si no existe la llave, arroja None y se puede manejar el error

print('avión' in my_dict) #conocer si una llave está en un diccionario, True or False
print('direccion' in my_dict) # si no está, arroja false