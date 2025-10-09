'''
Exercises: Level 1

1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1. Find the length of the set it_companies
print('# 1. Find the length of the set it_companies')

len_it_companies = (len(it_companies))
print(f'The len of {it_companies} is {len_it_companies} elements')

print('****************************************************\n')


#2. Add 'Twitter' to it_companies
print('# 2. Add Twitter to it_companies')
new_company = 'Twitter'
it_companies.add(new_company)
print(f'The new company is {new_company} and was added to {it_companies}')

print('****************************************************\n')


#3. Insert multiple IT companies at once to the set it_companies
print('#3. Insert multiple IT companies at once to the set it_companies')

new_companies = ['Xiaomi', 'HUAWEI', 'Samsung']
it_companies.update(new_companies)
print(f'The new companies are {new_companies} and they were added to {it_companies}')

print('****************************************************\n')


#4. Remove one of the companies from the set it_companies
print('#4. Remove one of the companies from the set it_companies')
removed_company = 'Xiaomi'
it_companies.remove(removed_company)
print(f'The removed company was {removed_company} and was removed to {it_companies}')

print('****************************************************\n')


#5. What is the difference between remove and discard
print('5. What is the difference between remove and discard')

print('''El método remove() genera error si al intentar eliminar este no existe en el set.
         El método discard() elimina el elemento si existe en el set, si no existe no genera error 
         ni lanza una excepción''')

print('****************************************************\n')