#!/usr/bin/python3

def multiple_returns(sentence: str):
    length = len(sentence)
    first_character = None

    if length != 0:
        first_character = sentence[0]

    return (length, first_character)
