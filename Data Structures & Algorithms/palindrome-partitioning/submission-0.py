class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(i, curr):
            if i == len(s):
                res.append(curr[:])
                return

            for j in range(i, len(s)):
                if s[i: j+1] == s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    helper(j+1, curr)
                    curr.pop()

        helper(0, [])
        return res