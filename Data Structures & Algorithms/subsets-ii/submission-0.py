class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, sub):
            res.append(sub[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                sub.append(nums[j])
                helper(j+1, sub)
                sub.pop()
        
        nums.sort()
        helper(0, [])

        return res