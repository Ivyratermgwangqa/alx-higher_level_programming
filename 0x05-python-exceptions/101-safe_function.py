#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except:
        error_msg = "Exception: {}".format(sys.exc_info()[1])
        print(error_msg, file=sys.stderr)
    return None
