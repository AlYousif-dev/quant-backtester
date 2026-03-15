import yfinance as yf

def download_data(symbol,start_date, end_date):
    #Fetch data from Yahoo Finance
    data = yf.download(symbol,start=start_date,end= end_date)
    #Store data as a CSV file
    data.to_csv("data/"+symbol+"_5y_data.csv")