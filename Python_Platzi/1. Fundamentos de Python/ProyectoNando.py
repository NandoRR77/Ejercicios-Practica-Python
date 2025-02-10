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
    
    print(f'Victorias usuario: {user_wins}')
    print(f'Victorias computadora: {computer_wins}')
    print(f'Empates: {draws}')
    
    user_option = input('Seleccione piedra, papel o tijera: \n')
    user_option = user_option.lower()
    
    rounds += 1  


    if not user_option in options:
        print(f'Opción {user_option} seleccionada no válida')
        continue
        
    computer_option = random.choice(options) #Escoger una opción aleatoria de la tupla o lista options

    if user_option == computer_option:
        print('Empate!')
        draws += 1
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Usuario gana!')
            user_wins =+ 1
        else:
            print('Papel gana a piedra')
            print('Computadora gana')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Usuario gana')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('Computadora gana')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('Usuario gana')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Computadora gana')
            computer_wins += 1
            
    if computer_wins == 3:
        print(f'El ganador absoluto es la computadora. Victorias {computer_wins}')
        break
    
    if user_wins == 3:
        print(f'El ganador absoluto es el usuario. Victorias {user_wins}')
        break