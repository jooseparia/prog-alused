"""Book store."""


class Book:
    """Represents a book with title, author, price, and rating."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """Initialize a book with the provided attributes."""
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represents a book store with a name, rating, and a collection of books."""

    def __init__(self, name: str, rating: float):
        """Initialize a store with the provided name and rating."""
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """Check if a book can be added to the store based on its rating."""
        for existing_book in self.books:
            if existing_book.title == book.title and existing_book.author == book.author:
                return False  # Book with the same title and author already exists
        return book.rating >= self.rating

    def add_book(self, book: Book):
        """Add a book to the store if it meets the criteria."""
        if self.can_add_book(book):
            self.books.append(book)
            print(f"Book '{book.title}' by {book.author} added to {self.name}.")
        else:
            print(f"Cannot add book '{book.title}' to {self.name}.")

    def can_remove_book(self, book: Book) -> bool:
        """Check if a book can be removed from the store."""
        return book in self.books

    def remove_book(self, book: Book):
        """Remove a book from the store if it exists."""
        if self.can_remove_book(book):
            self.books.remove(book)
            print(f"Book '{book.title}' removed from {self.name}.")
        else:
            print(f"Book '{book.title}' is not in {self.name}.")

    def get_all_books(self):
        """Get a list of all books in the store."""
        return self.books

    def get_books_by_price(self):
        """Get a list of books sorted by price."""
        return sorted(self.books, key=lambda x: x.price)

    def get_most_popular_book(self):
        """Get the most popular book(s) in the store based on rating."""
        if not self.books:
            return None

        max_rating = max(book.rating for book in self.books)
        most_popular_books = [book for book in self.books if book.rating == max_rating]
        return most_popular_books
