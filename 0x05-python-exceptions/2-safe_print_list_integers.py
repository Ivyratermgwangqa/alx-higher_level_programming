#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_integers = 0
    
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_integers = num_integers + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num_integers)
