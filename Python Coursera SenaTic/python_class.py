class Recipe():
    def __init__(self, dish, items, time): #Método constructor con los atributos como parámetros
        self.dish = dish                    #Atibutos
        self.items = items                  #Atibutos
        self.time = time                    #Atibutos
        
    def contents(self):                     #Defino otro método que imprime una cadena con los atributos de la clase
        print('The ' + self.dish + ' has ' + str(self.items) + \
            ' and takes ' + str(self.time) + '  min to prepare') 
    
pizza = Recipe('Pizza', ['cheese', 'bread', 'tomato'], 45) #Instancio un objeto de la clase Recipe
pasta = Recipe('Pasta', ['penne', 'sauce'], 55)             #Instancio otro objeto de la clase Recipe

print(pizza.items)                          #Accedo al atributo items de la instancia pizza      
print(pasta.dish)                           #Accedo al atributo dish de la instancia pizza

print(pizza.contents())                     #Accedo al método contents() declarado en la clase pero con los datos de la instancia pizza
print(pasta.contents())                     #Accedo al método contents() declarado en la clase pero con los datos de la instancia pasta