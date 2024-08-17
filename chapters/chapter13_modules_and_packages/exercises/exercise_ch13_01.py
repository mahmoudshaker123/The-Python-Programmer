## Exercise 13_01 - Module
# Given these working Python functions, we want to create a module called string_tools.py
# that contains these functions. The module should be placed in a package called tools.
# The package should be placed in the same directory as the main program.


def to_uppercase(s):
    return s.upper()


def to_lowercase(s):
    return s.lower()


def to_titlecase(s):
    return s.title()


def is_palindrome(s):
    return s == s[::-1]
