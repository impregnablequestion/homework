from flask import render_template, redirect, request
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def index():
    return render_template("index.html")