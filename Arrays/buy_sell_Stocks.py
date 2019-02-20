#__author__ = ritvikareddy2
#__date__ = 2019-02-16

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = float("inf")
    minIdx = -1
    maxIdx = -1
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            minIdx = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            maxIdx = i

    return max_profit