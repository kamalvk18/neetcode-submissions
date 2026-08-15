from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        heap = [(0, 0)]
        vis = set()
        while heap:
            cost, i = heappop(heap)
            if i in vis:
                continue
            res += cost
            vis.add(i)
            for dist, v in adj[i]:
                if v not in vis:
                    heappush(heap, (dist, v))

        return res
