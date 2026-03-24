import pandas as pd

def load_data(symbol,start,end):
    file_path = f"data/{symbol}_{start[:4]}_{end[:4]}_data.csv"
    data = pd.read_csv(file_path)
    
    # 1. Drop the first two rows (the extra headers)
    data = data.iloc[2:].copy()
    
    # 2. Reset the index so the first row is back to 0
    data.reset_index(drop=True, inplace=True)
    
    # 3. Convert the price columns from strings to numbers
    data['Close'] = data['Close'].astype(float)
    # You can do the same for High, Low, Open, Volume if you need them later!
    
    return data