import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": "placeholder"
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
stock_data = [value for (key, value) in data.items()]

yesterday_price = stock_data[0]["4. close"]
before_yesterday_price = stock_data[1]["4. close"]
diff = float(yesterday_price) - float(before_yesterday_price)
diff_perc = round((diff/float(yesterday_price)) * 100, 2)
if diff_perc > 5:
  news_params = {
    "apiKey": "placeholder",
    "qInTitle": COMPANY_NAME,
  }
  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_response.json()["articles"][:3]
  formatted_articles = [f"{STOCK_NAME}: {diff_perc}%\nHeadline: {article['title']}.\nBrief:{article['description']}" for article in articles]

  client = Client("ID", "AUTH_TOKEN")
  for article in formatted_articles:
    message = client.messages.create(
      body=article,
      from_='number',
      to='number'
    )