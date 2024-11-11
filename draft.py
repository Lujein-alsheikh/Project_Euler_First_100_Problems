values_dict = {chr(65 + i): i + 1 for i in range(26)}

def calculate_name_value(name):
    """calculates the alphabetical value for an input name"""
    return sum(values_dict.get(char, 0) for char in name)

print(calculate_name_value("Lulu"))