def str_reversal(str):
    if(len(str)) == 0:
        return str
    else:
        return str_reversal(str[1:]) + str[0]
    
str = "nando"
str_reversed = str_reversal(str)

print(str)
print(str_reversed)
 