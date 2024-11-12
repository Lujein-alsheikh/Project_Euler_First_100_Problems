import math

def get_nth_permutation(elements, n):
    permutation = [] 
    elements = elements[:] # Make a copy of the elements to manipulate
    n -= 1 # Adjust n to be zero-indexed
    
    for i in range(len(elements) - 1, -1, -1): # i =9,8,7,6,5,4,3,2,1
        fact = math.factorial(i)
        print(f"i is {i} and factorial is {fact}")
        index = n // fact # floor division
        n %= fact # remainder of division       
        print(f"index is {index} and n is {n}")
        permutation.append(elements.pop(index))
        print(f"permutation is {permutation}")
    
    return permutation

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_nth_permutation(L,1000000))

