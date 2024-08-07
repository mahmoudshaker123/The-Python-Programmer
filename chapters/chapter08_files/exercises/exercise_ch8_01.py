## Exercise 08_01 - Log File Analysis
# Write a function log_file_analysis that reads a log file log.txt and
# counts the number of occurrences of the word "ERROR". Print the count to the console.

# Example log.txt:
# INFO: 2021-07-01 10:00:00: System started
# INFO: 2021-07-01 10:00:01: User logged in
# ERROR: 2021-07-01 10:00:02: System crashed
# INFO: 2021-07-01 10:00:03: System restarted
# ERROR: 2021-07-01 10:00:04: System crashed again

# Result: 2


def count_errors_from_file(file_name: str) -> int:
    with open(file_name, "r") as file:
        return file.read().count("ERROR")
