from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i

            if i == len(word1):
                return len(word2) - j

            res = float('inf')
            if word1[i] == word2[j]:
                match = dfs(i+1, j+1)
                res = min(res, match)
            else:
                insert = dfs(i, j+1)
                delete = dfs(i+1, j)
                replace = dfs(i+1, j+1)
                res = min(res, 1+(min(insert, delete, replace)))

            return res

        return dfs(0, 0)