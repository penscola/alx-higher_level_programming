#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    tuple_a = tuple_a + tuple_c
    tuple_b = tuple_b + tuple_c
    tuple_d = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_d
