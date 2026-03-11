from download_data import download_data
from load_data import load_data
from strategies.buy_hold import buy_hold
import os

symbol = "AAPL"
start_date = "2021-09-21"
end_date = "2026-09-21"

file_path = "data/" + symbol + "_5y_data.csv"

if not os.path.exists(file_path):
    download_data(symbol, start_date, end_date)

data = load_data(symbol)
print(data['Close'].iloc[0],data["Close"].iloc[-1])

print(buy_hold(10000,d=data))