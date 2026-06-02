class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        if n == 2:
            return 1
            
        curr = 1
        prev = 1
        prev2 = 0

        for i in range(3, n+1):
            next_num = curr + prev + prev2
            prev2 = prev
            prev = curr
            curr = next_num

        return curr