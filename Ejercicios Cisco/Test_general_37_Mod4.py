numbers = [i*1 for i in range(5)]

foo = list(filter(lambda x: x % 2, numbers))

print(foo)
