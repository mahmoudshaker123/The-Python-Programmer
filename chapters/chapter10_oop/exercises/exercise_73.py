# Exercise 73 - Library Management System [Part 3/3]
# In this exercise, you will implement the `Library` class that will hold a collection of shelves.

# The `Library` class should have the following methods:
# 1. `add_shelf(shelf: BookShelf)`: Add a shelf to the library.
# 2. `remove_shelf(shelf: BookShelf)`: Remove a shelf from the library.
# 3. `get_books() -> List[Book]`: Return a list of all the books from all the shelves in the library.
# 4. `is_book_in_library(book: Book) -> bool`: Return `True` if the book is in the library, otherwise `False`.


# Note: Feel free to define any additional methods or attributes that
# you think are necessary for the `BookShelf` class.


# Example:
# author = Author("John", "Doe")
# book1 = Book("The Book", author, 2021, Genre.Fiction)
# shelf1 = BookShelf([book1])
# book2 = Book("Another Book", author, 2022, Genre.Fiction)
# shelf2 = BookShelf([book2])
# library = Library()
# library.add_shelf(shelf1)
# library.add_shelf(shelf2)
# assert library.get_books() == [book1, book2]
# assert library.is_book_in_library(book1) is True
# assert library.is_book_in_library(Book("Non Existing Book", author, 2021, Genre.Fiction)) is False
# library.remove_shelf(shelf1)
# assert library.get_books() == [book2]
from .exercise_71 import Book, Genre
from .exercise_72 import BookShelf


class Library:
    # Add your code here.
    ...
