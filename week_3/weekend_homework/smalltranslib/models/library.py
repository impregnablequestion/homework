from models.book import Book

book1 = Book("Paul takes the form of a mortal girl", "Andrea Lawlor", "Speculative fiction", False, "https://m.media-amazon.com/images/I/71HFLP3sZmL.jpg")
book2 = Book("People in Trouble", "Sarah Schulman", "Aids Memoir", False, "https://m.media-amazon.com/images/I/81e27xHrLTL.jpg")
book3 = Book("Lote", "Shola von Reinhold", "Fiction", True, "https://cdn.waterstones.com/bookjackets/large/9781/9130/9781913090111.jpg")
book4 = Book("Stone Butch Blues", "Leslie Feinberg", "Memoir", False, "https://m.media-amazon.com/images/I/413ZwlvjWiL.jpg")
book5 = Book("Detransition Baby", "Torrey Peters", "Fiction", False, "https://cdn.waterstones.com/bookjackets/large/9781/7881/9781788167222.jpg")
book6 = Book("Confessions of the Fox", "Jordy Rosenberg", "Historical Fiction", True, "https://cdn.waterstones.com/bookjackets/large/9781/7864/9781786496256.jpg")
book7 = Book("Testo Junkie", "Paul B. Preciado", "Memoir", False, "https://m.media-amazon.com/images/I/511Dw5e+BtL.jpg")
book8 = Book("The Transgender Issue", "Shon Faye", "Non-fiction", True, "https://cdn.penguin.co.uk/dam-assets/books/9780141991801/9780141991801-jacket-large.jpg")
book9 = Book("Nevada", "Imogen Binnie", "Fiction", True, "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1638827370l/58837536.jpg")
book10 = Book("Deep Wheel Orcadia", "Harry Josephine Giles", "Sci-fi", False, "https://m.media-amazon.com/images/I/91uEA3cY7fL.jpg")
book11 = Book("Tell Me I'm Worthless", "Alison Rumfitt", "Horror", False, "https://m.media-amazon.com/images/I/71cUZBaRP0S.jpg")
book12 = Book("Trans", "Juliet Jacques", "Memoir", False, "https://m.media-amazon.com/images/I/71ijxq-MNYL.jpg")
book13 = Book("We Both Laughed In Pleasure", "Lou Sullivan", "Diaries", True, "https://soupyweather.neocities.org/Screenshot%202022-11-26%20at%2018.02.27.png")
book14 = Book("Gender Explorers", "Juno Roche", "Theory", False, "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1580420542l/50725123.jpg")


book_list = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14]

def get_book(index):
    return book_list[index]

def add_book(book):
    book_list.append(book)

def remove_book(book):
    book_list.remove(book)

def update_checked_in(book):
    book.checked_out = not book.checked_out