# 122. Best Time to Buy and Sell Stock II :https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def maxProfitII(self, prices: List[int]) -> int:
        # Initialize the variable to store the maximum profit
        max_profit = 0

        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the current price is higher than the previous price
            if prices[i] > prices[i-1]:
                # Add the difference between the current and previous prices to the max_profit
                max_profit += prices[i] - prices[i-1]

        # Return the maximum profit
        return max_profit

# Create an instance of the Solution class
solution = Solution()

# Example usage:
prices = [7,1,5,3,6,4]
result = solution.maxProfitII(prices)
print(result)
