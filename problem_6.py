
def sum_of_squares():
    """ this function calculates the sum of squares of the first 100 natural numbers """
    sum = 0
    for num in range(1,101):
        sum += num*num 
    return sum 

def square_of_sums():
    """ this function calculates the square of the sums of the first 100 natural numbers """
    sum =0
    for num in range(1,101):
        sum += num 
    return sum*sum 

print(sum_of_squares(), square_of_sums(), -sum_of_squares() + square_of_sums())        
