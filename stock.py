import yfinance

class Stock:
    def __init__(self, ticker, num_shares, currency):
        self.ticker = ticker
        self.num_shares = num_shares
        self.currency = currency

    def __str__(self):
        return f"{self.currency} Stock \'{self.ticker}\', {self.num_shares} shares"

    def get_value(self, USDExchangeRate):
        stock_data = yfinance.Ticker(self.ticker).info
        stock_close = stock_data["regularMarketPreviousClose"]
        value = stock_close * self.num_shares

        if self.currency != "CAD":
            value *= USDExchangeRate

        return value
