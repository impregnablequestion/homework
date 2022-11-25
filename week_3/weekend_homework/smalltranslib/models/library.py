from models.book import Book

book1 = Book("Paul takes the form of a mortal girl", "Andrea Lawlor", "Speculative fiction", False)
book2 = Book("People in Trouble", "Sarah Schulman", "Aids Memoir", False)
book3 = Book("The Argonauts", "Maggie Nelson", "Auto-fiction", True)
book4 = Book("Lote", "Shola von Reinhold", "Fiction", True)
book5 = Book("Stone Butch Blues", "Leslie Feinberg", "Memoir", False)
book6 = Book("Detransition Baby", "Torrey Peters", "Fiction", False)
book7 = Book("Confessions of the Fox", "Jordy Rosenberg", "Historical Fiction", True)

book_list = [book1, book2, book3, book4, book5, book6, book7]

def get_book(index):
    return book_list[index]

def add_book(book):
    book_list.append(book)

def remove_book(book):
    book_list.remove(book)

def update_checked_in(book):
    book.checked_out = not book.checked_out