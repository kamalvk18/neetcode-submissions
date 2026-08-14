from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, rem_amount):
            if rem_amount == 0:
                return 1

            if i >= len(coins):
                return 0

            skip = dfs(i+1, rem_amount)
            pick = 0
            if rem_amount >= coins[i]:
                pick = dfs(i, rem_amount - coins[i])

            return pick + skip

        return dfs(0, amount)
