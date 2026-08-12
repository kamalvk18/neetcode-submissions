class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n+1)
        def helper(i):
            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            rob = nums[i] + helper(i+2)
            skip = helper(i+1)

            memo[i] = max(rob, skip)
            return memo[i]

        return helper(0)
