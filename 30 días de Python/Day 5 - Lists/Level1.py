''' Exercises: Level 1
#1. Declare an empty list
list = []

#2. Declare a list with more than 5 items
list = [1,2,3,4,5]

#3. Find the length of your list
print(len(list))

#4. Get the first item, the middle item and the last item of the list
print(list[0])
print(list[2])
print(list[-1])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Fernando', 39, 1.78, 'Married', 'cra 60 64 91 int 201']
print(mixed_data_types)

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[4])
print(it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[6] = 'Instagram'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('Sololearn')
print(it_companies)

#12 Insert an IT company in the middle of the companies list
it_companies.insert(4,'Sony')
print(it_companies)
e
#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14. Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
string = ['#;  ']
it_companies = it_companies + string
print(it_companies)

#15. Check if a certain company exists in the it_companies list.
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
word = input('Ingrese una compañía: ')
exists_in = word in it_companies
if word in it_companies:
    print(f'The search of company {word} in IT Companies is {exists_in} in position {it_companies.index(word)}')
else:
    print(f'The search of company {word} in IT Companies is {exists_in}')

#16. Sort the list using sort() method
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
it_companies.sort()
print(it_companies)    

#17. Reverse the list in descending order using reverse() method
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
it_companies.reverse()
print(it_companies)  

#18. Slice out the first 3 companies from the list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
it_companies = it_companies[:3]
print(it_companies)

#19. Slice out the last 3 companies from the list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
it_companies = it_companies[-3:]
print(it_companies)

#20. Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
#middle = (int(len(it_companies) // 2)) con esto hallo la mitad entera de la lista
it_companies = it_companies[:(int(len(it_companies) // 2))]
print(it_companies)

#21. Remove the first IT company from the list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
del it_companies[0]
print(it_companies)


#22. Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
middle = (int(len(it_companies) // 2))
print(f'El elemento a eliminar es {it_companies[middle]}')

deleted = it_companies[middle]
del it_companies[middle]

print(f'Se ha eliminado {deleted} de la lista IT Companies {it_companies}')


#23. Remove the last IT company from the list

it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
last = it_companies[-1]
print(f'El elemento a eliminar es {last}')

deleted = last
it_companies.pop(-1)

print(f'Se ha eliminado {deleted} de la lista IT Companies {it_companies}')

#24. Remove all IT companies from the list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
it_companies = ['Facebook', 'GOOGLE', 'Microsoft', 'Apple', 'Sony', 'IBM', 'Oracle', 'Instagram', 'Sololearn']

try:
    del it_companies
    print('Lista eliminada, no se puede imprimir su contenido')
except:    
    print('Lista eliminada!')

'''
#26. Join the following lists:
    #front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    #back_end = ['Node','Express', 'MongoDB']
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.index('Redux') #conocer el indice de Redux

full_stack.insert(full_stack.index('Redux')+1, 'Python') #agregar python después de redux
full_stack.insert(full_stack.index('Redux')+2, 'SQL') #agregar SQL después de Python
print(full_stack)
