from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style= "text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


def make_bold(fun):
    fun = "<b>"


make_bold()


@app.route("/bye")
@make_bold
def bye():
    return "bye!!"


@app.route('/username/<path:name>')
def greet(name):
    return f'Hello there {name}'


if __name__ == "__main__":
    app.run(debug=True)
