from game import Game
from player import Player

player_1 = Player("dave", "scissors")
player_2 = Player("niall", "scissors")
game = Game(player_1, player_2)

print(game.calculate_outcome())