class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftMin = prices[0]
        ans = 0
        for price in prices:
            ans = max(ans, price-leftMin)
            leftMin = min(leftMin, price)

        return ans