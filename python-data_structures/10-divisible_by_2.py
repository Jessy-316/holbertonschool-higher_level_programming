#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = [numbers % 2 == 0 for numbers in my_list]
    return list_result
