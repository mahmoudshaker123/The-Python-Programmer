import pytest
from ..exercises.exercise_64 import divide
from ..exercises.exercise_65 import check_positive, NegativeValueError

# from ..exercises.exercise_66 import
# from ..exercises.exercise_67 import


def test_e64():
    assert divide(1, 1) == 1
    assert divide(1, 2) == 0.5
    assert divide(10, 0) is None
    assert divide(10, 2) == 5
    assert divide(10, 5) == 2


def test_e65():
    assert check_positive(0) == 0
    assert check_positive(10) == 10
    with pytest.raises(NegativeValueError):
        check_positive(-1)
    with pytest.raises(NegativeValueError):
        check_positive(-10)
