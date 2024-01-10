#!/usr/bin/python3

def roman_to_int(roman_string: str) -> int:
    if not roman_string or type(roman_string) != str:
        return 0

    roman_to_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    previous = 0
    integized_number = 0

    for letter in reversed(roman_string):
        current = roman_to_int_dict[letter]

        if previous > current:
            integized_number -= current
        else:
            integized_number += current

        previous = current

    return integized_number
