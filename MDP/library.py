class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True

class Patron:
    def __init__(self,name):
         self.name=name
         self.borrowed_books=[]

class Library:
    def __init__(self):
        self.books=[]
        self.patrons=[]
        
    def add_book(self,book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self,patron,book):
        if book.available:
            book.available=False
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print(f"{patron.name} did not borrow '{book.title}'.")

library = Library()

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Alice Brown")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron("Rahul")
library.register_patron(patron1)

library.borrow_book(patron1, book1)
library.return_book(patron1, book1)


