from ..exercises.exercise_ch2_01 import hours_to_seconds
from ..exercises.exercise_ch2_02 import compute_average_grade
from ..exercises.exercise_ch2_03 import add_numbers
from ..exercises.exercise_ch2_04 import compute_length_difference
from ..exercises.exercise_ch2_05 import celsius_to_fahrenheit
from ..exercises.exercise_ch2_06 import convert_binary_to_decimal
from ..exercises.exercise_ch2_07 import calculate_gravity_force


def test_ch02_e01():
    assert hours_to_seconds(0) == 0
    assert hours_to_seconds(1) == 3600
    assert hours_to_seconds(2) == 7200
    assert hours_to_seconds(3) == 10800


def test_ch02_e02():
    assert compute_average_grade(100, 100, 100) == 100
    assert compute_average_grade(94, 94, 95) == 94.33
    assert compute_average_grade(88, 77, 66) == 77
    assert compute_average_grade(72.5, 66.8, 50.5) == 63.27


def test_ch02_e03():
    assert add_numbers("0", "0") == "0"
    assert add_numbers("1", "2") == "3"
    assert add_numbers("100", "100") == "200"
    assert add_numbers("-1000", "500") == "-500"


def test_ch02_e04():
    compute_length_difference("", "") == 0
    compute_length_difference("Hello", "World") == 0
    compute_length_difference("Python", "Java") == 2
    compute_length_difference("Python", "Programming") == 5


def test_ch02_e05():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6


def test_ch02_e06():
    assert convert_binary_to_decimal("0") == 0
    assert convert_binary_to_decimal("10") == 2
    assert convert_binary_to_decimal("11") == 3
    assert convert_binary_to_decimal("100") == 4


def test_ch02_e07():
    assert calculate_gravity_force(1, 1) == 9.8
    assert calculate_gravity_force(5, 2) == 19.6
    assert calculate_gravity_force(10, 5) == 49
    assert calculate_gravity_force(100, 10) == 980
