import requests
import os
from twilio.rest import Client

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_param = {
    'apikey': 'MNXBHO454ABOXOVS',
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
}

news_param = {
    'apiKey': '872cf0d904ba4291935c55ec7fc2e58b',
    'q': COMPANY_NAME,
    'from': '2021-05-20',
    'to': '2021-05-19',
    'url': STOCK_ENDPOINT,
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_param)
news_response.raise_for_status()
articles = news_response.json()['articles']
three_articles = articles[0:3]

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_param)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday_closing = float(stock_data['Time Series (Daily)']['2021-05-20']['4. close'])
day_b4_closing = float(stock_data['Time Series (Daily)']['2021-05-19']['4. close'])
change_percent = round(((yesterday_closing - day_b4_closing) / yesterday_closing) * 100)

change = None
if change_percent < 0:
    change = '🔻'
else:
    change = '🔺'

if abs(change_percent) < 5:
    client = Client(account_sid, auth_token)

    formatted_article = [
        f"{STOCK}: {change}{abs(change_percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles]

    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+15302035853',
            to=os.environ['PHONE_NUMBER']
        )
