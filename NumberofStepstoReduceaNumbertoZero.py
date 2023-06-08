#Number of Steps to Reduce a Number to Zero: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/ 

class Solution:
    def numberOfSteps(self, num: int) -> int:
      # Initialize a counter to keep track of the number of steps
      count = 0  
        
      # Continue the loop until num becomes zero
      while num != 0:
          if num % 2 == 0:  # If num is even
              num = num // 2  # Divide num by 2
          else:
              num -= 1  # If num is odd, subtract 1
          count += 1  # Increment the step counter
      
      return count  

print(Solution.numberOfSteps(1, 14))
