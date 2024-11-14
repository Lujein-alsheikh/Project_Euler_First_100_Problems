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

primes_smaller_than_1000 = primes_smaller_than_num(1000)

def has_recurring_cycle(d):
    # 1/d has a recurring cycle if num has prime factors other than 2 and 5.
    if is_prime(d): 
          if d ==2 or d==5:
                return False
          else:
              return True 
    else:
          primes_smaller_than_d = [num for num in primes_smaller_than_1000 if num < d]
          for prime in primes_smaller_than_d:
                if prime != 2 and prime != 5 and d% prime ==0:
                      return True 
          return False               
          
def coprime_to_10(num):
      # coprime means that 2 is not a factor and 5 is not a factor
      if num%2 !=0 and num%5 != 0:
            return True 
      else:
            return False 

#def recurring_digits_length_inner_function(num):
      

def recurring_digits_length(d):
    if coprime_to_10(d):
        for i in range(1,1000000): 
             # let the upper limit of i be a huge number we know we are not gonna reach
             if pow(10,i)%d == 1:
                  return i 
        # take as example 1/7
        # 1000000/7 = 142857.142857.... = 142857 + 1/7 . This is the point we are looking for
        # <=> 1000000 = 142857 x 7 + 1 <=> 1000000 % 7 is 1 <=> 1000000 ≡ 1 mod 7

    else: # if d has 2 or 5 as a prime factor
            return 0
            # there is no need to calculate any thing here, because the length of the cycle
            # is the same as the same for d/(the 2 and/or 5 factors) which is calculated above.
            # take examples:
            # d=2x5x2x3x3 => 1/d = (1/10) x (1/2) x(1/9) = 0.00555555
            # here each of 1/10 and 1/2 contribute to a fixed digit after the decimal point.
            # Take as examples d = 2x5x5x3x3, d=2x5x2x2x3x3, d=2x5x5x5x3x3, d=2x5x2x5x3x3 
"""
for num in range(1,50):
   print(f"1/{num} = {1/num} {has_recurring_cycle(num)}")  
"""              

max_len = 0
the_number = 0

for d in range(2,1000):
      current_len = recurring_digits_length(d)
      if  current_len > max_len:
            max_len = current_len 
            the_number = d 
print(f"the number is {the_number} and the length is {max_len}")
print(f" 1/ the number = {1/the_number}")

"""
1/7 = 0.(142857)
10 = 1x7 + 3 <=> 10/7=1.42857142857 <=> 10^1 ≡ 3 mod 7
100 = 14x7 + 2 <=> 100/7 = 14.2857142857 <=> 10^1 ≡ 2 mod 7
1000 = 142x7 + 6 <=> 1000/7 = 142.857142857 <=> 10^3 ≡ 6 mod 7
10000 = 1428 x7 +4 <=> 10000/7 = 1428.57142857 <=> 10^4 ≡ 4 mod 7
100000 = 14285 x 7 + 5 <=> 100000/7 = 14285.7142857 <=> 10^5 ≡ 5 mod 7
1000000 = 142857 x7 +1 <=> 1000000/7 = 142857.142857 <=> 10^6 ≡ 1 mod 7

The length of the cycle is m where 10^m ≡ 1 mod n
The group is Z*_{n}
We have: 10^m ≡ 1 mod n (1)
         10 ≡ s mod n (2) => 10^m ≡ s^m mod n (3)
         From (1) and (3), s^m ≡ 1 mod n
         so m is the order of s!
"""