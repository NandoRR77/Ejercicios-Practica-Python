#Exercises: Level 2

#1. Unpack siblings and parents from family_members
family_members = ('Ana', 'Camila', 'Adriana', 'Cesar', 'Jaiver', 'Frank', 'Piedad', 'Mario')
sibligns = family_members[:6]
parents = family_members[6:]

print(sibligns)
print(parents)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana', 'Apple', 'Mango', 'Orange')
vegetables = ('Potato' , 'Onion', 'Lettuce' , 'Carrot')
animals = ('Chicken' , 'Pork' , 'Cow' , 'Fish')
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice = food_stuff_lt[:int((len(food_stuff_lt)/2))]
print(slice)

#5. Slice out the first three items and the last three items from food_staff_lt list
slice2 = food_stuff_lt[:3]
slice3 = food_stuff_lt[-3:]
print(slice2)
print(slice3)

#6. Delete the food_staff_tp tuple completely
try:
    del food_stuff_tp
    print(food_stuff_tp)
except:
    print('The element is not defined because it was eliminated')

    
#7. Check if an item exists in tuple:
    #Check if 'Estonia' is a nordic country
    #Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)






