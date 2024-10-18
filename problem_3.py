import math

def is_prime(num):
    """ returns a boolean which indicates whether a number is prime or not """
    if num in [2,3]:
         return True 
    if num % 2 == 0 or num % 3 ==0:  
            return False
    # it is enough to check up untill the square root. 
    for i in range(3,int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
    return True  
          
    
def primes_smaller_than_num(num):
    """ returns a list with all prime numbers smaller than the input argument """
    L=[]
    for i in range(2,num):
        if is_prime(i):
            L.append(i)
    return L        

print(primes_smaller_than_num(140))

def factors(num):
    """ finds the prime factors of num """
    factors_list =[]
    primes = primes_smaller_than_num(num)
    while num >1:
        for prime in primes:
            if num % prime == 0:
                factors_list.append(prime)
                num = num/prime 
                break 
    return factors_list

print(factors(140))
num = 600851475143
# print(max(factors(num)))

""" Best to explain with an example:
To find the prime factors of 140:
list_of_primes_smaller_than_140 = [2,3,5,7,11,13,17,...]
140/2 = 70
70/2 = 35
35/5 = 7 (2 and 3 don't divide 35)
7/7 = 1 (2,3, and 5 don't divide 35)
So the list that my 'factors' functions returns is [2,2,5,7]
Similarly, 13195=5x7x13x29
"""
        