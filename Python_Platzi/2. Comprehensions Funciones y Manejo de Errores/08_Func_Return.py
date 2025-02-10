#Sin función: numeros del 1 al 10 y sumarlos

sum = 0
for i in range (1,10):
    sum += i
print('Sin función => ', sum)

#con funcion: numeros del 1 al 10 y sumarlos

def suma2(inicio,fin):
    print('Paramestros de entrada: ', inicio, ',' ,fin)
    sum2 = 0
    for i in range (inicio,fin):
        sum2 += i
    return sum2

result = suma2(1,10)
print(result)

result2 = suma2(result, result + 10) #Uso el resultado como parametro de entrada de la nueva ejecución
print(result2)

result3 = suma2(result2,1000) #Uso result2 como parametro de entrada de la nueva ejecución
print(result3)