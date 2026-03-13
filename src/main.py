from download_data import download_data
from load_data import load_data
from strategies.buy_hold import buy_hold
from indicators.sma import sma
import os

symbol = "AAPL"
start_date = "2021-03-12"
end_date = "2026-03-12"

file_path = "data/" + symbol + "_5y_data.csv"

if not os.path.exists(file_path):
    download_data(symbol, start_date, end_date)

data = load_data(symbol)
smaArr = sma('Close',50,data)

data['SMA_50'] = smaArr

# Round the values to 2 decimal places for cleaner reading
data['SMA_50'] = data['SMA_50'].round(2)

# Print the last 10 rows to see the alignment of Price and SMA
print(data[['Close', 'SMA_50']].tail(10))