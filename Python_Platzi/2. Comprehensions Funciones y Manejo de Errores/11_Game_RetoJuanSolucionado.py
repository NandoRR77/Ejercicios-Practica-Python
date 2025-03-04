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


def check_rules(user_option, computer_option, user_wins, computer_wins, draws):
    # Definimos las reglas en un diccionario
    rules = {
        'piedra': 'tijera',
        'papel': 'piedra',
        'tijera': 'papel'
    }
    
    # Si son iguales, es un empate
    if user_option == computer_option:
        print('\nEmpate!')
        draws += 1
    # Si la opción del usuario vence a la opción de la computadora
    elif rules[user_option] == computer_option:
        print(f'\n{user_option.capitalize()} gana a {computer_option.capitalize()}')
        print('Usuario gana!')
        user_wins += 1
    else:
        # Si no es empate y no ganó el usuario, ganó la computadora
        print(f'\n{computer_option.capitalize()} gana a {user_option.capitalize()}')
        print('Computadora gana')
        computer_wins += 1

    return user_wins, computer_wins, draws



def define_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print(f'\nEl ganador absoluto es la computadora. Victorias {computer_wins}')
    elif user_wins == 2:
        print(f'\nEl ganador absoluto es el usuario. Victorias {user_wins}')


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
        
        # Las variables user y computer option toman el valor de invocar la función choose_options()
        user_option, computer_option = choose_options()
        # Se agregó esto por si escriben mal una opcion
        if user_option is None:
            continue
        
        user_wins, computer_wins, draws = check_rules(user_option, computer_option, user_wins, computer_wins, draws)
       
        # Aquí ya no llamamos a define_winner, solo lo hacemos al final
       
    define_winner(user_wins, computer_wins)  # Aquí se define al ganador al final

run_game()
