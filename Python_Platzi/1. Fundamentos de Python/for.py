'''
#For con Range 1 sólo parámetro
for element in range(20): #range inicia desde 0 hasta el limite que se indique -1
    print(element)
'''    
 
'''    
#For con Range 2 parámetros
for element in range(1, 20): #acá se indica el elemento de inicio
    print(element)
    
'''
 
'''   
#For con Range 3 parámetros
for element in range(1, 20, 2): #acá se indica el elemento de inicio, el limite y el salto
    print(element)
'''

#Iterar una lista con for uno por uno
my_list = [ 23, 25, 26, 27]
for i in my_list:
    print(i)
    
    
#Iterar una tupla
my_tuple = ('Nando', 'jose', 'luis')
for i in my_tuple:
    print(i)
    

#Iterar un diccionario
my_dict = {
    'name': 'Camisa',
    'ID' : 123456,
    'Price': 100,
    'Stock': 5
}

for i in my_dict:
    #print(i) #Así me muestra solo las llaves
    print(my_dict[i]) #Así me muestra el valor de la llave en posición del elemento iterador

#mejorando la impresión
for key in my_dict:
    print(key, '=>' , my_dict[key])
    
#otra manera de imprimir la llave y el valor
for key, value in my_dict.items():
    print(key, '=>' , value)
    

#manipulando lista de diccionarios

people = [
    {
        'name': 'luis',
        'age': 41
    },
    {
        'name': 'juan',
        'age': 16
    },
    {   
        'name': 'cami',
        'age': 7
    }
]

for person in people:
    print(person) #imprimir todos los elementos de la lista de diccionarios
    print('name => ' , person['name']) #imprimir el valor