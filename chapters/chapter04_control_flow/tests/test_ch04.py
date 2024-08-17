from ..exercises.exercise_ch4_01 import fizzbuzz
from ..exercises.exercise_ch4_02 import is_prime
from ..exercises.exercise_ch4_03 import check_number
from ..exercises.exercise_ch4_04 import is_even
from ..exercises.exercise_ch4_05 import grade_result
from ..exercises.exercise_ch4_06 import sum_numbers
from ..exercises.exercise_ch4_07 import sum_even_numbers
from ..exercises.exercise_ch4_08 import largest_index
from ..exercises.exercise_ch4_09 import calculate_total_length
from ..exercises.exercise_ch4_10 import double_elements
from ..exercises.exercise_ch4_11 import find_first_divisible_by_5
from ..exercises.exercise_ch4_12 import sum_positive_numbers
from ..exercises.exercise_ch4_13 import reverse_digits


def test_ch04_e01():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == "7"


def test_ch04_e02():
    assert is_prime(2) is True
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(21) is False
    assert is_prime(23) is True


def test_ch04_e03():
    assert check_number(0) == "Zero"
    assert check_number(5) == "Positive"
    assert check_number(-5) == "Negative"


def test_ch04_e04():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(4) is True
    assert is_even(5) is False


def test_ch04_e05():
    assert grade_result(90) == "A"
    assert grade_result(80) == "B"
    assert grade_result(70) == "C"
    assert grade_result(60) == "Not Pass"
    assert grade_result(50) == "Not Pass"


def test_ch04_e06():
    assert sum_numbers(0, 2) == 1
    assert sum_numbers(1, 10) == 45
    assert sum_numbers(1, 100) == 4950


def test_ch04_e07():
    assert sum_even_numbers(0, 2) == 0
    assert sum_even_numbers(1, 10) == 20
    assert sum_even_numbers(1, 100) == 2450


def test_ch04_e08():
    assert largest_index([1, 2, 3, 4, 5]) == 4
    assert largest_index([5, 4, 3, 2, 1]) == 0
    assert largest_index([1, 2, 5, 4, 3]) == 2
    assert largest_index([1, 2, 3, 5, 4]) == 3


def test_ch04_e09():
    assert calculate_total_length(["Hello", "World"]) == 10
    assert calculate_total_length(["Python", "Programming"]) == 17
    assert calculate_total_length(["Python", "Programming", "Language"]) == 25


def test_ch04_e10():
    assert double_elements([1, 2, 3]) == [2, 4, 6]
    assert double_elements([4, 5, 6]) == [8, 10, 12]
    assert double_elements([7, 8, 9]) == [14, 16, 18]


def test_ch04_e11():
    assert find_first_divisible_by_5([1, 2, 3, 4, 5]) == 5
    assert find_first_divisible_by_5([5, 10, 15, 20, 25]) == 5
    assert find_first_divisible_by_5([6, 7, 8, 9, 10]) == 10
    assert find_first_divisible_by_5([11, 13, 16]) is None


def test_ch04_e12():
    assert sum_positive_numbers([]) == 0
    assert sum_positive_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_positive_numbers([1, -2, 3, -4, 5]) == 9


def test_ch04_e13():
    assert reverse_digits(123) == 321
    assert reverse_digits(456) == 654
    assert reverse_digits(789) == 987
    assert reverse_digits(101) == 101
