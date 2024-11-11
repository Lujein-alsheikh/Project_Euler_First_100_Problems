# first create a dict that tells us how many days there are each year.
# if a year has 365 days => not leap
# if a year has 366 days => leap
num_days = {}
# initialize num_days
for year in range(1901, 2001):
    num_days[year] = None

for year in range(1901,2001):
    # since there is only one century year (2000) and we already know it is a leap year, no
    # need to add the condition that if a year is a century, it has to divide 400.
    # 2000 is the only year and we know it does.
    if year % 4 == 0:
        num_days[year] = 366
    else:
        num_days[year]= 365

# When going through the years, I change the value of february on the go.
month_num_days = {"jan":31, "feb": 0,"march":31, "april":30, "may": 31, "june":30, "july":31,
                 "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}    
      
# this list will be updated each time we go through a month of the year. 
# here I initialize it with the day on which 1/jan/1901 falls which is wednesday.
# example, if a month starts on a sat, L will be updated like: sat, sun, mon, tues, ...
# I know that the first day of the year 1901 falls on a wed, because 1901 = 7x52+2.
# I used two pieces of info: 1900 starts on a monday and that it is not a leap year (because it is not divisible by 400).
L = [ "tues", "wed", "thurs", "fri", "sat", "sun", "mon"]

months = ["jan", "feb","march", "april", "may", "june", "july","aug", "sep", "oct", "nov", 
          "dec"]

def reorder_func(start_day: str, L:list):

    start_index = L.index(start_day)
    # Create reordered list by slicing from the start_index
    reordered_list = L[start_index:] + L[:start_index]
    return reordered_list


# counter for the values of sundays that are first of a month
counter = 0

for year in range(1901,2001):
    # this dict will save the first day of the week for each month
    year_dict = {}
    for month in months:
        year_dict[month] = ""
    # add the correct value for the number of days in feb to the list month_num_days    
    if num_days[year] == 365:
        month_num_days["feb"] = 28
    else:
        month_num_days["feb"] = 29

    for month_index in range(0, 12):
        first_day=""
        if months[month_index] == "jan":
            first_day = L[0]
        else:    
            prev_month = months[month_index-1]
            first_day = L[month_num_days[prev_month] % 7]
            L = reorder_func(first_day,L)
        year_dict[months[month_index]] = first_day    
        if first_day == "sun":
            counter +=1
    # now we prepare L for the next year. Dec has 31 days = 7x4 + 3
    L = reorder_func(L[3], L)

    if year in [1901,1902,1903]:
        print(year, year_dict)
    #print("\n")    

print(f"counter{counter}")        



