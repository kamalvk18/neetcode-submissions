class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        dq = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)

        res = []
        while dq:
            node = dq.popleft()
            res.append(node)
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    dq.append(v)

        if len(res) == numCourses:
            return res
        else:
            return []