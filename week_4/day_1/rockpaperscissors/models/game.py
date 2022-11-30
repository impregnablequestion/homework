class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1]
    
    def calculate_outcome(self):

        ints = {"rock":1, "paper":2, "scissors":3}
        p1choice = ints[self.player_1.choice]
        p2choice = ints[self.player_2.choice]

        if p1choice == p2choice:
            return 0
        elif p1choice == p2choice + 1 or p1choice == p2choice - 2:
            return 1
        elif p1choice == p2choice - 1 or p1choice == p2choice + 2:
            return 2
        else:
            return None

    def display_outcome(self):
        result = self.calculate_outcome()

        p1name = self.player_1.name
        p2name = self.player_2.name
        p1choice = self.player_1.choice
        p2choice = self.player_2.choice
    
        if result == 1:
            return f"you win!! {p1name} ({p1choice}) beats {p2name} ({p2choice})"
        if result == 2:
            return f"you lose!! {p2name} ({p2choice}) beats {p1name} ({p1choice})"
        if result == 0:
            return f"{p1name} and {p2name} draw with {p1choice}"
        if result == None:
            return "unexpected error"





