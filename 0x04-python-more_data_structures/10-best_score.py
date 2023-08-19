#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        b_score = None
    else:
        b_score = max(a_dictionary, key=a_dictionary.get)
        return b_score
