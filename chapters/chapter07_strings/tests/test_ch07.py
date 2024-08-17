from ..exercises.exercise_ch7_01 import get_substring
from ..exercises.exercise_ch7_02 import reverse_string
from ..exercises.exercise_ch7_03 import reverse_each_word
from ..exercises.exercise_ch7_04 import replace_spaces_with_hyphens
from ..exercises.exercise_ch7_05 import extract_error_messages
from ..exercises.exercise_ch7_06 import calculate_product_sales
from ..exercises.exercise_ch7_07 import find_longest_word
from ..exercises.exercise_ch7_08 import compress_string


def test_ch07_e01():
    assert get_substring("Hello", 1, 3) == "el"
    assert get_substring("Hello, World!", 0, 5) == "Hello"
    assert get_substring("Hello, World!", 7, 12) == "World"
    assert get_substring("Python is fun!", 7, 9) == "is"
    assert get_substring("Python is fun!", 0, 5) == "Python"


def test_ch07_e02():
    assert reverse_string("") == ""
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("ABCDEF") == "FEDCBA"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("Python") == "nohtyP"


def test_ch07_e03():
    assert reverse_each_word("") == ""
    assert reverse_each_word("HelloWorld") == "HelloWorld"
    assert reverse_each_word("Hello World") == "olleH dlroW"
    assert reverse_each_word("I want to reverse this") == "I tnaw ot esrever siht"


def test_ch07_e04():
    assert replace_spaces_with_hyphens("") == ""
    assert replace_spaces_with_hyphens("HelloWorld") == "HelloWorld"
    assert replace_spaces_with_hyphens("Hello World") == "Hello-World"
    assert replace_spaces_with_hyphens("Give Me Some Space") == "Give-Me-Some-Space"
    assert replace_spaces_with_hyphens("Give Me More-Hyphens") == "Give-Me-More-Hyphens"


def test_ch07_e05():
    assert extract_error_messages([]) == []
    assert extract_error_messages(["INFO User logged in"]) == []
    assert extract_error_messages(
        ["ERROR Unable to connect to the server", "ERROR Server error"]
    ) == [
        "Unable to connect to the server",
        "Server error",
    ]
    assert extract_error_messages(
        ["ERROR Unable to connect to the server", "INFO User logged in"]
    ) == ["Unable to connect to the server"]
    assert extract_error_messages(
        [
            "INFO System started",
            "DEBUG Sytem running",
            "ERROR Unable to connect to the server",
            "ERROR Server error",
            "INFO User logged in",
            "ERROR Sytem crashed",
        ]
    ) == [
        "Unable to connect to the server",
        "Server error",
        "Sytem crashed",
    ]


def test_ch07_e06():
    assert calculate_product_sales([]) == []
    assert calculate_product_sales(
        [
            "2021-01-01,Apple,100",
            "2021-01-02,Banana,200",
            "2021-01-03,Apple,300",
            "2021-01-04,Banana,400",
        ]
    ) == [("Apple", 400), ("Banana", 600)]
    assert calculate_product_sales(
        [
            "2021-01-01,Apple,100",
            "2021-01-01,Orange,200",
            "2021-01-02,Apple,150",
            "2021-01-02,Orange,250",
        ]
    ) == [("Apple", 250), ("Orange", 450)]
    assert calculate_product_sales(
        [
            "2021-01-01,Apple,100",
            "2021-01-01,Orange,200",
            "2021-01-02,Banana,150",
            "2021-01-02,Orange,250",
            "2021-01-03,Apple,200",
            "2021-01-03,Banana,300",
        ]
    ) == [("Apple", 300), ("Orange", 450), ("Banana", 450)]


def test_ch07_e07():
    assert find_longest_word("") == ""
    assert (
        find_longest_word(["hello", "world", "python", "programming"]) == "programming"
    )
    assert (
        find_longest_word(["hello", "world", "python", "programming", "language"])
        == "programming"
    )
    assert find_longest_word(["I", "am", "learning", "Python"]) == "learning"
    assert find_longest_word(["Hello", "World"]) == "Hello"


def test_ch07_e08():
    assert compress_string("") == ""
    assert compress_string("abcd") == "abcd"
    assert compress_string("aaabbbbbcc") == "a3b5c2"
    assert compress_string("aabbbcc") == "a2b3c2"
    assert compress_string("aaaaaabbbc") == "a6b2c"
    assert compress_string("aadddcccbb") == "a2d3c3b2"
