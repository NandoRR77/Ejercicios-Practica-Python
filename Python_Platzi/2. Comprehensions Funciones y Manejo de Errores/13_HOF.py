def increment (x):
    return x + 1

#version lambda de la función increment
increment_v2 = lambda x: x + 1

#Esta función recibe dos parámetros, una x y otra función
def high_ord_func (x, func):
    return x + func(x)

#version lambda de la funcion high_ord_func
high_ord_func_v2 = lambda x, func : x + func(x)

# En la variable result  voy a guardar el resultado de la ejecución de la funcion high_ord_fun
# a la cual le estoy pasando como parametro el 2 (x) y una función (incremente)
# en este caso, recibirá un 2 y al ejecutarse la función increment() que también recibe un 2 como 
# parámetro, devolverá 2 + 1 = 3
# El resultado total será 5
result = high_ord_func(2, increment)

#ejecutar las lambdas
result_v2 = high_ord_func(2, increment_v2)


print(f'Ejeciución HOF normales {result}')
print(f'Ejeciución HOF lambdas {result_v2}')

#Podría por ejemplo pasarse una lambda funcion como parámetro de la HOF
#Cambio la funcion lambda
result_v3 = high_ord_func(2, lambda x: x + 1)
print(result_v3)

#Cambiando otra vez la lambda
result_v3 = high_ord_func(3, lambda x: x * 5)
print(result_v3)