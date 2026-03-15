from data_processes.download_data import download_data
from data_processes.load_data import load_data
from strategies.buy_hold import buy_hold
from strategies.sma_crossover import sma_crossover
from indicators.sma import sma
from backtester.engine import run_backtest
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
# SMA ranges for testing
fast_range = range(1, 30, 1)    # 5, 10, 15, ...
slow_range = range(2, 60, 2) # 10, 20, 30, ...

best_profit = -99999999
best_combo = (0, 0)

for fast in fast_range:
    for slow in slow_range:
        if slow <= fast:
            continue  # skip invalid combos
        signals = sma_crossover(data, fast, slow)
        profit = run_backtest(data, signals, 100000)
        print(f"Fast: {fast}, Slow: {slow}, Profit: {profit:.2f}")
        if profit > best_profit:
            best_profit = profit
            best_combo = (fast, slow)

print(f"\nBest SMA combo: Fast={best_combo[0]}, Slow={best_combo[1]}, Profit={best_profit:.2f}")