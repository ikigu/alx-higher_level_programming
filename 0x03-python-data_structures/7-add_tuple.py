#!/usr/bin/python3

def add_tuple(tuple_a: list = (), tuple_b: list = ()):
    list1 = list(tuple_a)
    list2 = list(tuple_b)

    matrix = [list1, list2]

    for _list in matrix:
        for _ in range(2):
            if len(_list) >= 2:
                pass
            else:
                _list.append(0)

    x = list1[0] + list2[0]
    y = list1[1] + list2[1]

    return (x, y)
