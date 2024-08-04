from ..exercises.exercise_ch6_01 import remove_duplicates
from ..exercises.exercise_ch6_02 import count_occurrences
from ..exercises.exercise_ch6_03 import count_letters
from ..exercises.exercise_ch6_04 import unique_elements
from ..exercises.exercise_ch6_05 import tuple_frequency


def test_ch06_e01():
    assert remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 6, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert remove_duplicates([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_ch06_e02():
    assert count_occurrences(
        ["apple", "banana", "apple", "banana", "apple", "apple", "apple"]
    ) == {"apple": 5, "banana": 2}
    assert count_occurrences(["A", "B", "A", "B", "A", "A", "A"]) == {"A": 5, "B": 2}
    assert count_occurrences(["WordA", "WordB"]) == {"WordA": 1, "WordB": 1}


def test_ch06_e03():
    assert count_letters("apple") == {"a": 1, "p": 2, "l": 1, "e": 1}
    assert count_letters("banana") == {"b": 1, "a": 3, "n": 2}
    assert count_letters("Word") == {"W": 1, "o": 1, "r": 1, "d": 1}


def test_ch06_e04():
    assert unique_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) == {1, 2, 3, 4, 5, 6, 7, 8}
    assert unique_elements([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    }
    assert unique_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == {1, 2, 3, 4, 5}


def test_ch06_e05():
    assert tuple_frequency(
        [
            ("apple", "banana"),
            ("apple", "banana"),
            ("apple", "banana"),
            ("apple", "banana"),
        ]
    ) == {("apple", "banana"): 4}
    assert tuple_frequency(["A", "B", "A", "B", "A", "A", "A"]) == {
        "A": 5,
        "B": 2,
    }
