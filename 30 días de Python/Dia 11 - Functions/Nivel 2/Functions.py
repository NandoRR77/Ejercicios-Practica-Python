'''
Declara una función denominada evens_and_odds . Toma un entero positivo como parámetro y 
cuenta la cantidad de pares e impares en el número.
'''

def evens_and_odds(num):
    count_evens = 0
    count_odds = 0

    for i in range(num+1):
        if i % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
            
    print(f'La cantidad de números pares es: {count_evens} \nLa cantidad de números impares es: {count_odds}') 

evens_and_odds(100)