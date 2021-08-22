from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_api = "930bf3067f20d65c37483f809b2d5136"
URL = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)


class addMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class rateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5")
    review = StringField(label="Your Review")
    submit = SubmitField(label="Done")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(300), nullable=True)
    img_url = db.Column(db.String, nullable=False)


db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    rate_form = rateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)

    if rate_form.validate_on_submit():
        movie.rating = float(rate_form.rating.data)
        movie.review = rate_form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=rate_form)


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
    if add_movie.validate_on_submit():
        parameter = {
            "api_key": TMDB_api,
            "query": add_movie.movie_title.data
        }
        response = requests.get(url=URL, params=parameter)
        movie_list = response.json()['results']
        return render_template("select.html", movies=movie_list)
    return render_template("add.html", add_movie_form=add_movie)


@app.route("/find")
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        parameters = {
            "api_key": TMDB_api
        }
        response = requests.get(url=url, params=parameters)
        data = response.json()
        new_movie = Movie(title=data["original_title"],
                          year=data["release_date"].split("-")[0],
                          description=data["overview"],
                          img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}")
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
