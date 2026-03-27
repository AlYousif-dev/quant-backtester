import streamlit as st
import os
import pandas as pd
from data_processes.download_data import download_data
from data_processes.load_data import load_data
from strategies.sma_crossover import sma_crossover
from strategies.buy_hold import buy_hold
from backtester.engine import run_backtest

# 1. Page Configuration
st.set_page_config(page_title="Quant Backtester", layout="wide")
st.title("📈 Algorithmic Backtester")

# 2. Build the Sidebar (Replaces your input() questions)
st.sidebar.header("Backtest Parameters")

sym = st.sidebar.text_input("What Symbol?", value="AAPL").upper()
start = st.sidebar.text_input("Start Date (YYYY-MM-DD)", value="2020-01-01")
end = st.sidebar.text_input("End Date (YYYY-MM-DD)", value="2023-01-01")
bankroll = st.sidebar.number_input("What is your Bankroll?", value=10000, step=1000)

strategy_choice = st.sidebar.selectbox("Which Strategy?", ["Buy/Hold", "SMA Crossover"])

# Show SMA inputs ONLY if SMA is selected
if strategy_choice == "SMA Crossover":
    fast = st.sidebar.number_input("Fast Period", min_value=1, value=10)
    slow = st.sidebar.number_input("Slow Period", min_value=1, value=50)

# 3. The Execution Button
if st.sidebar.button("Run Backtest"):
    
    # st.spinner gives the user visual feedback while data downloads
    with st.spinner(f"Fetching data for {sym}..."):
        
        # Note: If your 'data' folder is outside 'src', you may need to use '../data/...'
        file_path = f"data/{sym}_{start[:4]}_{end[:4]}_data.csv"

        if not os.path.exists(file_path):
            download_data(sym, start, end)

        data = load_data(sym, start, end)
        st.success("Data loaded successfully!")

    # Run the selected strategy
    with st.spinner("Running strategy engine..."):
        if strategy_choice == "Buy/Hold":
            result = buy_hold(int(bankroll), data)
            st.write("### Strategy Results")
            st.write(result) # Streamlit will auto-format this output
            
        elif strategy_choice == "SMA Crossover":
            signals = sma_crossover(data, int(fast), int(slow))
            result = run_backtest(data, signals, int(bankroll))
            st.write("### Strategy Results")
            st.write(result)