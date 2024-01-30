#!/usr/bin/python3

"""indents text"""


def text_indentation(text):
    """prints text with 2 lines after various punctuation marks"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['?', '.', ':']
    prev = ""

    for i in range(len(text)):
        if prev in punctuation and text[i] == " ":
            prev = " "
            continue

        print(text[i], end="")
        prev = text[i]

        if text[i] in punctuation:
            print('\n')
