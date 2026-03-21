from indicators.sma import sma
from filters.regime import regime
def sma_crossover(d, fast_period, slow_period):
    fast_sma = sma('Close',fast_period,d)
    slow_sma = sma('Close', slow_period,d)
    fast = f'sma_{fast_period}'
    slow = f'sma_{slow_period}'
    
    d[fast] = fast_sma
    d[slow] = slow_sma
    
    signals = [0]
    
    regime_arr = regime(d, column_name=slow, lookback=10, threshold=0.05) 
    
    for i in range(1, len(d)):
        regimen = regime_arr[i]
        if d[fast].iloc[i] is None or d[slow].iloc[i] is None:
            signals.append(0)
        if ((d[fast].iloc[i-1] <= d[slow].iloc[i-1] and d[fast].iloc[i] > d[slow].iloc[i]) and (regimen == 1 or regimen == 0)):
            #Buy signal
            signals.append(1)
        elif ((d[fast].iloc[i-1] >= d[slow].iloc[i-1] and d[fast].iloc[i] < d[slow].iloc[i]) and (regimen == -1 or regimen == 0)):
            # Sell signal
            signals.append(-1)
        else:
            # Hold 
           signals.append(0)
    return signals

            

