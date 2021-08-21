from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_api = "930bf3067f20d65c37483f809b2d5136"
movie_list = []

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
Bootstrap(app)
db = SQLAlchemy(app)


class addMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Movies %r>" % self.id


db.create_all()
# try:
#     new_movie = Movie(title="Phone Booth",
#                       year=2002,
#                       description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
#                                   "extortionist's sniper rifle. Unable to leave or receive outside help, "
#                                   "Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#                       rating=7.3,
#                       ranking=10,
#                       review="My favourite character was the caller.",
#                       img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
#
#     db.session.add(new_movie)
#     db.session.commit()
# except IntegrityError:
#     pass


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        movie_id = request.args.get('id')
        for movie in movie_list:
            if movie["id"] == movie_id:

                new_movie = Movie(title=movie["original_title"],
                                  year=movie["release_date"],
                                  description=movie["overview"],
                                  img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}")

                db.session.add(new_movie)
                db.session.commit()

    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        movie_id = request.form['movie-id']
        movie = Movie.query.get(movie_id)
        movie.rating = request.form['new_rating']
        movie.review = request.form['new_review']
        db.session.commit()
        return redirect(url_for("home"))

    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_be_deleted = Movie.query.get(movie_id)
    db.session.delete(movie_to_be_deleted)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_movie = addMovieForm()
    if request.method == "POST":
        parameter = {
            "api_key": TMDB_api,
            "query": add_movie.movie_title.data
        }
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameter)
        movie_list = response.json()['results']
        return render_template("select.html", movies=movie_list)
    return render_template("add.html", add_movie_form=add_movie)


if __name__ == '__main__':
    app.run(debug=True)
