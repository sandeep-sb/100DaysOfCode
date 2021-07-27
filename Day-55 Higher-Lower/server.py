from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"


@app.route("/<int:guess>")
def number_entered(guess):
    if guess < random_num:
        return "<h1 style='color:Red;'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/9C1nyePnovqlpEYFMD/giphy.gif' />"

    elif guess > random_num:
        return "<h1 style='color:Purple;'>Too high, try again!!</h1>" \
               "<img src='https://media.giphy.com/media/JEVqknUonZJWU/giphy.gif' />"

    else:
        return "<h1 style='color:Green'>You found me!!!</h1>" \
               "<img src='https://media.giphy.com/media/jp2KXzsPtoKFG/giphy.gif' />"


if __name__ == "__main__":
    app.run(debug=True)
