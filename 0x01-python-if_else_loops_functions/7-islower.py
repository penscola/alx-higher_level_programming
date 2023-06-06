#!/usr/bin/python3

def islower(c):
    """ checks for lower case character
    returns true if lowercase else false.
    Args:
        c (str): letter
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
