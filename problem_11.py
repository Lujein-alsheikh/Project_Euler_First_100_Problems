import numpy as np
import math 

string= """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

# we replace the newline characters. Otherwise, in case we convert the string characters to integers, the newlines will give an error.
string = string.replace('\n', ' ')
elements = list(map(int, string.split()))
array = np.array(elements).reshape(20,20)

def slice_product(a_list):
    """ a_list: a list of 4 elements which we call a 'slice'
        this function calculate the product of the slice """
    product=1
    for i in range(0,len(a_list)):
        product = product* a_list[i]
    return product
    
def maximum_up_down(array):
    max_product = 0
    # for each column
    for j in range(0,20):
        # we stop when i == 16. when i>16, the length of the slice is smaller than 4.
        for i in range(0,17):
            slice = array[i:i+4, j].tolist()
            product = slice_product(slice)
            if product > max_product:
                max_product = product
    return max_product     

def maximum_left_right(array):
    max_product = 0
    # for each row
    for i in range(0,20):
        for j in range(0,17):
            slice = array[i, j:j+4]
            product = slice_product(slice)
            if product > max_product:
                max_product = product
    return max_product

def max_diagonal_product(diag_list, initial_max_product):
    """ diag_list is a list with elements from one diagonal 
        returns the biggest product of consecutive 4 elements bigger than the initial_max_product """
    max_product = initial_max_product
    if len(diag_list) ==4:
            product = math.prod(diag_list)
            if product > max_product:
                max_product = product 
    elif len(diag_list) >4:
            for k in range(0, len(diag_list) -4+1):
                product = math.prod(diag_list[k:k+4])
                if product > max_product:
                    max_product = product 
    return max_product  # note that if the diagonal has strictly less than 4 elements, then we return the initial_max_product.               

def maximum_diagonal(array):
    max_product = 0
    # there are 2(n-1)+1 diagonals. 
    # for each diagonal in the upper triangle including the main diagonal.
    for sum_of_indices in range(0,20): 
        # first we get the diagonal elements.
        diag_elements =[] # we store the elements of the diagonal in a list
        for i in range(0, sum_of_indices+1):
            j = sum_of_indices - i # i+j = sum_of_indices
            diag_elements.append(array[i][j])
        # now we scan the diagonal elements to find the slice with the biggest product bigger than the current max_product.    
        diag_max_product = max_diagonal_product(diag_elements, max_product)
        if diag_max_product > max_product:
            max_product = diag_max_product
    # for each diagonal in the lower triangle (excluding the main diagonal since it was included before).
    for sum_of_indices in range(20, 2*19 +1):
        diag_elements = []
        # for a fixed sum_of_indices, i belongs to [sum_of_indices - (n-1), n-1]
        for i in range(sum_of_indices - (20-1) , 20):
            j = sum_of_indices - i # the relation i+j = sum_of_indices still holds.
            diag_elements.append(array[i][j])
        diag_max_product = max_diagonal_product(diag_elements, max_product)
        if diag_max_product > max_product:
            max_product = diag_max_product

    return max_product                

# this function is not necessary.
def reversed_diag_4_elements(array):
    """ this function return the maximum of the product of the reversed diagonals that have exactly 4 elements """
    i=0
    L2=[]
    for j in range(16,20):
        L2.append(array[i][j])
        i += 1
    product_upper_diag = slice_product(L2)  # this should be the product of 50, 56, 36, 91

    j=0
    L1=[]
    for i in range(16,20):
        L1.append(array[i][j])
        j += 1
    product_lower_diag = slice_product(L1) # this should be the product of 4, 69, 35, 71

    return max(product_upper_diag, product_lower_diag)
 

def maximum_reversed_diagnoal(array):
    max_product = 0
    # we go through the diagonals in the lower triangle of the grid. We stop at i == 16 because it is the last diagonal that has
    # at least 4 elements.
    for i in range(0,17):
       diag_elements = []
       temp_i = i
       j=0
       # Each diagonal that includes the elements array[i][0] has n-i elements. Here n=20.
       num_elements = 20 - i
       for counter in range(1, num_elements+1):
           diag_elements.append(array[temp_i][j])
           i += 1
           j+= 1 
       diag_max_product = max_diagonal_product(diag_elements, max_product)
       if diag_max_product > max_product:
            max_product = diag_max_product   

    # now we go through the diagonals in the upper triangle. 
    for j in range(1,20):
        diag_elements=[]
        temp_j=j
        i=0
        num_elements=20-j # Each diagonal that includes the element [0][j] has n-j elements.
        for counter in range(1,num_elements+1):
            diag_elements.append(array[i][temp_j])
            i +=1
            temp_j += 1
        diag_max_product = max_diagonal_product(diag_elements, max_product)
        if diag_max_product > max_product:
            max_product = diag_max_product              
    return max_product



print(maximum_up_down(array))   
print(maximum_left_right(array))   
print(maximum_diagonal(array))
print(maximum_reversed_diagnoal(array))

            