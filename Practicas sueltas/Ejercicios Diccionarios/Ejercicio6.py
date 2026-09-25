'''
Ejercicio 6:

La Necesidad del Cliente (Misión AlphaLabs):
El equipo de despacho necesita procesar el camión de AlphaLabs. 
Tu misión es escribir un print(...) de acceso directo que extraiga el segundo artículo de su lista 
de items (el resultado en tu consola debe ser "Monitor").

pedidos = [
    {
        "cliente": "TechCorp",
        "detalles": {
            "prioridad": "Alta",
            "items": ["Servidor", "Switch", "Router"]
        }
    },
    {
        "cliente": "AlphaLabs",
        "detalles": {
            "prioridad": "Media",
            "items": ["Laptop", "Monitor"]
        }
    },
    {
        "cliente": "BetaOmega",
        "detalles": {
            "prioridad": "Baja",
            "items": ["Teclado", "Mouse", "Cables", "Hub USB"]
        }
    }
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

pedidos = [
    {
        "cliente": "TechCorp",
        "detalles": {
            "prioridad": "Alta",
            "items": ["Servidor", "Switch", "Router"]
        }
    },
    {
        "cliente": "AlphaLabs",
        "detalles": {
            "prioridad": "Media",
            "items": ["Laptop", "Monitor"]
        }
    },
    {
        "cliente": "BetaOmega",
        "detalles": {
            "prioridad": "Baja",
            "items": ["Teclado", "Mouse", "Cables", "Hub USB"]
        }
    }
]

print('\nReto 0:')
print(f'Ruta para encontrar el {pedidos[1]["detalles"]["items"][1]} en la estructura:\n pedidos[1]["detalles"]["items"][1]\n')


'''
Reto 1: El accesorio faltante
El cliente TechCorp (el primero de la lista) llamó para reportar que olvidó añadir un artículo. 
Modifica la estructura agregando el producto "Rack para Servidores" al final de su lista de items.

Tu objetivo: Ejecutar la línea de código correspondiente y luego imprimir pedidos[0] para verificar 
que el artículo se sumó con éxito.
'''

print('\n*'*3)
print('Reto 1:\n')
pedidos[0]["detalles"]["items"].append("Rack para Servidores")
print(f'Ruta para agregar "Rack para servidores" : \n pedidos[0]["detalles"]["items"].append("Rack para Servidores"')
print('Imprimir el cliente completo con el artículo agregado:\n' , pedidos[0])


'''
Reto 2: Registro de entrega
Para mejorar la logística, el departamento de sistemas necesita que el diccionario de detalles de 
BetaOmega (el tercer cliente) incluya una nueva etiqueta llamada "fecha_entrega" 
con el valor "Mañana".

Tu objetivo: 
Escribir la línea de asignación correspondiente y luego verificar el cambio con un print.

'''
print('\n*'*3)
print('Reto 2:\n')
pedidos[2]["detalles"]["fecha_entrega"] = "Mañana"
print(pedidos[2])

'''
Reto 3: Corrección de identidad 
(Cambiar el nombre de AlphaLabs a "Alpha Laboratories Inc.").
'''
print('\n*'*3)
print('Reto 3:\n')

pedidos[1]["cliente"] = "Alpha Laboratories Inc."
print(pedidos[1]["cliente"])

'''
Reto 4: Cambio de prioridades 
(Subir la prioridad de BetaOmega, el tercer cliente, de "Baja" a "Urgente").
'''

print('\n*'*3)
print('Reto 4:\n')

pedidos[2]["detalles"]["prioridad"] = "Urgente"
print(pedidos[2]["detalles"]["prioridad"])

'''
Reto 5: El buscador automático de ítems
Escribe un bucle for tradicional que recorra toda la lista pedidos. 
El bucle debe buscar dinámicamente al cliente cuyo nombre sea "TechCorp" y, cuando lo encuentre, 
imprimir únicamente su lista de items.
'''

print('\n*'*3)
print('Reto 5:\n')

for pedido in pedidos:
    if pedido["cliente"] == "TechCorp":
        print(f'Lista de artículos {pedido["detalles"]["items"]} del cliente {pedido["cliente"]}')


'''
Reto 6: Auditoría de Alta Prioridad
Escribe un bucle for que analice todos los pedidos e imprima en la pantalla el nombre del cliente 
únicamente si su prioridad de envío es igual a "Alta".

(Resultado esperado: Debería imprimir en pantalla únicamente el texto "TechCorp" de manera automática).
'''

print('\n*'*3)
print('Reto 6:\n')

for pedido in pedidos:
    if pedido["detalles"]["prioridad"] == "Alta":
        print(f'Para la prioridad Alta, se tiene el cliente {pedido["cliente"]}')