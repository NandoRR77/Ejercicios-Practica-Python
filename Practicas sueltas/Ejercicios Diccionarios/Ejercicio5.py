'''
Ejercicio 5:
Hubo un cambio en la estrategia de distribución. 
El equipo de inventario necesita auditar la categoría del segundo lote que está dentro del 
contenedor para asegurarse de que el camión refrigerado sea el correcto.

Tu Reto:
Escribe el print(...) con la combinación exacta de corchetes pegados a la variable contenedor para 
extraer directamente el texto de esa categoría (el resultado en pantalla debe ser "Línea Blanca").

contenedor = {
    "id_embarque": "EMB-2026",
    "destino": "Bogotá",
    "lote": [
        {
            "categoria": "Electrónica",
            "productos": ["Televisor", "Smartphone", "Audífonos"]
        },
        {
            "categoria": "Línea Blanca",
            "productos": ["Nevera", "Microondas", "Lavadora"]
        }
    ]
}

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

contenedor = {
    "id_embarque": "EMB-2026",
    "destino": "Bogotá",
    "lote": [
        {
            "categoria": "Electrónica",
            "productos": ["Televisor", "Smartphone", "Audífonos"]
        },
        {
            "categoria": "Línea Blanca",
            "productos": ["Nevera", "Microondas", "Lavadora"]
        }
    ]
}


print(contenedor["lote"][1]["categoria"])
