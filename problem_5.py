def divisible_by_all(num):
    divisors = [i for i in range(2,21)]
    # if a number is divisible by 20, then it is divisible by each of 2,4,5, and 10.
    divisors = [item for item in divisors  if item not in [2,4, 5,10]]
    for divisor in divisors:
        if num % divisor !=0:
            return False
    return True     

# the to-be-found number has to be divisible by 20 => it has to have a 0 end digit.
candidate=100
condition = False
while condition == False:
    candidate = candidate + 10
    if divisible_by_all(candidate):
        condition == True
        print(candidate)