# src/filters/regime.py

def regime(data, column_name, lookback=10, threshold=0.5):
    """
    Calculates the market regime based on the daily ROI of a specific column.
    """
    regime_arr = []
    
    for i in range(len(data)):
        if i < lookback:
            regime_arr.append(0)
            continue
            
        # Use the passed column_name directly
        price_new = data[column_name].iloc[i]
        price_old = data[column_name].iloc[i - lookback]
        
        if price_old is None or price_new is None or price_old == 0:
            regime_arr.append(0)
            continue
            
        slope = (price_new - price_old) / lookback
        daily_roi = (slope / price_old) * 100
        
        if daily_roi > threshold:
            regime_arr.append(1)
        elif daily_roi < -threshold:
            regime_arr.append(-1)
        else:
            regime_arr.append(0)
            
    return regime_arr