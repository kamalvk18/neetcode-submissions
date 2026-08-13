from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(i, curr_sum):
            if curr_sum == amount:
                return 0

            if curr_sum > amount:
                return float('inf')

            if i >= len(coins):
                return float('inf')

            # Pick current coin again if needed
            pick = 1 + helper(i, curr_sum + coins[i])

            # Skip current coin
            skip = helper(i + 1, curr_sum)

            return min(pick, skip)

        result = helper(0, 0)

        return result if result != float('inf') else -1