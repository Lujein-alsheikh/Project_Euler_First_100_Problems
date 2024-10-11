def is_palindromic(num):
    """ checks if a num is palindromic """
    string = str(num)
    #assert len(string) in [5,6], "argument should be 5 or 6 digits only!"
    # this assertion is applied in the problem only, because possible outcomes in our problem
    # will have either 5 or 6 digits.
    l = len(string)
 
    for i in range(0,int(l/2)):
            if string[i] != string[l-1-i]:
                return False
    return True    


def fun():
    # We calculate all possible outcomes from multiplying two numbers each with 3 digits. 
    # Then we check each outcome if it is palindromic or not. 
    # Each time we compare with the previously obtained max.
    max_palindromic_num = 0
    for x in range(100,1000):
        for y in range(100,1000):
            res = x*y
            if is_palindromic(res):
                 if res > max_palindromic_num:
                      max_palindromic_num= res
    print(max_palindromic_num)

fun()    