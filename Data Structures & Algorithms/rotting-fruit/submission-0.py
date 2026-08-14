class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    nr = r + x
                    nc = c + y
                    if nr < 0 or nr >= n or nc < 0 or nc >=m:
                        continue
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            time += 1

        return time if fresh == 0 else -1