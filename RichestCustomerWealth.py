#Richest Customer Wealth: https://leetcode.com/problems/richest-customer-wealth/

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize the variable to keep track of the maximum wealth
        maxVal = 0
        
        # Iterate over each customer's account
        for i in range(len(accounts)):
          
            # Calculate the wealth of the current customer
            wealth = sum(accounts[i])
            
            # Update the maximum wealth if the current wealth is higher
            maxVal = max(maxVal, wealth)
        
        # Return the maximum wealth
        return maxVal

# Example usage
accounts = [[1, 5], [7, 3], [3, 5]]
solution = Solution()
print(solution.maximumWealth(accounts))  