class Player:
    
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
    
    def computer_choice(self, userchoice):
        if userchoice == "rock":
            return "paper"
        elif userchoice == "paper":
            return "scissors"
        elif userchoice == "scissors":
            return "rock"
        else:
            return None