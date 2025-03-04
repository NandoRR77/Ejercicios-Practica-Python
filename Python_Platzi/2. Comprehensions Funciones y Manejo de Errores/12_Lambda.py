####Ejemplo 1
#Función normal de incremento

def increment(x):
    return x + 1

print(increment(10))


#Transformar a lambda function
lambda x : x + 1 #transformo la función 

increment_v2 = lambda x : x + 1 #asigno la función a una variable

#imprimo la variable a la que le asigné la función y a la función le paso el parametro (x)
print(increment_v2(20)) 


####Ejemplo 2
#Creo la función
full_name = lambda name, last_name : f'Full name is: {name.capitalize()} {last_name.capitalize()}'

#Asigno la función a una variable y le paso los parámetros a la función
text = full_name('fernando','ramírez')

#Imprimo la variable con la ejecución
print(text)