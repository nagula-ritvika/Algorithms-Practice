#__author__ = ritvikareddy2
#__date__ = 2019-02-18

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not len(prices):
        return 0
    curHigh = prices[0]
    curLow = prices[0]
    profit = 0
    i = 0
    # while i < len(prices) - 1:
    #     while i < len(prices) - 1 and prices[i] >= prices[i+1]:
    #         i += 1
    #     curLow = prices[i]
    #     while i < len(prices) - 1 and prices[i] <= prices[i+1]:
    #         i += 1
    #     curHigh = prices[i]
    #     profit += curHigh - curLow

    # or
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit





if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    print(maxProfit(a))
