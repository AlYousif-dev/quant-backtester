def run_backtest(data, signals, cash):
    initial = cash
    trades = 0
    position = 0   # 0 = flat, 1 = long, -1 = short
    close = data['Close']
    shares = 0
    entry_price = 0

    for i in range(len(signals)):
        price = close.iloc[i]

        # BUY SIGNAL
        if signals[i] == 1:
            if position == 0:
                # enter long
                shares = cash / price
                entry_price = price
                cash = 0
                position = 1
                trades += 1

            elif position == -1:
                # close short first
                cash = shares * (entry_price - price + entry_price)
                
                # then go long
                shares = cash / price
                entry_price = price
                cash = 0
                position = 1
                trades += 1

        # SELL SIGNAL
        elif signals[i] == -1:
            if position == 0:
                # enter short
                shares = cash / price
                entry_price = price
                position = -1
                trades += 1

            elif position == 1:
                # close long first
                cash = shares * price
                
                # then go short
                shares = cash / price
                entry_price = price
                position = -1
                trades += 1

    # CLOSE ANY OPEN POSITION AT END
    final_price = close.iloc[-1]

    if position == 1:
        cash = shares * final_price
        trades += 1

    elif position == -1:
        cash = shares * (entry_price - final_price + entry_price)
        trades += 1
    profit = cash - initial
    return profit