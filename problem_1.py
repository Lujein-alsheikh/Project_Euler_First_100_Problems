# We go through the numbers [3,1000] and we check if each number is a multiple of 3 or 5.
# If it is we add it to the required sum.
sum=0
for num in range(3, 1000):

    if num % 3 == 0 or num % 5 == 0:
        sum=sum+num

print(sum)
