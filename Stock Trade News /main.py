# Constants
import requests
from dateutil.utils import today

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWs_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_ENDPOINT_API_KEY = "R18OQQGKQJO7CQ8D" 
NEWS_ENDPOINT_API_KEY = "238af1d7e8844fbe9c2a0769339e2d41"

STOCK_API_ENDPOINT_PARAMETERS = {"function": "TIME_SERIES_DAILY",
                                 "symbol": STOCK_NAME,
                                 "apikey": STOCK_ENDPOINT_API_KEY}

NEWS_API_ENDPOINT_PARAMETERS = {"apikey": NEWS_ENDPOINT_API_KEY,
                                "q": "+Tesla +Stock",
                                "sortBy": "relevancy",
                                "pageSize": 10}

# Getting Responses
stock_response = requests.get(STOCK_API_ENDPOINT, params=STOCK_API_ENDPOINT_PARAMETERS)
stock_response.raise_for_status()
stock_response = stock_response.json()["Time Series (Daily)"]

news_response = requests.get(NEWs_ENDPOINT, params=NEWS_API_ENDPOINT_PARAMETERS)
news_response.raise_for_status()
news_response = news_response.json()

# print(news_response)
# print(stock_response)

# Collecting Data To Work With
stock_data = [value for key, value in stock_response.items()]