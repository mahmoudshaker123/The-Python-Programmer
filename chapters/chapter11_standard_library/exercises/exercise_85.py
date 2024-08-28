# Exercise 85 - Parse transaction files
# Given the following class and function, implement the `parse_transactions` function that reads a file
# and returns a list of transactions. Each line in the file contains a timestamp and a description separated by a comma.
# The timestamp should be converted to a `datetime` object.
#
from dataclasses import dataclass


@dataclass
class Transaction:
    timestamp: str  # Replace with `datetime`
    description: str


def parse_transactions(filename: str) -> list[Transaction]:
    # Your code should go here.

    ...
