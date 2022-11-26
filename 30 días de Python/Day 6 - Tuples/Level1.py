#Exercises: Level 1
#1. Create an empty tuple
tupla = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Ana','Camila','Adriana')
brothers = ('Cesar','Jaiver','Frank')

#3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

#4. How many siblings do you have?
print(f'I have {len(siblings)} siblings')

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
#changing tuple to list
siblings = list(siblings)

#adding elementos to list
siblings.append('Piedad')
siblings.append('Mario')

#changing list to tuple
siblings = tuple(siblings)

#assing tuple to new tuple
family_members = siblings

print(family_members)


