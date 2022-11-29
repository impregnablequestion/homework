class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1]
    
    def calculate_outcome(self):
        p1name = self.player_1.name
        p1choice = self.player_1.choice
        p2name = self.player_2.name
        p2choice = self.player_2.choice
        
        ints = {"rock":1, "paper":2, "scissors":3}

        if self.player_1.choice == self.player_2.choice:
            return "draw"
        elif ints[self.player_1.choice] == ints[self.player_2.choice] + 1: #player1 is rock/paper and player2 is paper/scissors
            return f"{self.player_1.name} ({self.player_1.choice}) beats {self.player_2.name} ({self.player_2.choice})"

        elif ints[self.player_1.choice]== ints[self.player_2.choice] - 1: #player2 is rock/paper and player1 is paper/scissors
            return f"{self.player_2.name} ({self.player_2.choice}) beats {self.player_1.name} ({self.player_1.choice})"

        elif ints[self.player_1.choice] == ints[self.player_2.choice] - 2: #player 1 is rock and player_2 is scissors
            return f"{self.player_1.name} ({self.player_1.choice}) beats {self.player_2.name} ({self.player_2.choice})"

        elif ints[self.player_1.choice] == ints[self.player_2.choice] + 2: #player 1 is scissors and player_2 is rock
            return f"{self.player_2.name} ({self.player_2.choice}) beats {self.player_1.name} ({self.player_1.choice})"
        
        else:
            return "unexpected input"

    def display_outcome(self):
        result = self.calculate_outcome()
        if result == player_1:
            return f""


