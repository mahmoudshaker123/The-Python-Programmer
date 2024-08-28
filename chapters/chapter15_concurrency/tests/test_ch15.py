# from exercises.exercise_1 import my_function
import pytest
import asyncio
from ..exercises.exercise_97 import add_matrices
from ..exercises.exercise_98 import fetch_urls
from ..exercises.exercise_99 import BankAccount
from ..exercises.exercise_100 import time_it


def test_e97():
    assert add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]]
    assert add_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]) == [
        [8, 10, 12],
        [14, 16, 18],
    ]
    assert add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]]


def test_e98():
    assert fetch_urls(["https://www.google.com", "https://www.yahoo.com"]) == [
        "Google",
        "Yahoo",
    ]


def test_e99():
    account = BankAccount("John Doe", 1000)
    assert account.balance == 1000
    account.deposit(500)
    assert account.balance == 1500
    account.withdraw(200)
    assert account.balance == 1300
    with pytest.raises(ValueError):
        account.withdraw(2000)
    assert account.balance == 1300


def test_e100():
    @time_it
    def foo():
        for _ in range(3600):
            pass

    foo()

    @time_it
    def async_bar():
        pass

    asyncio.run(async_bar())
