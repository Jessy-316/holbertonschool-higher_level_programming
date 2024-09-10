#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for numbers in my_list:
        if numbers > max_value:
            max_value = numbers
    return max_value
