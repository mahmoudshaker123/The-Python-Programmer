## Exercise 09_02 - Calculator Class
# Given the following `Calculator` class, there is a bug in the class definition.
# Find and fix the bug.

# Example of the expected behavior:
# Calculator.add(1, 2)  # Expected output: 3
# Calculator.subtract(1, 2)  # Expected output: -1


class Calculator:
    def add(a: int, b: int) -> int:
        return a + b

    def subtract(a: int, b: int) -> int:
        return a - b
