from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            skip = dfs(i+1, buying)
            if buying:
                buy = -prices[i] + dfs(i+1, not buying)
                res = max(buy, skip)
            else:
                sell = prices[i] + dfs(i+2, not buying)
                res = max(sell, skip)

            return res

        return dfs(0, True)