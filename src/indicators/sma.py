from collections import deque
from data_processes.load_data import load_data
def sma(price_column, period, data):
    prices = data[price_column]

    priceQ = deque()
    sma_values = []
    running_sum = 0

    for i in range(len(prices)):
        price = prices.iloc[i]

        priceQ.append(price)
        running_sum += price

        if len(priceQ) > period:
            running_sum -= priceQ.popleft()

        if len(priceQ) < period:
            sma_values.append(None)
        else:
            sma_values.append(running_sum / period)

    return sma_values
