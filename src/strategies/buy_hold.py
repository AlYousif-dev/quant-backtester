def buy_hold(bankroll, d):
    shares = bankroll / d['Close'].iloc[0]
    terminal_value = shares * d['Close'].iloc[-1]
    profit = terminal_value - bankroll  # <--- Change this line
    return profit