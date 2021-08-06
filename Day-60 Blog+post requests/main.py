from flask import Flask, render_template, request
import requests
import smtplib

my_email = "gmail"
my_password = "password"
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


@app.route("/contact", methods=['GET', 'POST'])
def go_to_contact():
    if request.method == 'POST':
        data = request.form
        print(data['username'])
        print(data['email'])
        print(data['phone'])
        print(data['msg'])
        with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="sandeepsb04@yahoo.com",
                                msg=f"Subject: New Mail\n\n"
                                    f"\nName: {data['username']}"
                                    f"\nemail: {data['email']}"
                                    f"\nPhone Number: {data['phone']}"
                                    f"\nMessage: {data['msg']}")

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def go_to_post(index):
    for post in all_posts:
        if post['id'] == index:
            return render_template("post.html", clicked_post=post)


if __name__ == "__main__":
    app.run(debug=True)
