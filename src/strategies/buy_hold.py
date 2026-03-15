def buy_hold(bankroll, d):
    #Shares bought initially
    shares = bankroll / d['Close'].iloc[0]
    #Final value of shares after the 5 year period
    terminal_value = shares * d['Close'].iloc[-1]
    profit = terminal_value - bankroll 
    return f'Proft: {profit:.2f}'