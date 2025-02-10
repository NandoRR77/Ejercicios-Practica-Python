'''
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print('Frutas normal => ' , fruits)

fruits_reversed = []

for i in range(len(fruits)-1,-1,-1):
    fruits_reversed.append(fruits[i])

print('Frutas inverso => ' , fruits_reversed)
    