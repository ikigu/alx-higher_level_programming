#!/usr/bin/python3

for i in range(0, 100):
    if i < 99:
        print("{number:02d}".format(number=i), end=", ")
    else:
        print("{number:d}".format(number=i))
