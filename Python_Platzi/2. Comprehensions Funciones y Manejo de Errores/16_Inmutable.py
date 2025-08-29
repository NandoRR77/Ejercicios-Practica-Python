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


#Agregar un nuevo atributo taxes al diccionario con map
#Defino una función para agregar los taxes

def add_taxes(item):
    # Acá agregamos una copia del diccionario para no afectar el original 
    # agregandole el nuevo atributo
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))

print('Diccionario original')
print(items)
print('Diccionario nuevo')
print(new_items)
