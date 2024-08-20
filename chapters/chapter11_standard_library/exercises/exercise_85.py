# Exercise 11_07 - Parse transaction files
# Given this "RateInterestCalculator" class with two methods,
# we need to replace the print() messages with log statements instead with
# the appropriate Log Level.

# Can you fix this?


class Transaction:
    timestamp: str  # Replace with `datetime`
    description: str


def parse_transactions(filename): ...
