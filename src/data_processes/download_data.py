import yfinance as yf
import os

def download_data(symbol, start_date, end_date):
    # Fetch data from Yahoo Finance
    data = yf.download(symbol, start=start_date, end=end_date)
    
    # Ensure the 'data' directory exists before attempting to save
    os.makedirs("data", exist_ok=True)
    
    # Store data as a CSV file
    data.to_csv(f"data/{symbol}_{start_date[:4]}_{end_date[:4]}_data.csv")