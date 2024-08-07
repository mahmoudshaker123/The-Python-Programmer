import textwrap
import pytest
from ..exercises.exercise_ch8_01 import count_errors_from_file
from ..exercises.exercise_ch8_02 import count_word_frequency
from ..exercises.exercise_ch8_03 import FileHandler
from ..exercises.exercise_ch8_04 import course_grades_summary


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
            INFO: System started
            ERROR: System crashed
            """
            ),
            1,
        ),
        (
            textwrap.dedent(
                """
                INFO: System started
                INFO: User logged in
                ERROR: System crashed
                INFO: System restarted
                ERROR: System crashed again
            """
            ),
            2,
        ),
    ],
)
def test_ch08_e01(source, expected):
    assert count_errors_from_file(source) == expected


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
                Python is a popular programming language
            """
            ),
            {
                "python": 1,
                "is": 1,
                "a": 1,
                "popular": 1,
                "programming": 1,
                "language": 1,
            },
        ),
        (
            textwrap.dedent(
                """
            Word_A Word_B Word_A Word_C Word_B WORD_A word_a WoRD_A Word_B
            """
            ),
            {"word_a": 5, "word_b": 3, "word_c": 1},
        ),
    ],
)
def test_ch08_e02(source, expected):
    assert count_word_frequency(source) == expected


@pytest.mark.parametrize(
    "file_content",
    [
        textwrap.dedent(
            """
                Python is a popular programming language
            """
        ),
    ],
)
def test_ch08_e03(source):
    file_handler = FileHandler(source)
    file_handler.write("Hello, World!")
    assert file_handler.read() == "Hello, World!"


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
                Math: 90, 85, 88, 92, 95
                Science: 78, 85, 88, 92, 95
                History: 88, 85, 88, 92, 95
                English: 98, 85, 88, 92, 95   
            """
            ),
            [("Math", 90.0), ("Science", 87.6), ("History", 89.6), ("English", 91.6)],
        ),
    ],
)
def test_ch08_e04(source, expected):
    assert course_grades_summary(source) == expected
