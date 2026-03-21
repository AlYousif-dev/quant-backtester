from data_processes.download_data import download_data
from data_processes.load_data import load_data
from strategies.sma_crossover import sma_crossover
from indicators.sma import sma
from backtester.engine import run_backtest
import pandas as pd
import itertools
import os
import time

symbol = "AAPL"
start_date = "2011-03-12"
end_date = "2026-03-12"
initial_capital = 100000

file_path = f"data/{symbol}_5y_data.csv"

if not os.path.exists(file_path):
    download_data(symbol, start_date, end_date)

data = load_data(symbol)

# Establish Macro Environment 
macro_period = 200
macro_col = f'SMA_{macro_period}'
data[macro_col] = sma('Close', macro_period, data)

# Tests everything from hyper-fast scalping (2/10) to deep macro trends (50/250)
fast_range = range(2, 52, 2)     # 2, 4, 6... 50
slow_range = range(10, 260, 10)  # 10, 20, 30... 250


# ==========================================

# Generate all valid combinations where fast < slow
valid_combos = [(f, s) for f, s in itertools.product(fast_range, slow_range) if f < s]
total_runs = len(valid_combos)

print(f"Executing parameter sweep across {total_runs} valid combinations...")

results = []
start_time = time.time()

for idx, (fast, slow) in enumerate(valid_combos, 1):
    # Print progress every 100 iterations
    if idx % 100 == 0 or idx == total_runs:
        print(f"Processing {idx}/{total_runs} combinations...")
        
    signals = sma_crossover(data, fast, slow) 
    profit = run_backtest(data, signals, initial_capital)
    
    results.append({
        'Fast_SMA': fast,
        'Slow_SMA': slow,
        'Net_Profit': round(profit, 2),
        'Return_Pct': round((profit / initial_capital) * 100, 2)
    })

elapsed = time.time() - start_time
print(f"\nSweep completed in {elapsed:.2f} seconds.")

results_df = pd.DataFrame(results)
top_combos = results_df.sort_values(by='Net_Profit', ascending=False).head(20)

print("\n--- Top 20 SMA Combinations ---")
print(top_combos.to_string(index=False))

# Export the entire landscape to a CSV so you can graph the 3D surface later
results_df.to_csv("data/optimization_results.csv", index=False)
print("\nFull optimization landscape saved to data/optimization_results.csv")