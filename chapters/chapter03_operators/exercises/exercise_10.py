# Exercise 10 - Bitwise Operations
#  Write a program that takes two numbers as input and performs
# bitwise AND, OR, and XOR operations and returns the results in a single string with a space between.
# For example, given the numbers 5 and 3, the function should return "1 7 6".


def bitwise_operations(num1, num2):
    # Your code should go here.
    bitwise_and = num1 & num2
    bitwise_or = num1 | num2
    bitwise_xor = num1 ^ num2
    return f"{bitwise_and} {bitwise_or} {bitwise_xor}"
    