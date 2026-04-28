class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        difference = 0
        for i in range(len(prices)):
            z = i+1
            while z < len(prices):
                if prices[z] - prices [i] > difference:
                    difference = prices[z] - prices[i]
                z += 1
        return difference