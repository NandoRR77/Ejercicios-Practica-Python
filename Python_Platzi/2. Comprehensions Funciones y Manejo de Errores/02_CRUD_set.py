set_countries = {'colombia', 'mexico' , 'bolivia'}

size = len(set_countries)
print(size)

#buscar elementos en un set
print('colombia' in set_countries)
print('peru' in set_countries)

#agregar elementos (add)
set_countries.add('ecuador')
print(set_countries)

#actualizar elementos (update)
set_countries.update({'argentina', 'peru', 'ecuador'})
print(set_countries)

#eliminar elementos (remove)
set_countries.remove('colombia')
print(set_countries)

set_countries.discard('uruguay') #si no existe el elemento a eliminar no genera error
print(set_countries)

set_countries.pop() #eliminar ultima posición
print(set_countries)

set_countries.clear() #eliminar todo el conjunto
print(set_countries)