import math

def is_prime(num):
    """ returns a boolean which indicates whether a number is prime or not """
    if num<0:
         num= -1*num
    if num in [2,3]:
         return True 
    if num % 2 == 0 or num % 3 ==0:  
            return False
    # it is enough to check up until the square root. 
    for i in range(3,int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
    return True  

# we know that n^2+an+b has to be prime for n=0 and we know that b is between -1000 and +1000
# so in order to optimize the search we only consider b values that are prime numbers and < |1000|
def b_prime_values():
    L=[]
    for num in range(2,1000):
        if is_prime(num):
            L.append(num)
    L = L + [-x for x in L]
    return L

max_prev_counter=0
ans_a=0
ans_b=0

for b in b_prime_values():
      for a in range(-1000,1000):
            n=0
            counter = 0
            while is_prime(n**2 + a*n + b):
                n+=1
                counter+=1
            if n > max_prev_counter:
                max_prev_counter = n
                ans_a = a
                ans_b = b

print(ans_a,ans_b,ans_a*ans_b) # -61 971 -59231            