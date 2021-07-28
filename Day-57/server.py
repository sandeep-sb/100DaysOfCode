from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_num = random.randint(1, 10)
    year = datetime.datetime.now()
    return render_template("index.html", num=random_num, year=year.strftime("%Y"))


@app.route("/guess/<input_name>")
def guess(input_name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={input_name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_response = requests.get(url=f"https://api.agify.io?name={input_name}")
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess_name_age.html", name=input_name, age=age, gender=gender)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(url=blog_url)
    blog_post = response.json()
    return render_template("blog.html", blogs=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
