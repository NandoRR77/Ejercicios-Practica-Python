#ZeroDivisionError

#En matemáticas existen reglas sobre dividir por cero. El siguiente código intenta hacerlo 
# y mostrará un ZeroDivisionError. Agregue la gestión de excepciones para devolver 0 en lugar de permitir que se produzca el error.


# Starter code - NO LOGRADO
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print("0")
    
    
'''
Solución  plataforma
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)
'''