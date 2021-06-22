import smtplib
import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com/PICTEK-Mechanical-Keyboard-Equivalent-Anti-Ghosting/dp/B07VNQQZFK/ref=sr_1_1_sspa?crid=18G5JIMTOCN9I&dchild=1&keywords=mechanical+keyboard&qid=1624366472&sprefix=mechanical+key%2Caps%2C409&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExM0RTSTVDT0hWRFJYJmVuY3J5cHRlZElkPUEwMzg2NTY0TzAyRVlBV1VQQzEmZW5jcnlwdGVkQWRJZD1BMDYyNTAyNDE0QzI1MEw2TjdISDImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.106 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
}
response = requests.get(url=product_url, headers=header)
website_tag = response.text
soup = BeautifulSoup(website_tag, "html.parser")
product_price = soup.find("span", id="priceblock_ourprice").getText()
product_price = float(product_price.split("$")[1])
product_title = soup.find("span", id="productTitle").getText()
print(product_price)
print(product_title)
print(product_url)

if product_price < 24.00:
    my_email = "sandeepsbhadouria@gmail.com"
    password = "**********"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr="sandeepsb04@yahoo.com",
        to_addrs=my_email,
        msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now ${product_price} \n {product_url}."
    )
    connection.close()
