import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)


# user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == "POST":
        email_entered = request.form.get("email")
        name_entered = request.form.get("name")
        password_entered = request.form.get("password")

        hashed_and_salted_password = generate_password_hash(password_entered, method="pbkdf2:sha256", salt_length=8)

        new_user = User()

        # check if user is already present in the database
        if User.query.filter_by(email=email_entered):
            flash("You've already signed-up with that email, log in instead.")
            return redirect(url_for("login"))
        else:
            new_user.email = email_entered
            new_user.name = name_entered
            new_user.password = hashed_and_salted_password
            db.session.add(new_user)
            db.session.commit()

        # login and authenticate user after adding details to the database
        login_user(new_user)

        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email_entered = request.form.get("email")
        password_entered = request.form.get("password")

        # find user by email entered
        user = User.query.filter_by(email=email_entered).first()

        # check if user with this email exists
        if user:

            # check stored password hash against entered password hash
            if check_password_hash(pwhash=user.password, password=password_entered):
                login_user(user)
                return redirect(url_for("secrets"))

            else:
                flash("Password incorrect, please try again.")

        else:
            flash("This email does not exists, please try again.")

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("login")


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static",
        filename="files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
