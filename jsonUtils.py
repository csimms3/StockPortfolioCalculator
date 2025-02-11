from datetime import datetime
import json

def get_stocks():
    with open("./stocks.json","r") as stocks:
        stock_data = json.load(stocks)
    return stock_data

def write_value(value):
    with open("./portfolioValue.json", "r") as file:
        portfolio_data = json.load(file)

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "value": round(value, 2)
    }

    portfolio_data.append(entry)

    with open("./portfolioValue.json", "w") as file:
        json.dump(portfolio_data, file, indent=4)

