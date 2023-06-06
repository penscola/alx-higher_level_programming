#!/usr/bin/python3

def print_last_digit(number):
    for number in range(0, 99):
        print("{} = {}".format(number, hex(number)))


print_last_digit(15)
