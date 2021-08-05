from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/dbecbee1d9f5685aaa7b"
blog_response = requests.get(BLOG_URL)
all_posts = blog_response.json()

app = Flask(__name__)


@app.route("/")
def go_to_home():
    return render_template("index.html", blogs=all_posts)


@app.route("/about")
def go_to_about():
    return render_template("about.html")


@app.route("/contact")
def go_to_contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def go_to_post(index):
    for post in all_posts:
        if post['id'] == index:
            return render_template("post.html", clicked_post=post)


if __name__ == "__main__":
    app.run(debug=True)
