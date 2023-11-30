#!/usr/bin/python3
# add_0.py
def add(a, b):
    return a + b
# main_program.py
a = 1
b = 2

from add_0 import add

result = add(a, b)

print("{} + {} = {}".format(a, b, result))

