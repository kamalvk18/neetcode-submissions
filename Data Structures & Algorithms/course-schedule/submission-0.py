class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        vis = set()
        def dfs(i):
            if i in vis:
                return False
            
            if graph[i] == []:
                return True
                
            vis.add(i)
            for v in graph[i]:
                if not dfs(v):
                    return False

            vis.remove(i)
            graph[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True