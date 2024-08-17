from datetime import date
from ..exercises.exercise_ch11_01 import days_until_next_birthday
from ..exercises.exercise_ch11_02 import Address, Person
from ..exercises.exercise_ch11_03 import multiply_by_10
from ..exercises.exercise_ch11_04 import flatten_list_of_lists


def test_ch11_e01():
    assert (
        days_until_next_birthday(birthday=date(2021, 1, 1), now=date(2021, 1, 1)) == 364
    )
    assert (
        days_until_next_birthday(birthday=date(1994, 12, 18), now=date(2024, 8, 15))
        == 120
    )
    assert (
        days_until_next_birthday(birthday=date(1990, 1, 15), now=date(2025, 1, 1)) == 14
    )
    assert (
        days_until_next_birthday(birthday=date(1992, 1, 2), now=date(2025, 1, 2)) == 0
    )


def test_ch11_e02():
    address = Address(street="123 Main St", city="Springfield", zip_code="12345")
    person = Person(name="John Doe", age=30, address=address)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.address.street == "123 Main St"
    assert person.address.city == "Springfield"
    assert person.address.zip_code == "12345"
    assert person.previous_address == []

    address_2 = Address(street="456 Elm St", city="Springfield", zip_code="12345")
    address_3 = Address(street="789 Oak St", city="Springfield", zip_code="12345")
    person_2 = Person(
        name="Jane Doe",
        age=28,
        address=address,
        previous_address=[address_2, address_3],
    )
    assert person_2.name == "Jane Doe"
    assert person_2.age == 28
    assert person_2.address.street == "123 Main St"
    assert person_2.address.city == "Springfield"
    assert person_2.address.zip_code == "12345"
    assert person_2.previous_address == [address_2, address_3]


def test_ch11_e03():
    assert multiply_by_10(5) == 50
    assert multiply_by_10(10) == 100
    assert multiply_by_10(15) == 150
    assert multiply_by_10(0) == 0


def test_ch11_e04():
    assert flatten_list_of_lists([[]]) == []
    assert flatten_list_of_lists([[1, 2], [3, 4], [5, 6]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    assert flatten_list_of_lists([[1, 2, 3]]) == [1, 2, 3]
    assert flatten_list_of_lists([[1], [2], [3]]) == [1, 2, 3]
    assert flatten_list_of_lists([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten_list_of_lists([[1], [2, 3], [4]]) == [1, 2, 3, 4]
