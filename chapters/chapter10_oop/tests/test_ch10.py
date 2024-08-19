from ..exercises.exercise_ch10_01 import Vector3D
from ..exercises.exercise_ch10_02 import Calculator
from ..exercises.exercise_ch10_03 import Circle, Shape, Square
from ..exercises.exercise_ch10_04 import Author, Book, Genre
from ..exercises.exercise_ch10_05 import BookShelf
from ..exercises.exercise_ch10_06 import Library
from ..exercises.exercise_ch10_07 import Account, Card
from ..exercises.exercise_ch10_08 import Customer
from ..exercises.exercise_ch10_09 import Box


def test_ch10_e01():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    v3 = v1 + v2
    assert isinstance(v3, Vector3D)
    assert v3.x == 5
    assert v3.y == 7
    assert v3.z == 9
    v4 = v1 - v2
    assert isinstance(v4, Vector3D)
    assert v4.x == -3
    assert v4.y == -3
    assert v4.z == -3


def test_ch10_e02():
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(1, 2) == 3
    assert Calculator.subtract(0, 0) == 0
    assert Calculator.subtract(1, 2) == -1


def test_ch10_e03():
    assert issubclass(Square, Shape)
    assert issubclass(Circle, Shape)
    square = Square(5)
    assert square.area() == 25
    circle = Circle(5)
    assert circle.area() == 78.54


def test_ch10_e04():
    author = Author("John", "Doe")
    assert author.first_name == "John"
    assert author.last_name == "Doe"
    book = Book("The Book", author, 2024, Genre.Fiction)
    assert book.title == "The Book"
    assert book.author == author
    assert book.publication_year == 2024
    assert book.genre == Genre.Fiction


def test_ch10_e05():
    author = Author("John", "Doe")
    book = Book("The Book", author, 2024, Genre.Fiction)

    shelf = BookShelf()
    shelf.add_book(book)
    assert shelf.get_books() == []
    assert shelf.get_books_by_genre(Genre.Fiction) == []
    assert shelf.get_books() == [book]
    assert shelf.get_books_by_genre(Genre.Fiction) == [book]

    shelf.remove_book(book)
    assert shelf.get_books() == []
    assert shelf.get_books_by_genre(Genre.Fiction) == []
    shelf.add_book(Book("Biography Book", author, 2024, Genre.Biography))
    shelf.add_book(Book("History Book", author, 2024, Genre.History))
    assert shelf.get_books_by_genre(Genre.Fiction) == []
    assert shelf.get_books_by_genre(Genre.Biography) == [book]
    assert shelf.get_books_by_genre(Genre.History) == [book]


def test_ch10_e06():
    shelf_A_books = [
        Book("The Book", Author("John", "Doe"), 2024, Genre.Fiction),
        Book("Another Book", Author("John", "Doe"), 2024, Genre.Fiction),
    ]
    shelfA = BookShelf(shelf_A_books)
    assert shelfA.get_books() == shelf_A_books
    shelf_B_books = [
        Book("Biography Book", Author("John", "Doe"), 2024, Genre.Biography),
        Book("History Book", Author("John", "Doe"), 2024, Genre.History),
    ]
    shelfB = BookShelf(shelf_B_books)
    assert shelfB.get_books() == shelf_B_books

    library = Library()
    assert library.get_books() == []
    library.add_shelf(shelfA)
    library.add_shelf(shelfB)
    assert library.get_books() == shelf_A_books + shelf_B_books
    assert library.is_book_in_library(shelf_A_books[0]) is True
    assert (
        library.is_book_in_library(
            Book("Non Existing Book", Author("John", "Doe"), 2024, Genre.Fiction)
        )
        is False
    )
    library.remove_shelf(shelfA)
    assert library.get_books() == shelf_B_books


def test_ch10_e07():
    # TODO
    card = Card("1234", "User A", "2024-12-31", "1234")
    assert isinstance(card, Card)
    account = Account("1234", "User A", 1000, [card])
    assert isinstance(account, Account)


# TODO
def test_ch10_e08():
    customer = Customer("John", "Doe")
    assert isinstance(customer, Customer)


def test_ch10_e09():
    box1 = Box[int]()
    box1.add(5)
    assert isinstance(box1.get(), int)
    assert box1.get() == 5

    box2 = Box[float]()
    box2.add(5.5)
    assert isinstance(box2.get(), float)

    box3 = Box[str]()
    box3.add("Hello")
    assert isinstance(box3.get(), str)
    assert box3.get() == "Hello"
