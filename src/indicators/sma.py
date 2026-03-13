from collections import deque
from load_data import load_data
def sma(price_column,period,d):
    data = d
    priceQ = deque()
    sma = []
    running_sum = 0
    for i in range(len(data)):
        price = data[price_column].iloc[i]
        priceQ.append(price)
        running_sum += price
        if(len(priceQ) > period):
            running_sum -= priceQ.popleft()
        if(len(priceQ) < period):
            sma.append(None)
        else:
            sma.append(running_sum/period)
    return(sma)

