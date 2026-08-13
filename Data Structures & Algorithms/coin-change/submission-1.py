from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float('inf')

        dp = [[INF] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                skip = dp[i+1][j]

                pick = INF
                if coins[i] <= j:
                    pick = 1 + dp[i][j-coins[i]]

                dp[i][j] = min(pick, skip)

        ans = dp[0][amount]
        return ans if ans != INF else -1