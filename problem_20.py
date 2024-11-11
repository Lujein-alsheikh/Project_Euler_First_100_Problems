def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
    
num = fact(100)    
print(num)  
num_str = str(num)
print(num_str)

res = 0
for char in num_str:
    res += int(char)
print(res)    