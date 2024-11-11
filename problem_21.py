import math
import numpy as np
import pandas as pd

def sum_divisors(n):
    L=[] # list of proper divisors
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            L.append(i)
            if i != math.sqrt(n):
                L.append(int(n/i))
    L.append(1)        
    #print(n, L, sum(L))
    #print("\n")        
    return sum(L)    

l1 = [i for i in range(2,10000+1)]
l2= [sum_divisors(i) for i in range(2,10000+1)]

arr = np.column_stack((l1, l2))

# remove prime numbers since d(a prime number)=1 and d(1)=0.
# using boolean indexing
arr = arr[arr[:, 1] != 1]  
"""
df = pd.DataFrame(arr)
df.rename(columns={0: "num", 1: "sum_of_divisors"}, inplace=True)
print(df)
df.to_csv("problem_21.csv", index=False)
"""


amicable_nums=[]

# take two numbers a and b (a!=b) at a time and check if the amicable numbers condition applies or not.
for i in range(0,arr.shape[0]-1): # i goes till second to last element
    a = arr[i][0]
    d_a = arr[i][1]
    for j in range(i+1,arr.shape[0]): # j always goes till the last element
        b=arr[j][0]
        d_b = arr[j][1]
        if a != b:
            if a == d_b and b == d_a:
                amicable_nums.append((a,b))

print(amicable_nums)

total_sum = sum(num for tup in amicable_nums for num in tup)
print(total_sum)