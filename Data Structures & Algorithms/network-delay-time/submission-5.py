from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        signal_time = [float('inf')] * n
        signal_time[k-1] = 0

        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        heap = []
        for node, weight in adj[k]:
            heappush(heap, (weight, node))

        while heap:
            wt, node = heappop(heap)
            if signal_time[node-1] > wt:
                signal_time[node-1] = wt
                for v, w in adj[node]:
                    if signal_time[v-1] > w + wt:
                        heappush(heap, (w + wt, v))

        res = max(signal_time)
        return res if res != float('inf') else -1