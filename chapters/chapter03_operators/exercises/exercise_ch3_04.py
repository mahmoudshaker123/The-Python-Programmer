## Exercise 03_04 - Is Prime

# Write a function that takes an integer as input and returns True if the number is prime, False otherwise.
# A prime number is a number that is only divisible by 1 and itself.
# For example, 2, 3, 5, 7, 11, 13, and 17 are prime numbers.

# There is a bug in the code below. Find and fix it.


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return False
