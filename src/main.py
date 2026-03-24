from data_processes.download_data import download_data
from data_processes.load_data import load_data
from strategies.sma_crossover import sma_crossover
from strategies.buy_hold import buy_hold
from indicators.sma import sma
from backtester.engine import run_backtest
import pandas as pd
import itertools
import os
import time
flag = True
while flag:

    print('What Symbol?')
    sym = input().strip()

    print('What Start Date? (YYYY-MM-DD)')
    start = input().strip()

    print('What End Date? (YYYY-MM-DD)')
    end = input().strip()
    
    print(f"Fetching data for {sym}")
    file_path = f"data/{sym}_{start[:4]}_{end[:4]}_data.csv"

    if not os.path.exists(file_path):
        download_data(sym,start,end)

    data = load_data(sym,start,end)

    print("What is your Bankroll?")
    bankroll_in = input()

    print("Which Strategy would you like to run? 1: Buy/Hold; 2 SMA Crossover")
    strategy_choice = input()

    if int(strategy_choice) == 1:
        print(buy_hold(int(bankroll_in),data))
    elif int(strategy_choice) == 2:

        print("Fast Period?")
        fast = input()

        print("Slow Period?")
        slow = input()

        print('Fetching Signals...')
        signals = sma_crossover(data,int(fast),int(slow))
        print("Done!")

        print("Running Backtest...")
        print(run_backtest(data,signals,int(bankroll_in)))
    print('Want to run another backtest? 1 for yes; 2 for no;')
    choice = input()
    if(int(choice) != 1):
        flag = False
