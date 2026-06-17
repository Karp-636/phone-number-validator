import json 
import re

with open('states_area_codes.json', 'r') as file:
    foobar = json.load(file)

    print(foobar)

def input_validator(fn):
    def wrapper(phone_num):
        regex_pattern = r"(\(\d{3}\)\d{3}-\d{4})$"
        re.findall(regex_pattern, phone_num)
        if
            return fn(phone_num)
            print()
        else: 
            print("error")
    return wrapper




# @input_validator
def f_num(phone_num):
    regex_pattern = r"(\(\d{3}\)\d{3}-\d{4})$"
    my_string = "(303)933-4958)"
print("Correct output")
