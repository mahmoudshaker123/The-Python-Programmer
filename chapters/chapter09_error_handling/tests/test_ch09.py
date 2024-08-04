from ..exercises.exercise_ch9_01 import divide
from ..exercises.exercise_ch9_02 import check_positive
from ..exercises.exercise_ch9_03 import robust_file_reader


def test_ch09_e01():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Cannot divide by zero"


def test_ch09_e02():
    assert check_positive(10) == 10
    assert check_positive(-10) == "NegativeValueError"


def test_ch09_e03():
    assert robust_file_reader() == "Hello, World!"
    assert robust_file_reader() == "FileEmptyError"
