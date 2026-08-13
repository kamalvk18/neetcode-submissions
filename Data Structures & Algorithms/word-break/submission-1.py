from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        n = len(s)
        @cache
        def helper(ind):
            if ind == n:
                return True

            for i in range(ind, n):
                if s[ind: i+1] in word_dict:
                    if helper(i+1):
                        return True

            return False

        return helper(0)