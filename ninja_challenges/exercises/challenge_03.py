# Challenge 03 - Merge list of Receipts
# You are given a list of receipts. Each receipt is a tuple of the form (name, amount).
# Write a function that merges the list of receipts into a dictionary,
# where the key is the name and the value is the total amount for that name.

# For example, given the following list of receipts:
# receipts = [
#     ("Alice", 100),
#     ("Bob", 200),
#     ("Alice", 200),
#     ("Bob", 100),
# ]

# The function should return the following dictionary:
# {
#     "Alice": 300,
#     "Bob": 300,
# }


def merge_receipts(receipts: list[tuple[str, int]]) -> dict[str, int]: ...
