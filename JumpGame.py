from typing import List

class Solution:
    def canJump(nums):
      max_reachable = 0  # Maximum reachable index
      length = len(nums)

      for i in range(length):
          # If the current index is beyond the maximum reachable index
          if i > max_reachable:
              return False

          # Update the maximum reachable index
          max_reachable = max(max_reachable, i + nums[i])

          # If the last index is reachable, return True
          if max_reachable >= length - 1:
              return True

      return False  # If the last index is not reachable

# Example usage:
nums = [2,3,1,1,4]
result = Solution.canJump(nums)
print(result)

nums = [3, 2, 1, 0, 4]
result = Solution.canJump(nums)
print(result) 