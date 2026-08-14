class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(i, j):
            dq = deque([(i, j)])
            grid[i][j] = '0'

            while dq:
                x, y = dq.popleft()
                for dx, dy in directions:
                    nr, nc = x + dx, y + dy
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == '0'):
                        continue
                    dq.append((nr, nc))
                    grid[nr][nc] = '0'


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)

        return islands