#comidas = ['Pizza', 'Hamburguesa', 'Papas fritas', 'Ensalada', 'Helado']

numbers = [1,2,3,4,5,6,7,8,9,10]

#Filtrar solo los números pares con filter y lambda
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
