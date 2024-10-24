import math

ans = math.factorial(40)/(math.factorial(20) * math.factorial(20))
print(ans)

# In order to get from the top left corner to the bottom right one, we have to make 40 moves
# in total (k=40). 20 moves to the right (k1=20) and other 20 moves down (k2=20). 
# The order doesn't matter.
# There are k!/(k1! k2!) ways to arrange a route. 