#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    result = None

    try:
        result = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
    finally:
        return result
