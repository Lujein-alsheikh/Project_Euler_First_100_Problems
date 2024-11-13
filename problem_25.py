def has_thousand_digits(num):
    """tells us if a number has thousand digits"""
    if int(num/(pow(10,999))) in [1,2,3,4,5,6,7,8,9]:
        return True
    return False 

# Example: if a number has 3 digits, int(num/100) has to be between 1 and 9.

found = False 
L=[1,1]
while found == False:
    new_element=L[len(L)-1] + L[len(L)-2]
    L.append(new_element)
    if has_thousand_digits(new_element):
        found=True 
        #print(L)
        print(len(L))