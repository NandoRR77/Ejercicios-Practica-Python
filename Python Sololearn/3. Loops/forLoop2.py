nums = [1, 2, 3, 4]
res = 0
for x in nums:
    if(x%2==0):
        continue
    else:
        res += x
        
print(res)
