from flask import render_template, redirect, request
from app import app
from models.player import Player
from models.game import Game
import random
import pdb

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/submitform/', methods=["POST"])
# def play_game():
#     rps=["rock", "paper","scissors"]
#     results=request.form
#     username=results["player_name"]
#     userchoice=results["choice"]
#     user_player = Player(username, userchoice)
#     computerchoice=random.choice(rps)
#     computer_player = Player("séamus", computerchoice)
#     game = Game(user_player, computer_player)
#     outcome = game.display_outcome()
#     return render_template(
#         'result.html',
#         outcome = outcome,
#         userchoice = userchoice, 
#         computerchoice = computerchoice
#         )

#sneaky version
@app.route('/submitform/', methods=["POST"])
def play_game():
    rps=["rock", "paper","scissors"]
    results=request.form
    username=results["player_name"]
    userchoice=results["choice"]
    user_player = Player(username, userchoice)
    compchoice = user_player.computer_choice(userchoice)
    computer_player = Player("séamus", compchoice)
    game = Game(user_player, computer_player)
    outcome = game.display_outcome()
    return render_template(
        'result.html',
        outcome = outcome,
        userchoice = userchoice, 
        computerchoice = compchoice
        )



    



