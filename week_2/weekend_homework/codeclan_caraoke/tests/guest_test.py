import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Dave")
        self.guest2 = Guest("Lewis")
        self.guest3 = Guest("Natasha")

    def test_guest_has_name(self):
        output = self.guest1.name 
        self.assertEqual(output, "Dave")