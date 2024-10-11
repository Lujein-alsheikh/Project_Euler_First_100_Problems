# We generate the numbers in the Fibonacci sequence and we stop when the next value generated
# > 4000000 (we don't include it). We store the values in a list then we simply check for
# even numbers.
L = [1,2]
next_value = 3 
while next_value <= 4000000:
    L.append(next_value)
    next_value = L[len(L)-1] + L[len(L)-2]

print(L)
sum=0
for num in L:
    if num %2 == 0:
        sum = sum+num
print(sum)      
 