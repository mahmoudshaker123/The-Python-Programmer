# Exercise 10_05 - Library Management System [Part 2/4]
# In the previous exercise, you defined the core classes for a library management system.
# In this exercise, you will implement the `BookShelf` class that will hold a collection of books.

# The `BookShelf` class should have the following methods:
# 1. `__init__(books: list[Book])`: Initialize the shelf with a list of books.
# 1. `add_book(book: Book)`: Add a book to the shelf.
# 2. `remove_book(book: Book)`: Remove a book from the shelf.
# 3. `get_books() -> List[Book]`: Return a list of all the books on the shelf.
# 4. `get_books_by_genre(genre: Genre) -> List[Book]`: Return a list of books by genre.

# Note: Define any additional methods or attributes that you think are necessary for the `Shelf` class.

# Example of the expected behavior:
# author = Author("John", "Doe")
# book1 = Book("The Book", author, 2021, Genre.Fiction)
# shelf = BookShelf([book1])
# book2 = Book("Another Book", author, 2022, Genre.Fiction)
# shelf.add_book(book2)
# assert shelf.get_books() == [book1, book2]
# assert shelf.get_books_by_genre(Genre.Fiction) == [book1, book2]


class BookShelf:
    # Add your code here.
    ...
