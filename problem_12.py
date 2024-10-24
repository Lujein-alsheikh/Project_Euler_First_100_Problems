import math

def factors(num):
    """ returns the number of factors of the parameter num excluding 1 and the num itself """
    L = [] # the list of factors
    for i in range(2,math.ceil(math.sqrt(num))+1):
        if num % i ==0:
            L.append(i)
            L.append(int(num/i))
    # notice that for num=6, L = [2, 3, 3, 2]  
    # we keep only unique elements in L
    s = set(L)
    return len(s)        

prev_triangle_num = 1
counter = 2 
requested_num_found = False

# as long as we haven't found our target number, we keep creating triangle numbers and
# for each triangle number, we calculate the number of factors. If it exceeds 498, then the
# current triangle number is the requested triangle number. 
# When counting the number of factors, I exclude 1 and the number itself.

while requested_num_found == False:
    triangle_num = prev_triangle_num + counter 
    num_of_factors = factors(triangle_num)
    if num_of_factors>500-2:
        print(triangle_num)
        requested_num_found = True 
    prev_triangle_num = triangle_num
    counter += 1    