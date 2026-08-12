class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resLen = 0
        resIdx = -1
        for i in range(n):
            #odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

            #even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

        return s[resIdx: resIdx+resLen]