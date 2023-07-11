#!/usr/bin/python3
"""Module for read_file method."""
def read_file(filename=""):

    """Method for read_file."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

if __name__ == "__main__":
    read_file("./tests/my_file_0.txt")
    print("")
    read_file("./tests/my_file_0.txt")
    print("")
    read_file("./tests/my_file_0.txt")
    print("")
