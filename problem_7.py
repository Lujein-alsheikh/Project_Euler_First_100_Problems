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

def func():
    prime_numbers_counter = 0 
    num =2
    while True:
        if is_prime(num):
                prime_numbers_counter +=1 
        if prime_numbers_counter == 10001:
              return num         
        num +=1      

print(func())  
      