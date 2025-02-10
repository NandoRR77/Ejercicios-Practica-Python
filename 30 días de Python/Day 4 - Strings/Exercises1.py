''' #1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
text_a = 'Thirty'
text_b = 'Days'
text_c = 'Of'
text_d = 'Python'
space = ' '
string = text_a + space + text_b + space + text_c + space + text_d
print(string)

#2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
text_a = 'Coding'
text_b = 'For'
text_c = 'All'
space = ' '
string = text_a + space + text_b + space + text_c
print(string)

#3.Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4.Print the variable company using print().
print(company)

#5.Print the length of the company string using len() method and print().
print(len(company))

#6.Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7.Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9.Cut(slice) out the first word of "Coding For All" string.
company = "Coding For All"
cut_first_word = company[6:]
print(cut_first_word)

#10.Check if "Coding For All" string contains a word "Coding" using the method index, find or other methods.
company = "Coding For All"
substring = "Coding"
print(company.index(substring))
print(company.rindex(substring))
print(company.count(substring))
print(company.find(substring))
print(company.rfind(substring))

#11.Replace the word coding in the string 'Coding For All' to Python.
company = "Coding For All"
print(company.replace("Coding","Python"))

#12.Change Python for Everyone to Python for All using the replace method or other methods.
phrase = "Change Python for Everyone"
print(phrase.replace("Change Python for Everyone", "Python for All"))

#13.Split the string 'Coding For All' using space as the separator (split()) .
phrase = 'Coding For All'
phrase_splited = phrase.split(' ')
print(phrase_splited)

#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
phrase = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
phrase_splited = phrase.split(',')
print(phrase_splited)

#15.What is the character at index 0 in the string Coding For All.
string = 'Coding For All'
print(string[0])

#16.What is the last index of the string Coding For All
string = 'Coding For All'
print(string[-1])

#17.What character is at index 10 in "Coding For All" string.
string = 'Coding For All'
print(string[10])

#18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python For Everyone'
acronym = string[0]
for i in range (1, len(string)):
    if string [i - 1] == ' ':
        acronym += string[i]

acronym = acronym.upper()
print(acronym)

#19.Create an acronym or an abbreviation for the name 'Coding For All'.
string = 'Coding For All'
acronym = string[0]

for i in range(1, len(string)):
    if string [i -1] == ' ':
        acronym += string[i]

acronym = acronym.upper()
print(acronym)

#20.Use index to determine the position of the first occurrence of C in Coding For All.
string = 'Coding For All'
substring = 'C'
print(string.index(substring)+1)

#21.Use index to determine the position of the first occurrence of F in Coding For All.
string = 'Coding For All'
substring = 'F'
print(string.index(substring)+1)

#22.Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding For All'
substring = 'l'
print(string.rfind(substring)+1)

#23.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
substring = 'because'
print(len(string))
print(string.find(substring)+1)

#24.Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
substring = 'because'
print(len(string))
print(string.rfind(substring)+1)

#25.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.split('because because because'))

#26.Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
substring = 'because'
print(string.find('because')+1) #modo 1
print(string.find(substring)+1) #modo 2

#27.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.split('because because because'))

#28.Does ''Coding For All' start with a substring Coding?
string = 'Coding For All' 
substring = 'Coding'

#modo 1
if substring in string: 
    print('Yes')
else:
    print('No')

#modo 2
print(string.startswith(substring))
    
#29.Does 'Coding For All' end with a substring coding?
string = 'Coding For All' 
substring = 'coding'

#modo 1
if substring in string: 
    print('Yes')
else:
    print('No')

#modo 2
print(string.endswith(substring))

#30.'   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '

print(string.strip(' '))


#31.Which one of the following variables return True when we use the method isidentifier():
    #30DaysOfPython
    #thirty_days_of_python

lista=['30DaysOfPython','thirty_days_of_python']

for i in range(len(lista)):
    if lista[i].isidentifier():
        print(f'{lista[i]} is identifier')
    else:
        print(f'{lista[i]} is not identifier')


#32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.

list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list_join = ' '.join(list)
print(list_join)


#33.Use the new line escape sequence to separate the following sentences.
    #I am enjoying this challenge.
    #I just wonder what is next.

sentence1 = 'I am enjoying this challenge'
sentence2 = 'I just wonder what is next'
print(f'{sentence1}\n{sentence2}')

#34.Use a tab escape sequence to write the following lines.
    #Name      Age     Country   City
    #Asabeneh  250     Finland   Helsinki

print('Name      \tAge     \tCountry   \tCity')
print('Asabeneh  \t250     \tFinland   \tHelsinki')

#35.Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

'''
#36.Make the following using string formatting methods:
a = 8
b = 6

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}') #.2f for two decimals
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')





