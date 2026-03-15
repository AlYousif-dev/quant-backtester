def run_backtest(data,signals,cash):
    initial = cash
    trades = 0
    position = 0
    close = data['Close']
    shares = 0
    for i in range(len(signals)):
        if (signals[i] == 1 and position == 0):
            position = 1
            shares = cash / close.iloc[i]
            cash = 0
            trades += 1
        elif (signals[i] == -1 and position == 1):
            position = 0
            cash = shares * close.iloc[i]
            shares = 0 
            trades += 1 
    if position == 1:
        cash = shares * close.iloc[-1]
        trades += 1
    return cash - initial
