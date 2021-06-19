import requests
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_text = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get("href")
    article_link.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_score = max(article_upvote)
largest_index = article_upvote.index(largest_score)

print(article_text[largest_index])
print(article_link[largest_index])








# import lxml
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# print(soup.p)
