from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(f):
    def wrapper():
        return f"<em>{f()}</em>"

    return wrapper


def make_underlined(fun):
    def wrapper():
        return f"<u>{fun()}</u>"

    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style= "text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!!"


@app.route('/username/<path:name>')
def greet(name):
    return f'Hello there {name}'


if __name__ == "__main__":
    app.run(debug=True)
