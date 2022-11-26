import unittest
from models.book import Book
from models.library import get_book, add_book, remove_book, book_list, book1, update_checked_in

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Paul takes the form of a mortal girl", "Andrea Lawlor", "Speculative fiction", False, "https://m.media-amazon.com/images/I/71HFLP3sZmL.jpg")
        self.book2 = Book("People in Trouble", "Sarah Schulman", "Aids Memoir", False, "https://m.media-amazon.com/images/I/81e27xHrLTL.jpg")
        self.book3 = Book("The Argonauts", "Maggie Nelson", "Auto-fiction", True, "https://m.media-amazon.com/images/I/51P6HXnhONL.jpg")
        self.book4 = Book("Lote", "Shola von Reinhold", "Fiction", True, "https://cdn.waterstones.com/bookjackets/large/9781/9130/9781913090111.jpg")
        self.book5 = Book("Stone Butch Blues", "Leslie Feinberg", "Memoir", False, "https://m.media-amazon.com/images/I/413ZwlvjWiL.jpg")
        self.book6 = Book("Detransition Baby", "Torrey Peters", "Fiction", False, "https://cdn.waterstones.com/bookjackets/large/9781/7881/9781788167222.jpg")
        self.book7 = Book("Confessions of the Fox", "Jordy Rosenberg", "Historical Fiction", True, "https://cdn.waterstones.com/bookjackets/large/9781/7864/9781786496256.jpg")

        self.book_list = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]

    def test_book_has_title(self):
        self.assertEqual(self.book1.title, "Paul takes the form of a mortal girl")  
    
    def test_book_has_author(self):
        self.assertEqual(self.book1.author, "Andrea Lawlor") 

    def test_book_has_genre(self):
        self.assertEqual(self.book1.genre, "Speculative fiction") 

    def test_book_has_thumbnail(self):
        self.assertEqual(self.book1.thumbnail_url, "https://m.media-amazon.com/images/I/71HFLP3sZmL.jpg") 
    
    def test_book_has_checked_out_value(self):
        self.assertEqual(self.book1.checked_out, False)

    def test_get_book_by_index(self):
        output = get_book(0)
        self.assertEqual(output.title, self.book1.title)

    def test_add_book_to_list(self):
        add_book(self.book7)
        output = book_list[14]
        self.assertEqual(output.title, self.book7.title)

    def test_remove_book_from_list(self):
        remove_book(book1)
        self.assertEqual(len(book_list), 14)

    def test_update_checked_in(self):
        update_checked_in(self.book1)
        self.assertEqual(self.book1.checked_out, True)



