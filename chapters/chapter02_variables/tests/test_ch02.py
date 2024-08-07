from ..exercises.exercise_ch2_01 import celsius_to_fahrenheit
from ..exercises.exercise_ch2_02 import compute_area_of_circle
from ..exercises.exercise_ch2_03 import compute_average_grade
from ..exercises.exercise_ch2_04 import add_numbers
from ..exercises.exercise_ch2_05 import total_length_of_words
from ..exercises.exercise_ch2_06 import area_of_triangle
from ..exercises.exercise_ch2_07 import convert_binary_to_decimal


def test_ch02_e01():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6


def test_ch02_e02():
    assert compute_area_of_circle(0) == 0
    assert compute_area_of_circle(1) == 3.14159
    assert compute_area_of_circle(2) == 12.56636


def test_ch02_e03():
    assert compute_average_grade(100, 100, 100) == 100
    assert compute_average_grade(94, 94, 95) == 94.33
    assert compute_average_grade(88, 77, 66) == 77
    assert compute_average_grade(72.5, 66.8, 50.5) == 63.27


def test_ch02_e04():
    assert add_numbers("0", "0") == "0"
    assert add_numbers("1", "2") == "3"
    assert add_numbers("100", "100") == "200"
    assert add_numbers("-1000", "500") == "-500"


def test_ch02_e05():
    total_length_of_words("", "") == 0
    total_length_of_words("Hello", "World") == 10
    total_length_of_words("Python", "Programming") == 17


def test_ch02_e06():
    assert area_of_triangle(0, 0) == 0
    assert area_of_triangle(1, 1) == 0.5
    assert area_of_triangle(2, 2) == 2
    assert area_of_triangle(3, 3) == 4.5


def test_ch02_e07():
    assert convert_binary_to_decimal("0") == 0
    assert convert_binary_to_decimal("10") == 2
    assert convert_binary_to_decimal("11") == 3
    assert convert_binary_to_decimal("100") == 4
