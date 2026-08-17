class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if max_jump < i:
                return False
                
            max_jump = max(max_jump, i + num)
            if max_jump >= n-1:
                return True

        return False