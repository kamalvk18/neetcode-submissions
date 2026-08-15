class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        signal_time = [float('inf')] * n

        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        def dfs(i, time):
            if time >= signal_time[i-1]:
                return

            signal_time[i-1] = time
            for v, t in adj[i]:
                dfs(v, time + t)
            

        dfs(k, 0)

        max_time = max(signal_time)
        if max_time == float('inf'):
            return -1
        else:
            return max_time