import random

#Juego piedra papel o tijera
options = ('piedra','papel', 'tijera')

rounds = 1
user_wins = 0
computer_wins = 0
draws = 0

while True:

    print('*' * 20)
    print(f'Round {rounds}')
    print('*' * 20)
    
    print(f'\nVictorias usuario: {user_wins}')
    print(f'Victorias computadora: {computer_wins}')
    print(f'Empates: {draws}')
    
    user_option = input('Seleccione piedra, papel o tijera: \n')
    user_option = user_option.lower()
    
    rounds += 1  


    if not user_option in options:
        print(f'Opción {user_option} seleccionada no válida')
        continue
        
    computer_option = random.choice(options) #Escoger una opción aleatoria de la tupla o lista options
    
    print(f'\nOpción usuario: {user_option}')
    print(f'Opción computadora: {computer_option}')

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
            
    if computer_wins == 2:
        print(f'\nEl ganador absoluto es la computadora. Victorias {computer_wins}')
        break
    
    if user_wins == 2:
        print(f'\nEl ganador absoluto es el usuario. Victorias {user_wins}')
        break