#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.

sum = 0

for i in range(101):
    sum += i
print(f'The sum of all numbers is: {sum}')

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.

sum_pares = 0
sum_impares = 0

for x in range(0,101,1):
    if x % 2 == 0:
        sum_pares += x
    else:
        sum_impares += x

print(f'The sum of all evens is: {sum_pares}')
print(f'The sum of all evens is: {sum_impares}')