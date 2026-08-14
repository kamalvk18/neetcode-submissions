class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                skip = dp[i+1][j]
                pick = 0
                if j >= coins[i]:
                    pick = dp[i][j-coins[i]]
                dp[i][j] = pick + skip

        return dp[0][amount]