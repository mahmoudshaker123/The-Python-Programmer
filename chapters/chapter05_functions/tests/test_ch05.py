from ..exercises.exercise_ch5_01 import increment_by
from ..exercises.exercise_ch5_02 import is_palindrome
from ..exercises.exercise_ch5_03 import factorial
from ..exercises.exercise_ch5_04 import number_of_1_bits
from ..exercises.exercise_ch5_05 import apply_vouchers
from ..exercises.exercise_ch5_06 import find_max
from ..exercises.exercise_ch5_07 import sum_digits
from ..exercises.exercise_ch5_08 import multiply
from ..exercises.exercise_ch5_09 import reverse_vowels
from ..exercises.exercise_ch5_10 import count_char_freq


def test_ch05_e01():
    assert increment_by(5, 5) == 10
    assert increment_by(10, 2) == 12
    assert increment_by(10) == 11


def test_ch05_e02():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("mom") is True


def test_ch05_e03():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6


def test_ch05_e04():
    assert number_of_1_bits(0) == 0
    assert number_of_1_bits(1) == 1
    assert number_of_1_bits(11) == 3
    assert number_of_1_bits(255) == 8
    assert number_of_1_bits(512) == 1
    assert number_of_1_bits(1023) == 10


def test_ch05_e05():
    def ten_percent(x: int):
        return x - (x * 0.10)

    def fifteen_percent(x: int):
        return x - (x * 0.15)

    def five_dollar(x: int):
        return x - 5

    assert apply_vouchers(ten_percent, total=100) == 90
    assert apply_vouchers(fifteen_percent, total=100) == 85
    assert apply_vouchers(five_dollar, total=100) == 95
    assert apply_vouchers(ten_percent, fifteen_percent, total=100) == 76.5
    assert apply_vouchers(ten_percent, fifteen_percent, five_dollar, total=100) == 71.5


def test_ch05_e06():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 10


def test_ch05_e07():
    assert sum_digits("") == 0
    assert sum_digits("1") == 1
    assert sum_digits("123") == 6
    assert sum_digits("123456") == 21
    assert sum_digits("123456789") == 45


def test_ch05_e08():
    assert multiply(5, 5) == 25
    assert multiply(10, 2) == 20
    assert multiply(10, 0) == 0


def test_ch05_e09():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("world") == "world"
    assert reverse_vowels("applepie") == "epplapie"
    assert reverse_vowels("racecar") == "racecar"
    assert reverse_vowels("headphones") == "heedphonas"


def test_ch05_e10():
    assert count_char_freq("hello", "l") == 2
    assert count_char_freq("hello", "o") == 1
    assert count_char_freq("Programming in python", "p") == 1
    assert count_char_freq("Programming in python".lower(), "p") == 2
