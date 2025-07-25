# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # problem
        # the problem is to choose a day to buy a stock (low) and sell that
        # stock in the future (high)
        #
        # constraints
        # if there is no way to achieve profit, then return 0
        #
        # example
        # input: prices = [7,1,5,3,6,4]
        # output: 5
        # input: prices = [2,4,1]
        # output: 2
        # input: prices = [3,2,6,5,0,3]
        # output: 4

        # assume that the first number is the smallest and largest
        # NOTE: this should effectively skip the first loop
        buy_idx = sell_idx = 0
        profit = 0
        # loop through each of the prices
        for i, num in enumerate(prices):
            # if the current price is less than the current buy, then reset
            # both the indices to this day
            if num < prices[buy_idx]:
                buy_idx = sell_idx = i
            # otherwise if the current price is greater, only reset the sell
            # price
            elif num > prices[sell_idx]:
                sell_idx = i

            # compute the difference and only update the profit if
            # 1. you sell later than you buy (duh)
            # 2. the new difference is larger
            diff = prices[sell_idx] - prices[buy_idx]
            if sell_idx > buy_idx:
                profit = max(profit, diff)  # easy way to get bigger value

        return profit
