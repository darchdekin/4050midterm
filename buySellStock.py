def maxProfit(prices):
    n = len(prices)
    optimalProfit = [None] * n # optimalProfit[i] stores the maximum profit you can make using the subset of days i to n.
    highestPrice = [None] * n # highestPrice[i] stores the highest price that occurs in the subset of days i to n.
    highestPrice[n-1] = prices[n-1]
    optimalProfit[n-1] = 0 # if you buy and sell on the last day, you will make 0 profit.
    for i in range(n - 2, -1, -1):
        highestPrice[i] = max(prices[i], highestPrice[i+1])
        optimalProfit[i] = max(highestPrice[i] - prices[i], optimalProfit[i+1])
    return optimalProfit[0]