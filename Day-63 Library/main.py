from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL,"
# #                " author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///new-books-collection.db'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SECRET_KEY"] = "My library project"
db = SQLAlchemy(app)

# Create Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


# Create Record
# new_book = Book(id=1, title="Murder On the Orient Express", author="Agatha Christie", rating=9.6)
# db.session.add(new_book)
# db.session.commit()

# Read all the data
# all_books_data = Book.query.all()

# Read data by using particular query
# read = Book.query.filter_by(title="Hercule Poirot").first()
# print(read.rating)

# Update record using particular query
# update_record = Book.query.filter_by(title="Hercule Poirot").first()
# update_record.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# Upadte Record using primary key
# book_to_update = Book.query.get(1)
# book_to_update.title = "Hercule Poirot"
# db.session.commit()

# Delete a record by primary key
# rec_del = Book.query.get(1)
# db.session.delete(rec_del)
# db.session.commit()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        print(request.form)
        try:
            new_book = Book(title=request.form["title"],
                            author=request.form["author"],
                            rating=request.form['rating']
                            )
            db.session.add(new_book)
            db.session.commit()
        except IntegrityError:  # this is done so that titles and authors are not repeated.
            return redirect(url_for("add"))
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        update_record = Book.query.get(book_id)
        update_record.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("book_id")
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get("book_id")
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
