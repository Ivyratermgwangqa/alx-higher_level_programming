#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            res_div = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            res_div = 0
        except ZeroDivisionError:
            print("division by 0")
            res_div = 0
        except IndexError:
            print("out of range")
            res_div = 0
        finally:
            new_list.append(res_div)
    return (new_list)
