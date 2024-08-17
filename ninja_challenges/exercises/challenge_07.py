# Challenge 07 - Compute Rows in Pascal's Triangle

# This figure shows the first 5 rows of Pascal's triangle:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# Each entry in each row before the last one is adjacent to one or two numbers in the row below it.
# Each entry holds the sum of the numbers in the adjacent positions in the row above it.


# Write a function that takes a positive integer n and returns the first n rows of Pascal's triangle.
def pascals_triangle(n: int) -> list[list[int]]: ...
