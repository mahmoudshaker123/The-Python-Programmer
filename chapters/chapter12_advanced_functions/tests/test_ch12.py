import pytest

from ..exercises.exercise_ch12_01 import EvenNumberIterator
from ..exercises.exercise_ch12_02 import FibonacciIterator
from ..exercises.exercise_ch12_03 import even_numbers_generator
from ..exercises.exercise_ch12_04 import fibonacci_generator
from ..exercises.exercise_ch12_05 import counter
from ..exercises.exercise_ch12_06 import time_this
from ..exercises.exercise_ch12_07 import repeat_it


def test_ch12_e01():
    assert list(EvenNumberIterator(5)) == [0, 2, 4, 6, 8]
    iterator = EvenNumberIterator(5)
    assert next(iterator) == 0
    assert next(iterator) == 2
    assert next(iterator) == 4
    assert next(iterator) == 6
    assert next(iterator) == 8
    with pytest.raises(StopIteration):
        next(iterator)


def test_ch12_e02():
    assert list(FibonacciIterator(5)) == [0, 1, 1, 2, 3]
    iterator = FibonacciIterator(5)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)


def test_ch12_e03():
    assert list(even_numbers_generator(5)) == [0, 2, 4, 6, 8]
    iterator = even_numbers_generator(5)
    assert next(iterator) == 0
    assert next(iterator) == 2
    assert next(iterator) == 4
    assert next(iterator) == 6
    assert next(iterator) == 8
    with pytest.raises(StopIteration):
        next(iterator)


def test_ch12_e04():
    assert list(fibonacci_generator(5)) == [0, 1, 1, 2, 3]
    iterator = fibonacci_generator(5)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)


def test_ch12_e05():
    c = counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3


def test_ch12_e06():
    @time_this
    def my_function():
        pass

    my_function()


def test_ch12_e07():
    @repeat_it(3)
    def my_function():
        pass

    my_function()
    my_function()
