txt = input('Ingrese una cadena: ')

def words():
    #your code goes here
    for word in txt.split(' '):
        yield word
        
print(list(words()))
