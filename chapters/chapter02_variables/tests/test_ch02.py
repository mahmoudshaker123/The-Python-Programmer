from ..exercises.exercise_ch2_01 import celsius_to_fahrenheit
from ..exercises.exercise_ch2_02 import compute_area_of_circle
from ..exercises.exercise_ch2_03 import compute_average_grade
from ..exercises.exercise_ch2_04 import add_numbers
from ..exercises.exercise_ch2_05 import total_length_of_words


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
    assert compute_average_grade(90, 80, 70) == 80
    assert compute_average_grade(80, 70, 60) == 70
    assert compute_average_grade(70, 60, 50) == 60


def test_ch02_e04():
    assert add_numbers("0", "0") == "0"
    assert add_numbers("1", "2") == "3"
    assert add_numbers("100", "100") == "200"
    assert add_numbers("-1000", "500") == "-500"


def test_ch02_e05():
    total_length_of_words("", "") == 0
    total_length_of_words("Hello", "World") == 10
    total_length_of_words("Python", "Programming") == 17
