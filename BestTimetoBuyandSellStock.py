# 121. Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # If the prices list is empty, return 0
            return 0

        min_price = prices[0]  # Set the initial minimum price to the first element in the list
        max_profit = 0  # Set the initial maximum profit to 0

        for price in prices:
            # Update the minimum price if a smaller price is encountered
            min_price = min(min_price, price)  
            # Calculate the maximum profit by finding the difference between the current price and the minimum price
            max_profit = max(max_profit, price - min_price)  

        return max_profit  

nums = [7, 1, 5, 3, 6, 4]
Solution.maxProfit(1, nums) 