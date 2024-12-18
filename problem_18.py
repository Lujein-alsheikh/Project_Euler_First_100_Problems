triangle = [[3],[7,4],[2,4,6],[8,5,9,3]]

input_string = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
lines = input_string.strip().splitlines()
num_lines = len(lines)
# I store the triangle as a list of lists. Each list corresponds to one line from the string.
triangle = [list(map(int, line.split())) for line in lines]

# print(triangle)

L = [[0]]
for i in range(0,num_lines-1):
    new_L=[]
    for l in L:
        last_element = l[len(l)-1]
        i1 = last_element
        i2= i1+1
        l1 = l+[i1]
        l2 = l+[i2]
        new_L.append(l1)
        new_L.append(l2)
    L = new_L    

all_paths = L           

max_path=[]
max_sum = 0
for path in all_paths:
    sum =0
    for i in range(0,num_lines):
        sum = sum + triangle[i][path[i]]
    if sum > max_sum:
        max_path = path
        max_sum = sum

print(max_sum, max_path)            
