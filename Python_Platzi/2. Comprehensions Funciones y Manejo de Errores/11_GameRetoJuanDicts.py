'''
Le tengo otro pero es un poquto más dificil

1. Simplifique esa función check_rules para que no quede con tanto if elif.
Yo lo haría por otro lado
Juancolombio: Definiría un diccioanario con las reglas
rules = {
        'piedra': 'tijera',
        'papel': 'piedra',
        'tijera': 'papel'
    }
    
2. Pidale el nombre al usuario y lo imprime, "Nando" gana a computadora - OK

'''

import random

def choose_options():
    #Juego piedra papel o tijera
    options = ('piedra','papel', 'tijera')
    
    user_option = input('Seleccione piedra, papel o tijera: \n')
    user_option = user_option.lower()
    
    if not user_option in options:
        print(f'Opción {user_option} seleccionada no válida')
        return None, None
    
    #Escoger una opción aleatoria de la tupla o lista options   
    computer_option = random.choice(options)
    
    print(f'\nOpción usuario: {user_option}')
    print(f'Opción computadora: {computer_option}')
    return user_option, computer_option


''' Funcion check_rules() versión1

def check_rules(user_option, computer_option, user_wins, computer_wins, draws):   
    if user_option == computer_option:
        print('\nEmpate!')
        draws += 1
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('\nPiedra gana a tijera')
            print('Usuario gana!')
            user_wins += 1
        else:
            print('\nPapel gana a piedra')
            print('Computadora gana')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('\nPapel gana a piedra')
            print('Usuario gana')
            user_wins += 1
        else:
            print('\nTijera gana a papel')
            print('Computadora gana')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('\nTijera gana a papel')
            print('Usuario gana')
            user_wins += 1
        else:
            print('\nPiedra gana a tijera')
            print('Computadora gana')
            computer_wins += 1
    return user_wins, computer_wins, draws
'''

def check_rules(user_option, computer_option, user_wins, computer_wins, draws):
    
    #Este diccionario tiene las reglas de que elemento le gana a otro
    rules = {
        'piedra': 'tijera',
        'papel': 'piedra',
        'tijera': 'papel'
    }
        
    if user_option == computer_option:
        print('\nEmpate!')
        draws += 1
    elif rules[user_option] == computer_option:
        print('Usuario gana!')
        user_wins += 1
    else:
        print('Computadora gana')
        computer_wins += 1
    
    return user_wins, computer_wins, draws


def define_winner(user_wins,computer_wins):
    name_user = ''
    if computer_wins == 2:
        print(f'\nEl ganador absoluto es la computadora. Victorias {computer_wins}')
    elif user_wins == 2:
        name_user = input(str('Ingrese su nombre: \n'))
        print(f'\nEl ganador absoluto es {name_user}. Victorias {user_wins}')
    

    
def run_game():
    user_wins = 0
    computer_wins = 0
    draws = 0
    
    rounds = 1
     
    while user_wins < 2 and computer_wins < 2:
        print('\n')
        print('*' * 20)
        print(f'Round {rounds}')
        print('*' * 20)
        
        print(f'\nVictorias usuario: {user_wins}')
        print(f'Victorias computadora: {computer_wins}')
        print(f'Empates: {draws}')
        
        rounds += 1
        
        #Las variables user y computer option toman el valor de invocar la función choose_options()
        user_option, computer_option = choose_options()
        
        if user_option is None:
            continue
        
        user_wins, computer_wins, draws = check_rules(user_option,computer_option, user_wins, computer_wins, draws)
        
    define_winner(user_wins, computer_wins)
    
        
run_game()