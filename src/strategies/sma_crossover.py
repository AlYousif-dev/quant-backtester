from indicators.sma import sma

def sma_crossover(d, fast_period, slow_period):
    fast_sma = sma('Close',fast_period,d)
    slow_sma = sma('Close', slow_period,d)
    fast = f'sma_{fast_period}'
    slow = f'sma_{slow_period}'
    d[fast] = fast_sma
    d[slow] = slow_sma
    signals = [0]
    for i in range(1,len(d)):
        if d[fast].iloc[i] is None or d[slow].iloc[i] is None:
            signals.append(0)
        if (d[fast].iloc[i-1] <= d[slow].iloc[i-1] and d[fast].iloc[i] > d[slow].iloc[i]):
            #Buy signal
            signals.append(1)
        elif (d[fast].iloc[i-1] >= d[slow].iloc[i-1] and d[fast].iloc[i] < d[slow].iloc[i]):
            # Sell signal
            signals.append(-1)
        else:
            # Hold 
            signals.append(0)
    return signals

            

