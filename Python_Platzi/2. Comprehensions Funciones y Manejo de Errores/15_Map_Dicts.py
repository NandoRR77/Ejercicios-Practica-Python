items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }    
]

#Obtener los precios de la lista de diccionarios en una nueva lista
prices = list(map(lambda item: item['price'], items))
print(prices)


#Agregar un nuevo atributo taxes al diccionario con map
#Defino una función para agregar los taxes

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))

print('Diccionario original')
print(items)
print('Diccionario nuevo')
print(new_items)