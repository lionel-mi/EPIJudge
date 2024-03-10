from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    buying_price = prices[0]
    profit = 0
    for price in prices[1:]:
        if price >= buying_price:
            profit = max(profit, price - buying_price)
        else:
            buying_price = price
    return profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_06_buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
