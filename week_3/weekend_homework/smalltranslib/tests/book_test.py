import unittest
from models.book import Book
from models.library import get_book, add_book, remove_book, book_list, book1, update_checked_in

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Paul takes the form of a mortal girl", "Andrea Lawlor", "Speculative fiction", False)
        self.book2 = Book("People in Trouble", "Sarah Schulman", "Aids Memoir", False)
        self.book3 = Book("The Argonauts", "Maggie Nelson", "Auto-fiction", True)
        self.book4 = Book("Lote", "Shola von Reinhold", "Fiction", True)
        self.book5 = Book("Stone Butch Blues", "Leslie Feinberg", "Memoir", False)
        self.book6 = Book("Detransition Baby", "Torrey Peters", "Fiction", False)
        self.book7 = Book("Confessions of the Fox", "Jordy Rosenberg", "Historical Fiction", True)

        self.book_list = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]

    def test_book_has_title(self):
        self.assertEqual(self.book1.title, "Paul takes the form of a mortal girl")  
    
    def test_book_has_author(self):
        self.assertEqual(self.book1.author, "Andrea Lawlor") 

    def test_book_has_genre(self):
        self.assertEqual(self.book1.genre, "Speculative fiction")  
    
    def test_book_has_checked_out_value(self):
        self.assertEqual(self.book1.checked_out, False)

    def test_get_book_by_index(self):
        output = get_book(0)
        self.assertEqual(output.title, self.book1.title)

    def test_add_book_to_list(self):
        add_book(self.book7)
        output = get_book(6)
        self.assertEqual(output.title, self.book7.title)

    def test_remove_book_from_list(self):
        remove_book(book1)
        self.assertEqual(len(book_list), 7)

    def test_update_checked_in(self):
        update_checked_in(self.book1)
        self.assertEqual(self.book1.checked_out, True)

