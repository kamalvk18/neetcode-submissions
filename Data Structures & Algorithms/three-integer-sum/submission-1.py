class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                tsum = nums[i] + nums[j] + nums[k]
                if tsum == 0:
                    triplet = (nums[i], nums[j], nums[k])
                    triplets.add(triplet)
                    j+=1
                    k-=1
                elif tsum > 0:
                    k-=1
                else:
                    j+=1

        return list(triplets)