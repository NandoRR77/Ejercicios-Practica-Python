'''
Level 3

1. Convert the ages to a set and compare the length of the list and the set, 
which one is bigger?
2. Explain the difference between the following data types: string, list, tuple and set
3. I am a teacher and I love to inspire and teach people. 
How many unique words have been used in the sentence? 
Use the split methods and set to get the unique words.


# set
age = [22, 19, 24, 25, 26, 24, 25, 24]

'''
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print('# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger\n')

converted_age = set(age)
len_age = len(age)
len_converted_age = len(converted_age)

print(f'List age = {age}')
print(f'Set converted age = {converted_age}')
print(f'The list age contains {len_age} elements')
print(f'The set converted_age contains {len_converted_age} elements')

print('\n****************************************************\n')


#2. Explain the difference between the following data types: string, list, tuple and set

print('# 2. Explain the difference between the following data types: string, list, tuple and set')

print('''String: Ordenada, inmutable, admite duplicados.
         List: Ordenada, mutable, admite duplicados.
         Tuple: Ordenada, inmutable, admite duplicados.
         Set: No ordenada, mutable, no admite duplicados.
         ''')

print('\n****************************************************\n')


#3. How many unique words have been used in the sentence?

print('# 3. How many unique words have been used in the sentence >= ')
print('I am a teacher and I love to inspire and teach people.')

sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_split = list(sentence.split(' '))

print(sentence_split)

print(f'''Converting list sentence_split 
      {sentence_split} in a set...\n''')

set_sentence = set(sentence_split)
len_set_sentence = len(set_sentence)

print(f'Set sentence_split {set_sentence} \n')
print(f'''The sentence >= "I am a teacher and I love to inspire and teach people"
             has {len_set_sentence} unique words''')


print('\n****************************************************\n')