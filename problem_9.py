# We are searching for three numbers a,b,c that satisfy the conditions:
# a<b<c & a+b+c=1000 & a^2 + b^2 = c^2
# we go through all possible values for a and b. c has to be 1000-a-b. No need for it to have
# its own loop.

for a in range(1,1001):
    for b in range(1,1001):
            c = 1000 -a-b
            if a<b<c and a*a + b*b == c*c:
                print(f"a={a}. b={b}. c={c}")
                print(a*b*c)
                break