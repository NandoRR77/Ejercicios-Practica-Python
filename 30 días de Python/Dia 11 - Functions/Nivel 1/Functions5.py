'''
Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
'''

def f_check_season(month):
    seasons = {
        12:'Winter', 1:'Winter', 2:'Winter', 
        3:'Spring', 4:'Spring', 5:'Spring',
        6:'Summer', 7:'Summer', 8:'Summer',
        9:'Autumn', 10:'Autumn', 11:'Autumn'
    }
    return (seasons[month])

print(f_check_season(12))