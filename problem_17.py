words_dict = {
    1: "one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",
    9: "nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
    16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
    20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 
    70:"seventy", 80:"eighty", 90:"ninety", 1000:"onethousand"
}

def has_one_digit(num):
    if int(num/10) == 0:
        return True
    else:
        return False

def has_two_digits(num):
    if len(str(num))==2:
        return True
    else:
        return False

def has_three_digits(num):
    if len(str(num)) ==3:
        return True
    else:
        return False


def number_word(num):
    two_digits_under_20 = [11,12,13,14,15,16,17,18,19]
    if has_one_digit(num):
        return words_dict[num]
    
    elif has_two_digits(num):
        if num in two_digits_under_20:
            return words_dict[num]
        else:
            first_digit = int(str(num)[0])
            second_digit = int(str(num)[1])
            word_1 = words_dict[first_digit*10]
            if second_digit == 0:
                word_2 = ""
            else:    
                word_2 = words_dict[second_digit]
            return word_1+word_2
    
    elif has_three_digits(num):
        first_digit = int(str(num)[0])
        second_digit = int(str(num)[1])
        third_digit = int(str(num)[2])
        word_1 = words_dict[first_digit]
        if second_digit*10 + third_digit in two_digits_under_20:
            word = words_dict[second_digit*10 + third_digit]
            return word_1+"hundred"+"and"+word 
        else:
            if second_digit == 0:
                word_2 = ""
            else:    
                word_2 = words_dict[second_digit*10]
            if third_digit == 0:
                word_3 =""
            else:        
                word_3 = words_dict[third_digit]
            if word_2 == "" and word_3 == "":
                return word_1 + "hundred"    
            else:
                return word_1 + "hundred" + "and" + word_2 + word_3
    elif num == 1000:
        return words_dict[1000]


total = 0
for num in range(1,1001):
    total = total + len(number_word(num))
print(total)   

"""
for num in range(900,1001):
    print(num, number_word(num))
"""   