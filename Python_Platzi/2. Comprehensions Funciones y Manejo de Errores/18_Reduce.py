import functools

numbers = [1,2,3,4]

#Transformar toda una lista a un solo valor
result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)