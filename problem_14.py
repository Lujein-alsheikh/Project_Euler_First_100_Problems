import math 

def function(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1 
    
def chain_length(starting_num):
    """ returns the chain length of a given starting number """
    num = starting_num
    stop = False
    counter = 1
    #L = []
    while stop == False:
        result = function(num)
        #L.append(result)
        counter += 1 
        if result == 1: # we stop when the chain reaches 1
            stop = True 
            #print(L)
            return counter
        else:
            num = result 

# initial values for the loop
starting_num = 3 # we can skip 1 and 2
longest_chain_len = 0 

while starting_num < 1000000:
    length = chain_length(starting_num)
    if length > longest_chain_len:
        longest_chain_len = length 
        special_starting_num = starting_num # the requested starting number
    starting_num += 1    

print(longest_chain_len, special_starting_num)