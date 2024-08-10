import pytest
from ..exercises.exercise_ch9_01 import divide
from ..exercises.exercise_ch9_02 import check_positive, NegativeValueError
from ..exercises.exercise_ch9_03 import robust_file_reader


def test_ch09_e01():
    assert divide(1, 1) == 1
    assert divide(1, 2) == 0.5
    assert divide(10, 0) is None
    assert divide(10, 2) == 5
    assert divide(10, 5) == 2


def test_ch09_e02():
    assert check_positive(0) == 0
    assert check_positive(10) == 10
    with pytest.raises(NegativeValueError):
        check_positive(-1)
    with pytest.raises(NegativeValueError):
        check_positive(-10)


def test_ch09_e03():
    assert robust_file_reader() == "Hello, World!"
    assert robust_file_reader() == "FileEmptyError"
