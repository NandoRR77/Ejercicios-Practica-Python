#ejemplo for loops

nums = [4,7,3,1]
for x in nums:
    print(x*2)


#ejemplo 2 - contador de caracteres con loop for
print("ejemplo for con contador")
str = "testing for loops"
count = 0
for x in str:
  if(x == 't'):
    count += 1
    print("encontramos una " , x)
print("Contador de caracteres",count)

#ejemplo 3 - cuando encuentre el primer elemento, romper con break
print("ejemplo for con break")
text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)