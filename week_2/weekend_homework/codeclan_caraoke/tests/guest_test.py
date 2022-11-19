import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Dave", 50.00, "Angels")
        self.guest2 = Guest("Lewis", 45.00, "Song 2")
        self.guest3 = Guest("Natasha", 75.00, "Sweet Caroline")

    def test_guest_has_name(self):
        output = self.guest1.name 
        self.assertEqual(output, "Dave")

    def test_guest_has_money(self):
        output = self.guest1.wallet
        self.assertEqual(output, 50.00)

    def test_cheer_function(self):
        output = self.guest1.cheer()
        self.assertEqual(output, "Banger!!!")