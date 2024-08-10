from exercises.challenge_00 import hello_world
from exercises.exercise_ch5_04 import number_of_1_bits


def test_hello_world():
    assert hello_world() == "Hello, World!"


def test_ch05_e04():
    assert number_of_1_bits(0) == 0
    assert number_of_1_bits(1) == 1
    assert number_of_1_bits(11) == 3
    assert number_of_1_bits(255) == 8
    assert number_of_1_bits(512) == 1
    assert number_of_1_bits(1023) == 10
