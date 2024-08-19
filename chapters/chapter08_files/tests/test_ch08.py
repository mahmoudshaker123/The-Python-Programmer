import textwrap

import pytest

from ..exercises.exercise_ch8_01 import count_errors_from_file
from ..exercises.exercise_ch8_02 import count_word_frequency
from ..exercises.exercise_ch8_03 import course_grades_summary
from ..exercises.exercise_ch8_04 import inventory_management


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
            """
            ),
            {},
        ),
        (
            textwrap.dedent(
                """
                python is a popular programming language
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
                python is a popular programming language
                python is a popular programming language
            """
            ),
            {
                "python": 2,
                "is": 2,
                "a": 2,
                "popular": 2,
                "programming": 2,
                "language": 2,
            },
        ),
    ],
)
def test_ch08_e02(source, expected):
    assert count_word_frequency(source) == expected


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
            """
            ),
            [],
        ),
        (
            textwrap.dedent(
                """
                Math: 90, 85, 88, 92, 95
                Science: 78, 85, 88, 92, 95
                History: 88, 85, 88, 92, 95
                English: 98, 85, 88, 92, 95"""
            ),
            [
                ("Math", 90.0),
                ("Science", 87.6),
                ("History", 89.6),
                ("English", 91.6),
            ],
        ),
        (
            textwrap.dedent(
                """
                Math: 90, 85, 88, 92, 95
                Science: 78, 85, 88, 92, 95
                Physics: 61, 75, 70, 92, 93, 98, 81, 59, 88, 92
            """
            ),
            [("Math", 90.0), ("Science", 87.6), ("Physics", 79.9)],
        ),
    ],
)
def test_ch08_e03(source, expected):
    assert course_grades_summary(source) == expected


@pytest.mark.parametrize(
    "file_content, restock_threshold, expected",
    [
        (
            textwrap.dedent(
                """
            """
            ),
            0,
            [],
        ),
        (
            textwrap.dedent(
                """
                item_name,item_id,quantity,price
                Apple,1,100,0.5
                Banana,2,200,0.3
                Orange,3,150,0.4
            """
            ),
            200,
            [
                {
                    "item_name": "Apple",
                    "item_id": 1,
                    "quantity": 100,
                    "price": 0.5,
                },
                {
                    "item_name": "Orange",
                    "item_id": 3,
                    "quantity": 150,
                    "price": 0.4,
                },
            ],
        ),
        (
            textwrap.dedent(
                """
                item_name,item_id,quantity,price
                Apple,1,100,0.5
                Banana,2,200,0.3
                Orange,3,150,0.4
            """
            ),
            100,
            [
                {
                    "item_name": "Apple",
                    "item_id": 1,
                    "quantity": 100,
                    "price": 0.5,
                },
            ],
        ),
        (
            textwrap.dedent(
                """
                item_name,item_id,quantity,price
                Apple,1,100,0.5
                Banana,2,200,0.3
                Orange,3,150,0.4
            """
            ),
            300,
            [],
        ),
        (
            textwrap.dedent(
                """
                item_name,item_id,quantity,price
                Apple,1,100,0.5
                Banana,2,200,0.3
                Orange,3,150,0.4
                Pear,4,300,0.6
                Kiwi,5,400,0.7
            """
            ),
            250,
            [
                {
                    "item_name": "Apple",
                    "item_id": 1,
                    "quantity": 100,
                    "price": 0.5,
                },
                {
                    "item_name": "Orange",
                    "item_id": 3,
                    "quantity": 150,
                    "price": 0.4,
                },
            ],
        ),
    ],
)
def test_ch08_e04(source, restock_threshold, expected):
    assert inventory_management(source, restock_threshold) == expected
