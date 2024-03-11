from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:

    profits = [0] * len(prices)
    buying_price = prices[0]
    for idx, price in enumerate(prices[1:], 1):
        if price < buying_price:
            buying_price = price
        profits[idx] = max(profits[idx-1], price - buying_price)

    selling_price = prices[-1]
    max_profit = max(profits)
    for idx in range(len(prices)-2, 0, -1):
        price = prices[idx]
        if price > selling_price:
            selling_price = price
        max_profit = max(max_profit, selling_price - price + profits[idx-1])
    return max_profit





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_07_buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
