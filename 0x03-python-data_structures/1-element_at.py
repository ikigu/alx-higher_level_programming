#!/usr/bin/python3

def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return None

    return my_list[idx]


my_list = [1, 2, 3, 4]
print("{:d}".format(element_at(my_list, 4)))
