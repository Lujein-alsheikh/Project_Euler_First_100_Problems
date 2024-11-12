# Solution 1: primitive solution using loops

L = [0,1,2,3,4,5,6,7,8,9]

def remove_elements(original_list, elements_to_remove):
    return [item for item in original_list if item not in elements_to_remove]

counter = 0 
found = False 

for i1 in L:
    for i2 in remove_elements(L,[i1]):
        for i3 in remove_elements(L,[i1,i2]):
            for i4 in remove_elements(L,[i1,i2,i3]):
                for i5 in remove_elements(L,[i1,i2,i3,i4]):
                    for i6 in remove_elements(L,[i1,i2,i3,i4,i5]):
                        for i7 in remove_elements(L,[i1,i2,i3,i4,i5,i6]):
                            for i8 in remove_elements(L,[i1,i2,i3,i4,i5,i6,i7]):
                                for i9 in remove_elements(L,[i1,i2,i3,i4,i5,i6,i7,i8]):
                                     i10 = remove_elements(L,[i1,i2,i3,i4,i5,i6,i7,i8,i9])[0]   
                                     perm = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
                                     counter += 1
                                     if counter == 1000000:
                                            print(perm)
                                            found = True 
                                            break                                    
                                if found:
                                    break 
                            if found:
                                break 
                        if found:
                            break 
                    if found:
                        break 
                if found:
                    break 
            if found:
                break  
        if found:
            break 
    if found:
        break                                   
                                        
# Solution 2: using the itertools library
from itertools import islice, permutations

L = [0,1,2,3,4,5,6,7,8,9]
target_permutation_index = 1000000 - 1  # permutations are counted starting from 0

millionth_permutation = next(islice(permutations(L), target_permutation_index, target_permutation_index + 1))
print(millionth_permutation)

# Solution 3: Best solution
import math

def get_nth_permutation(elements, n):
    permutation = [] 
    elements = elements[:] # Make a copy of the elements to manipulate
    n -= 1 # Adjust n to be zero-indexed
    
    for i in range(len(elements) - 1, -1, -1): # i =9,8,7,6,5,4,3,2,1,0
        fact = math.factorial(i)
        print(f"i is {i} and factorial is {fact}")
        index = n // fact # floor division
        n %= fact # remainder of division or number of permutations we still need to calculate.      
        print(f"index is {index} and n is {n}")
        permutation.append(elements.pop(index))
        print(f"permutation is {permutation}")
    
    return permutation

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_nth_permutation(L,1000000))

'''
When i=9: we decide on the first digit. We have 9 options. For each option there are 9! = 362880 permutations. Since we
are searching for the permutation number 99999, we calculate 99999/362880= 2.something. So the digit is 2 (which is L[2]).
We still need to search for 99999%362880 permutations so we update n.
'''