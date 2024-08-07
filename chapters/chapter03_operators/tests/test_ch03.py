from ..exercises.exercise_ch3_01 import fizzbuzz
from ..exercises.exercise_ch3_02 import compute_slope
from ..exercises.exercise_ch3_03 import bitwise_operations
from ..exercises.exercise_ch3_04 import is_prime


def test_ch03_e01():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == "7"


def test_ch03_e02():
    assert compute_slope(0, 0, 4, 2) == 0.5
    assert compute_slope(0, 0, 1, 1) == 1
    assert compute_slope(0, 0, 2, 4) == 2


def test_ch03_e03():
    assert bitwise_operations(0, 0) == "0 0 0"
    assert bitwise_operations(5, 3) == "1 7 6"
    assert bitwise_operations(10, 5) == "0 15 15"
    assert bitwise_operations(15, 10) == "10 15 5"


def test_ch03_e04():
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(21) == False
    assert is_prime(23) == True
