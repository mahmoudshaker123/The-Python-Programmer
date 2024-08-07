## Exercise 05_10 - Count Character Frequency
# Write a recursive function that takes a string and a character
# and returns the number of times the character appears in the string.


# There is a bug in the code below. Find and fix it.
def count_char_freq(string: str, target: str) -> int:
    if not string:
        return 0
    if string[0] == target:
        return count_char_freq(string[1:], target)
    else:
        return count_char_freq(string[1:], target)
