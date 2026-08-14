class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        pac = set()
        atl = set()

        def dfs(i, j, vis, prevVal):
            if (
                i < 0 or j < 0 or
                i == r or j == c or
                (i, j) in vis or
                heights[i][j] < prevVal
            ):
                return

            vis.add((i, j))

            dfs(i+1, j, vis, heights[i][j])
            dfs(i, j+1, vis, heights[i][j])
            dfs(i-1, j, vis, heights[i][j])
            dfs(i, j-1, vis, heights[i][j])


        for i in range(c):
            dfs(0, i, pac, heights[0][i])
            dfs(r-1, i, atl, heights[r-1][i])

        for i in range(r):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, c-1, atl, heights[i][c-1])

        res = []
        for node in pac:
            if node in atl:
                res.append(node)

        return res