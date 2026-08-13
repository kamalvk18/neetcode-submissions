class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 1)
        def helper(i):
            if i == len(s):
                return 1

            #take 1 digit
            if i > len(s) or s[i] == '0':
                return 0

            if memo[i] != -1:
                return memo[i]

            pick1 = helper(i+1)

            #take 2 digits
            pick2 = 0
            if s[i:i+2] <= '26':
                pick2 = helper(i+2)

            memo[i] = pick1 + pick2
            return memo[i]

        return helper(0)