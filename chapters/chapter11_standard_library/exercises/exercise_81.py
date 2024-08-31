# Exercise 81 - Functools
# Write a function that uses `functools.partial` to create a function that always multiplies by 10.
from functools import partial


def multiply(x, y):
    return x * y


def multiply(): ...


multiply_by_10 = ...
