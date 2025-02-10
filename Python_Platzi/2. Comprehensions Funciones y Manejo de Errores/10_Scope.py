price = 100 # Global

def increment():
    price = 200 # Contexto local
    price = price + 10
    return price
    
print(price)
increment()

price_2 = increment()
print(price_2)