import yfinance as yf

def download_data(symbol,start_date, end_date):
    data = yf.download(symbol,start=start_date,end= end_date)
    data.to_csv("data/"+symbol+"_5y_data.csv")