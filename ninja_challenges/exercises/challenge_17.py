# Challenge 17 - Compare Version Numbers
# Write a function that compares two version numbers version1 and version2.
# To compare version numbers, compare their components in left-to-right order.
# Components are separated by a dot '.' and each component may contain
# multiple digits. Every component contains non-negative integers except
# for the first component. The first component is a non-negative integer
# and the rest of the components are separated by a dot '.'.
# For example, 2.5.33 and 0.1 are valid version numbers.
# To compare version numbers:
# If version1 > version2 return 1,
# If version1 < version2 return -1,
# Otherwise return 0.


def compare_versions(version1: str, version2: str) -> int: ...
