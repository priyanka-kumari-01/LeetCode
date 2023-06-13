# 80. Remove Duplicates from Sorted Array II: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        index = 2  # Start from the third element
        for i in range(2, len(nums)):
            # Check if the current element is different from the two elements before it
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1

        return index


nums = [0,0,1,1,1,1,2,3,3]     

# Create Solution instance
Solution.removeDuplicates(1, nums)