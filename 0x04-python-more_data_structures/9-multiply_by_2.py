#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key = a_dictionary.copy()
    for i, j in key.items():
        key[i] = j * 2
    return key
