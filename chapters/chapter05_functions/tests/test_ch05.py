from ..exercises.exercise_ch5_01 import add_by
from ..exercises.exercise_ch5_02 import is_palindrome
from ..exercises.exercise_ch5_03 import factorial
from ..exercises.exercise_ch5_04 import factorial_recursive
from ..exercises.exercise_ch5_05 import apply_functions
from ..exercises.exercise_ch5_06 import find_max
from ..exercises.exercise_ch5_07 import sum_array
from ..exercises.exercise_ch5_08 import multiply


def test_ch05_e01():
    assert add_by(5, 5) == 10
    assert add_by(10, 2) == 12
    assert add_by(10) == 11


def test_ch05_e02():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("mom") is True


def test_ch05_e03():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6


def test_ch05_e04():
    assert factorial_recursive(5) == 120
    assert factorial_recursive(4) == 24
    assert factorial_recursive(3) == 6


def test_ch05_e05():
    def add_one(n):
        return n + 1

    def double(n):
        return n * 2

    def square(n):
        return n**2

    assert apply_functions(5, add_one, double, square) == 36
    assert apply_functions(3, add_one, double, square) == 16
    assert apply_functions(4, add_one, double, square) == 25


def test_ch05_e06():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 10


def test_ch05_e07():
    assert sum_array([1, 2, 3, 4, 5]) == 15
    assert sum_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert sum_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 55


def test_ch05_e08():
    assert multiply(5, 5) == 25
    assert multiply(10, 2) == 20
    assert multiply(10, 0) == 0
