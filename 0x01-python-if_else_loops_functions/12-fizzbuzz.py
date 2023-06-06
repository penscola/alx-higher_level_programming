#!/usr/bin/python3
def fizzbuzz():
    """ for multiples of 3 prints fizz
    for multiples of 5 prints buzz
    for multiples of 3 and 5 prints FizzBuzz
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
