# Challenge 08 - UNIX Tail Command
# The UNIT tail command displays the last part of a file.
# For this challenge, assume that tail takes two arguments: a file name and
#  a number of lines, starting from the last line, that are to be printed.


# Write a function that implements the UNIX tail command.
def tail(file_name: str, n: int = 1) -> list[str]: ...
