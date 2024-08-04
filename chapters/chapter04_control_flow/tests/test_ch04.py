from ..exercises.exercise_ch4_01 import check_number
from ..exercises.exercise_ch4_02 import is_even
from ..exercises.exercise_ch4_03 import grade_result
from ..exercises.exercise_ch4_04 import calculator
from ..exercises.exercise_ch4_05 import sum_numbers_from_1_to_10
from ..exercises.exercise_ch4_06 import sum_even_numbers_from_1_to_100
from ..exercises.exercise_ch4_08 import calculate_total_length


def test_ch04_e01():
    assert check_number(5) == "Number is positive"


def test_ch04_e02():
    assert is_even(4) == "Number is even"


def test_ch04_e03():
    assert grade_result(80) == "Grade is A"


def test_ch04_e04():
    assert calculator(4, 5, "+") == 9


def test_ch04_e05():
    assert sum_numbers_from_1_to_10() == 55


def test_ch04_e06():
    assert sum_even_numbers_from_1_to_100() == 2550


def test_ch04_e08():
    assert calculate_total_length("Hello", "World") == 10
