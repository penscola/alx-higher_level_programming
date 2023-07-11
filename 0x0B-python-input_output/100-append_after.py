#!/usr/bin/python3
"""Module contains append_after """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each
    line containing a specific string"""
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
