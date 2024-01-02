#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
number_copy = number

if number < 0:
    number_copy = number * -1

last_digit = number_copy % 10

if number < 0:
    last_digit *= -1

prefix = "Last digit of"

if last_digit > 5:
    suffix = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    suffix = "and is less than 6 and not 0"
elif last_digit == 0:
    suffix = "and is 0"

print(f"{prefix} {number:d} is {last_digit:d} {suffix}")
