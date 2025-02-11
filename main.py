import requests
from stock import Stock
from jsonUtils import get_stocks, write_value


def get_usd_to_cad_exchange_rate():
    api_key = "c94712ec8abe2fddc0f9f280"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cad_rate = data['conversion_rates']["CAD"]
        return cad_rate
    else:
        print("Error fetching rate:", response.status_code)
        return None

def get_portfolio_value(portfolio, usdExchangeRate):
    stocks = []
    country_codes = ["CAD", "USD"]
    for country_code in country_codes:
        for stock in portfolio[country_code]:
            stock_obj = Stock(stock, portfolio[country_code][stock], country_code)
            stocks.append(stock_obj)



    value = 0
    for stock in stocks:
        value += stock.get_value(usdExchangeRate)

    value += portfolio["CASH"]["CAD"]
    value += portfolio["CASH"]["USD"] * usdExchangeRate

    return value


def main():
    stocks = get_stocks()
    usd_exchange_rate = get_usd_to_cad_exchange_rate()
    value = get_portfolio_value(stocks, usd_exchange_rate)
    print(round(value,2))
    write_value(value)

if __name__ == "__main__":
    main()