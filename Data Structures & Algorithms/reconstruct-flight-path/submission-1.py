from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in tickets:
            heappush(adj[src], dst)

        result = []

        def dfs(node):
            while adj[node]:
                nxt = heappop(adj[node])
                dfs(nxt)

            result.append(node)

        dfs("JFK")

        return result[::-1]