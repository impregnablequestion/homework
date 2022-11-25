from flask import render_template, redirect
from app import app
from models.library import book_list
from models.book import Book

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/library/')
def library():
    return render_template("library.html", library = book_list)

@app.route('/library/donate')