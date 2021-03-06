from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/ed99320662742443cc5b"
posts = requests.get(blog_url).json()
all_posts = []
for post_ in posts:
    post_obj = Post(post_['id'], post_['title'], post_['subtitle'], post_['body'])
    all_posts.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=all_posts)


@app.route("/post/<int:index>")
def posts(index):
    requested_post = 0
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
