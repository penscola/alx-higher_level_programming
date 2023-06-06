#!/usr/bin/python3


def remove_char_at(str, n):
    """Creates a copy of the string removing the character at n position
    Args:
        str (string)
        n (integer)
    Returns:
        sliced string
    """
    if n < 0:
        return str
    return (str[0:n] + str[n + 1:])
