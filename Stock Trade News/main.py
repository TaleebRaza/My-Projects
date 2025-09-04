import requests

class StockTradeNews:
    STOCK_NAME = ""

    STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    STOCK_ENDPOINT_API_KEY = "API KEY"
    NEWS_ENDPOINT_API_KEY = "API KEY"

    STOCK_API_ENDPOINT_PARAMETERS = {"function": "TIME_SERIES_DAILY",
                                     "symbol": STOCK_NAME,
                                     "apikey": STOCK_ENDPOINT_API_KEY}

    NEWS_API_ENDPOINT_PARAMETERS = {"apikey": NEWS_ENDPOINT_API_KEY,
                                    "q": "+Tesla +Stock",
                                    "sortBy": "relevancy",
                                    "pageSize": 10}

    def __init__(self):
        # self.yest_price, self.day_before_yest_price = self.get_stock_data()
        self.news = self.get_news_data()

    def get_stock_data(self):
        stock_response = requests.get(self.STOCK_API_ENDPOINT, params=self.STOCK_API_ENDPOINT_PARAMETERS)
        stock_response.raise_for_status()
        stock_response = stock_response.json()["Time Series (Daily)"]

        stock_data = [value for item, value in stock_response.items()][0:2]
        yest_price = float(stock_data[0]["4. close"])
        yest_plus_closing_price = float(stock_data[1]["4. close"])

        return yest_price, yest_plus_closing_price

    def get_news_data(self):
        news_response = requests.get(self.NEWS_ENDPOINT, params=self.NEWS_API_ENDPOINT_PARAMETERS)
        news_response.raise_for_status()
        news_response = news_response.json()["articles"][0:3]

        news_data = [f"Title: {article["title"]}\nBrief: {article["description"]}\n"for article in news_response]
        return news_data

    def print_news(self):
        percentage_difference = 20

        if abs(percentage_difference) >= 5.0:
            for article in self.news:
                print(article)

stock = StockTradeNews()
stock.print_news()