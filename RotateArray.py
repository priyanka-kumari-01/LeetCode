#189. Rotate Array:  https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Calculate the effective rotation index
        k = k % len(nums)

        # Reverse the entire array
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])

        # Print the modified array (optional)
        print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

Solution.rotate(1, nums, k)