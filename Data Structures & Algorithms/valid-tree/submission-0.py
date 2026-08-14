class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = set()
        def dfs(i, pre):
            if i in vis:
                return False

            vis.add(i)
            for v in adj[i]:
                if v == pre:
                    continue
                    
                if not dfs(v, i):
                    return False

            return True

        if dfs(0, -1) and len(vis) == n:
            return True
        else:
            return False