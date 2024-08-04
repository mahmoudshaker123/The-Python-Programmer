from ..exercises.exercise_ch2_01 import celsius_to_fahrenheit
from ..exercises.exercise_ch2_03 import compute_area_of_circle
from ..exercises.exercise_ch2_04 import compute_average_grade


def test_ch02_e01():
    assert celsius_to_fahrenheit(10) == 0


def test_ch02_e0x():
    assert compute_area_of_circle(10) == 0
    assert compute_area_of_circle(10) == 0


def test_ch02_e0x():
    assert compute_average_grade(10, 20, 30, 40) == 25
    assert compute_average_grade(0, 0, 0, 0) == 0
