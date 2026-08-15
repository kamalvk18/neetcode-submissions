class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        prices = [INF] * n
        prices[src] = 0

        tmpPrices = prices.copy()

        for i in range(k+1):
            for u, v, c in flights:
                if prices[u] + c < tmpPrices[v]:
                    tmpPrices[v] = prices[u] + c
            prices = tmpPrices.copy()

        res = prices[dst]
        return res if res != INF else -1