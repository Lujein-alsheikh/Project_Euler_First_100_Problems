import math
def is_prime(num):
    """ returns a boolean which indicates whether a number is prime or not """
    assert num > 1, "num should be greater than 1"
    if num in [2,3]:
          return True
    
    if num % 2 == 0 or num % 3 ==0:  
            return False
        
    for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
    return True 

sum = 0 
for num in range(2,2000001):
       if is_prime(num):
              sum += num 
print(sum)              