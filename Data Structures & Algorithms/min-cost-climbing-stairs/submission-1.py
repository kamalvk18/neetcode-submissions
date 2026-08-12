class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n+1)
        def helper(i):
            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(helper(i+1), helper(i+2))
            return memo[i]

        return min(helper(0), helper(1))