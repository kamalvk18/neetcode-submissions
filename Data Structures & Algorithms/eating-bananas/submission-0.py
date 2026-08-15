class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def check(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
                if hours > h:
                    return False

            return True

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return r