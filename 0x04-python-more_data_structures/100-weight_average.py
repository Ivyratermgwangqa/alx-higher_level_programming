#!/usr/bin/python3
def weight_average(input_list=[]):
    if len(input_list) == 0:
        return 0

    weighted_sum = 0
    total_weight = 0
    for item in input_list:
        weighted_sum += (item[0] * item[1])
        total_weight += (item[1])
    return (weighted_sum / total_weight)
