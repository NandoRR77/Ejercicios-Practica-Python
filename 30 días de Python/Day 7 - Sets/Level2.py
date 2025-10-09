'''
Level 2

1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
'''

#1. Join A and B
print('1. Join A and B')

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

print(f'\nA = {A} \nB = {B} \nA union B = C {C}')

print('****************************************************\n')

#2. Find A intersection B
print('2. Find A intersection B')

D = A.intersection(B)

print(f'\nA = {A} \nB = {B} \nA intersection B = D {D}')

print('****************************************************\n')


#3. Is A subset of B
print('3. Is A subset of B')

E = A.issubset(B)
print(f'Is A {A} subset of B {B}? \n{E}')

print('****************************************************\n')

#4. Are A and B disjoint sets
print('4. Are A and B disjoint sets')

F = A.isdisjoint(B)
print(f'Are A {A} and B {B} disjoint sets? \n{F}')

print('****************************************************\n')


#5. Join A with B and B with A
print('5. Join A with B and B with A')

G = A.union(B)
H = B.union(A)
I = G.union(H)

print(f'A union B and B union A\n{I}')

print('****************************************************\n')


#6. What is the symmetric difference between A and B
print('6. What is the symmetric difference between A and B')

J = A.symmetric_difference(B)

print(f'The symmetric difference between A and B = {J}')

print('****************************************************\n')


#7. Delete the sets completely
print('7. Delete the sets completely')

print(f'Original set A {A}')
print(f'Original set B {B}')
print(f'Original set C {C}')
print(f'Original set D {D}')
print(f'Original set E {E}')
print(f'Original set F {F}')
print(f'Original set G {G}')
print(f'Original set H {H}')
print(f'Original set I {I}')
print(f'Original set J {J}')

print('Deleting sets...')

del A, B, C, D, E, F, G, H, I, J

print('The sets have been deleted...')
print('****************************************************\n')

