'''
Declara una función llamada capitalize_list_items. Toma una lista como parámetro y devuelve una lista de elementos en mayúsculas
'''

def capitalize_list_items(list, element):
    list.append(element)
    list_capitalize = []
    for item in list:
        item2 = item.upper()
        list_capitalize.append(item2)
    print(list_capitalize)
        
capitalize_list_items(['nando','cesar'], 'camila')