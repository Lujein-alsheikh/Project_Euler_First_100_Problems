import csv
import pandas as pd

# first we define a dictionary with keys 'A', 'B', ... and values 1,2,...
values_dict = {chr(65 + i): i + 1 for i in range(26)}

def calculate_name_value(name):
    """calculates the alphabetical value for an input name"""
    return sum(values_dict.get(char, 0) for char in name)

# we prepare a .csv file with a column that has the names
# first we load the names after removing the quotations marks and splitting the names
with open('problem_22_names.txt', 'r') as txt_file:
    names = txt_file.read().replace('"', '').split(',')
# we create a .csv file and write the names into it one by one
with open('problem_22_names.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name"]) # call the column "Name"
    for name in names:
        writer.writerow([name])

# I add the na_filter = False, because one of the names is "NA" which was converted to NaN
# and treated as a missing value.
df = pd.read_csv("problem_22_names.csv", na_filter=False)
"""
non_string_values = df[~df['Name'].apply(lambda x: isinstance(x, str))]
print(non_string_values)
"""

# first step is sorting the names
df= df.sort_values(by='Name')
df = df.reset_index(drop=True)
df.to_csv("problem_22_names_sorted.csv", index=False)

# second step is to creating a column with the alphabetical values for each name.
df['Alphabetical_value'] = df['Name'].apply(calculate_name_value)
df["Alphabetical_positions"] = df.index + 1
df["Score"] = df["Alphabetical_value"] * df["Alphabetical_positions"]
print(df.head())
result = df["Score"].sum()
print(result)

