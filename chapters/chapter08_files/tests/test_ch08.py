from ..exercises.exercise_ch8_01 import count_errors_from_file
from ..exercises.exercise_ch8_02 import word_frequency
from ..exercises.exercise_ch8_03 import FileHandler
from ..exercises.exercise_ch8_04 import generate_report


def test_ch08_e01():
    assert count_errors_from_file() == 2


def test_ch08_e02():
    assert word_frequency("Hello, World! Hello, Python!") == {
        "Hello": 2,
        "World": 1,
        "Python": 1,
    }


def test_ch08_e03():
    file_handler = FileHandler("test.txt")
    file_handler.write("Hello, World!")
    assert file_handler.read() == "Hello, World!"


def test_ch08_e04():
    sales = [
        ("ProductA", 100, 10),
        ("ProductB", 200, 20),
        ("ProductC", 300, 30),
        ("ProductD", 400, 40),
    ]
    assert generate_report(sales) == "Total sales: 30000"
