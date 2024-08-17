# Challenge 16 - Word Search
# Write a function that takes a 2D matrix of letters and a word
# and returns True if the word is present in the matrix.

# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example:
# Given the following matrix:
# [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E'],
# ]
#
# word_search(matrix, "ABCCED") -> True
# word_search(matrix, "SEE") -> True
# word_search(matrix, "ABCB") -> False


def is_word_in_matrix(matrix: list[list[str]], word: str) -> bool: ...
