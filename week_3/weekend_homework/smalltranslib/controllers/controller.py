from flask import render_template, redirect, request
from app import app
from models.library import book_list, add_book
from models.book import Book

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/library/')
def library():
    return render_template("library.html", library = book_list)

@app.route('/library/donate/')
def donate():
    return render_template("donate.html")

@app.route('/library/', methods=["POST"])
def donatebook():
    data = request.form
    book_name = data["book_name"]
    book_author = data["book_author"]
    book_genre = data["book_genre"]
    new_book = Book(book_name, book_author, book_genre, False)
    add_book(new_book)

    return redirect('/library/')
