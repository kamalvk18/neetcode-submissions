from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        n = len(nums)
        half_sum = total_sum // 2

        @cache
        def helper(i, curr_sum):
            if curr_sum == half_sum:
                return True

            if i == n:
                return False

            pick = helper(i+1, curr_sum + nums[i])
            skip = helper(i+1, curr_sum)

            if pick or skip:
                return True

            return False

        return helper(0, 0)