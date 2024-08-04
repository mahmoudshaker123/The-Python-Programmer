from ..exercises.exercise_ch7_01 import get_substring
from ..exercises.exercise_ch7_02 import reverse_string
from ..exercises.exercise_ch7_03 import replace_spaces_with_hyphens
from ..exercises.exercise_ch7_04 import extract_error_messages
from ..exercises.exercise_ch7_05 import calculate_product_sales


def test_ch07_e01():
    assert get_substring("Hello, World!", 0, 5) == "Hello"
    assert get_substring("Hello, World!", 7, 12) == "World"


def test_ch07_e02():
    assert reverse_string("ABCDEF") == "FEDCBA"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("Python") == "nohtyP"


def test_ch07_e03():
    assert replace_spaces_with_hyphens("Hello, World!") == "Hello,-World!"
    assert replace_spaces_with_hyphens("Python is fun!") == "Python-is-fun!"
    assert replace_spaces_with_hyphens("This is a test") == "This-is-a-test"


def test_ch07_e04():
    log_entries = [
        "2021-05-10 08:00:00 INFO System started",
        "2021-05-10 08:01:00 INFO User logged in",
        "2021-05-10 08:02:00 ERROR Database connection failed",
        "2021-05-10 08:03:00 ERROR File not found",
        "2021-05-10 08:04:00 INFO System stopped",
    ]
    assert extract_error_messages(log_entries) == [
        "Database connection failed",
        "File not found",
    ]


def test_ch07_e05():
    sales = [
        ("ProductA", 100, 10),
        ("ProductB", 200, 20),
        ("ProductC", 300, 30),
        ("ProductD", 400, 40),
    ]
    assert calculate_product_sales(sales) == 30000
