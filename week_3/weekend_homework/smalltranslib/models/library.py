from models.book import Book

book1 = Book("Paul takes the form of a mortal girl", "Andrea Lawlor", "Speculative fiction", False, "https://m.media-amazon.com/images/I/71HFLP3sZmL.jpg")
book2 = Book("People in Trouble", "Sarah Schulman", "Aids Memoir", False, "https://m.media-amazon.com/images/I/81e27xHrLTL.jpg")
book3 = Book("The Argonauts", "Maggie Nelson", "Auto-fiction", True, "https://m.media-amazon.com/images/I/51P6HXnhONL.jpg")
book4 = Book("Lote", "Shola von Reinhold", "Fiction", True, "https://cdn.waterstones.com/bookjackets/large/9781/9130/9781913090111.jpg")
book5 = Book("Stone Butch Blues", "Leslie Feinberg", "Memoir", False, "https://m.media-amazon.com/images/I/413ZwlvjWiL.jpg")
book6 = Book("Detransition Baby", "Torrey Peters", "Fiction", False, "https://cdn.waterstones.com/bookjackets/large/9781/7881/9781788167222.jpg")
book7 = Book("Confessions of the Fox", "Jordy Rosenberg", "Historical Fiction", True, "https://cdn.waterstones.com/bookjackets/large/9781/7864/9781786496256.jpg")

book_list = [book1, book2, book3, book4, book5, book6, book7]

def get_book(index):
    return book_list[index]

def add_book(book):
    book_list.append(book)

def remove_book(book):
    book_list.remove(book)

def update_checked_in(book):
    book.checked_out = not book.checked_out