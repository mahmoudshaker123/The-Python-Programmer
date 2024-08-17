# Challenge 18 - Flatten Nested List Iterator
# Write an iterator that will flatten a nested list of integers.
# The iterator should have two methods:
# next() and hasNext().
#
# For example, given the following nested list:
# [
#     1,
#     [4, [6]]
# ]
#
# The iterator should return 1, 4, 6.


class NestedIterator:
    def __init__(self, nested_list: list[list[int]]): ...

    def next(self) -> int: ...

    def hasNext(self) -> bool: ...
