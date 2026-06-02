from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        total_ways = 0
        if n >= 1:
            total_ways += self.climbStairs(n-1)
        if n >= 2: 
            total_ways += self.climbStairs(n-2)

        return total_ways