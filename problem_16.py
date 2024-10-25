
print(2**1000)
# the trick is to convert 2**1000 to a string and then convert each character to an int separately.
string = str(2**1000)

digits = [int(x) for x in string]

print(sum(digits))