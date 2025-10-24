'''
Escriba una función llamada add_all_nums que tome una cantidad arbitraria de argumentos y sume todos los argumentos. 
Verifique si todos los elementos de la lista son de tipo numérico. 
Si no es así, proporcione una respuesta razonable.
'''


def f_dd_all_nums(*args):
    numbers = []
    total = 0
    for num in args:
        has_numeric_values = any(isinstance(num, (str)) for num in args) #Validación valores string
        if has_numeric_values: 
            print("La lista contiene elementos diferentes a números")
            break 
        else: 
            numbers.append(num)
            total += num
    print(f'Los números ingresados fueron {numbers} \nSuman en total {total}')
f_dd_all_nums(1,3,7,4,'a')