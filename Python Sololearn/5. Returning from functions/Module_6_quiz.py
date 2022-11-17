#What's the highest number output by this code?
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)


#What's the output of this code?
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res
print(func(3))