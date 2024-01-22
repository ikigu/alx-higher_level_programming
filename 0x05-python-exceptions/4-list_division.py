#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result_list = []

    while list_length > i:
        result = 0

        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
        finally:
            result_list.append(result)

        i = i + 1

    return result_list
