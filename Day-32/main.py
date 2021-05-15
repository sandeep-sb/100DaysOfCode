import smtplib

my_email = "sandeepsbhadouria@gmail.com"
my_password = "@sandeep99"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="sandeepsb04@yahoo.com",
                    msg="Subject: Mailing in Python\n\nThis is my first mail using Python")
connection.close()
