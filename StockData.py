import yfinance as yf

# Downloading the data
data = yf.download("AAPL", period="5y", interval="1d")
# Displaying the first and last few rows

print(data[['Open','High','Low','Close']].head())

data.to_csv("data/apple_5y_data.csv")

