import unittest
from models.player import Player


class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player = Player("dave", "rock")

    def test_player_has_name(self):
        self.assertEqual(self.player.name, "dave")

    def test_player_has_choice(self):
        self.assertEqual(self.player.choice, "rock")
