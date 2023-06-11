#26. Remove Duplicates from Sorted Array: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i = 0
      for j in range(1, len(nums)):
          # If the current element is different from the previous element
          if nums[j] != nums[i]:
              i += 1
              # Move the unique element to the next position
              nums[i] = nums[j]
      
      return i + 1

nums = [1,1,2]
# Create Solution instance
Solution.removeDuplicates(1, nums)