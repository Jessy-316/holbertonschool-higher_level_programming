#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    unique = set()

    for numbers in my_list:
        if numbers in seen:
            unique.discard(numbers)
        else:
            seen.add(numbers)
            unique.add(numbers)

    return sum(unique)
