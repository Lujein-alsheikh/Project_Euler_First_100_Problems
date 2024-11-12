import math

def is_abundant(num):
    """tells us if a num is abundant or not"""
    divisors=[]
    square_root = int(math.sqrt(num))
    #print(f"square root {square_root}")
    for i in range(2, square_root+1):
        if num%i ==0:
            divisors.append(i)
            if i != math.sqrt(num):
                divisors.append(int(num/i))
    divisors.append(1)            
    #print(f"divisors of {num} are {divisors}")            
    sum_of_divisors = sum(divisors)
    if sum_of_divisors>num:
        #print(f"{num} is abundant")
        return True
    else:
        #print(f"{num} is not abundant")
        return False 
    

def sum_of_two_abundant_numbers(num):
    """tells us if a num can be written as a sum of two abundant numbers"""
    # since we know that 24 is the smallest number that can be written as a sum of two 
    # abundant numbers, we don't need to check for smaller numbers. 
    assert num > 24, "number should be bigger than 24"

    for i in range(12, int(num/2)+1): 
            # we start counting from 12 since it is the smallest abundant number
            num_1 = i 
            num_2 = num-i 
            if is_abundant(num_1) and is_abundant(num_2):
                return True 
    return False 

initial_sum = 23*24 // 2  # using the formula for sum of numbers from 1 to n: n * (n + 1) // 2
print(initial_sum)

res = initial_sum + sum(x for x in range(25, 28123) if not sum_of_two_abundant_numbers(x))
print(res)






