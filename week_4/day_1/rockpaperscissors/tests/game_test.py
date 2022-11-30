import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("dave", "rock")
        self.player_2 = Player("niall", "paper")
        self.player_3 = Player("francis", "paper")
        self.player_4 = Player("saoirse", "scissors")
        self.game_1 = Game(self.player_1, self.player_2) #paper beats rock
        self.game_2 = Game(self.player_2, self.player_3) #draw
        self.game_3 = Game(self.player_1, self.player_4) #rock beats scissors
        self.game_4 = Game(self.player_4, self.player_2) #scissors beats paper

    def test_game_has_player1(self):
        self.assertEqual(self.game_1.player_1.name, self.player_1.name)

    def test_game_has_player2(self):
        self.assertEqual(self.game_1.player_2.name, self.player_2.name)

    def test_calculate_outcome_draw(self):
        output = self.game_2.display_outcome()
        self.assertEqual(output, "niall and francis draw with paper")

    def test_calculate_outcome_rock_beats_scissors(self):
        output = self.game_3.display_outcome()
        self.assertEqual(output, "dave (rock) beats saoirse (scissors)")

    def test_calculate_outcome_paper_beats_rock(self):
        output = self.game_1.display_outcome()
        self.assertEqual(output, "niall (paper) beats dave (rock)")

    def test_calculate_outcome_scissors_beats_paper(self):
        output = self.game_4.display_outcome()
        self.assertEqual(output, "saoirse (scissors) beats niall (paper)")

        # write tests for player position switched (pain in ass)