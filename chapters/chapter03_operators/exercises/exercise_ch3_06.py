# Exercise 03_06 - ISBN Verifier
# Write a program that checks if a given ISBN number is valid.
# The ISBN is valid if:
# - It consists of 10 digits.
# - The first 9 digits are numbers.
# - The last digit is a number or an uppercase X.
# - The ISBN is valid if the sum of the 10 digits multiplied by their position modulo 11 is 0.
# The program should return True if the ISBN is valid and False otherwise.
# formula: (d1*1 + d2*2 + d3*3 + d4*4 + d5*5 + d6*6 + d7*7 + d8*8 + d9*9 + d10*10) % 11 == 0


def is_valid_isbn(isbn):
    # Your code should go here.

    return ...
