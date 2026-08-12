class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        memo = {}
        def helper(i, n):
            if i >= n:
                return 0

            if (i, n) in memo:
                return memo[(i, n)]

            rob = nums[i] + helper(i+2, n)
            skip = helper(i+1, n)

            memo[(i, n)] = max(rob, skip)
            return memo[(i, n)]

        return max(helper(0, n-1), helper(1, n))