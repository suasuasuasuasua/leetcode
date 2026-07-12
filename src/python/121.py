class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_idx = 0
        sell_idx = buy_idx + 1
        profit = 0

        # iterate while the sell index (right bound of the sliding window)
        # is within the bounds of the prices
        #
        # the reason why we stop like this is because we cannot get a bigger profit by advancing
        # the start of the sliding window; we've already established a running maximum
        while sell_idx < len(prices):
            buy_price = prices[buy_idx]
            sell_price = prices[sell_idx]

            # record the running profit
            if buy_price <= sell_price:
                profit = max(profit, prices[sell_idx] - buy_price)
                sell_idx += 1
            # stop and reset the sliding window
            else:
                buy_idx = sell_idx
                sell_idx = buy_idx + 1

        return profit
