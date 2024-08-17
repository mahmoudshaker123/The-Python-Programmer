# Challenge 05 - Compute All Valid IP Addresses
# A decimal string is a string consisting of digits from 0 to 9.
# Internet Protocols (IP) addresses can be written as four decimal strings separated by periods,
# e.g., 192.168.0.1.

# Write a function that determines where to add periods to a decimal string so that the resulting
# string is a valid IP address. There may be more than one valid IP address corresponding to a
# decimal string, in which case you should return all possibilities.

# For example, if the mangled string is "19216811", then the resulting IP addresses could be
# ["192.168.1.1", "19.216.81.1"]


def compute_ip_addresses(s: str) -> list[str]: ...
