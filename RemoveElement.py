#27. Remove Element:https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
              # Swap the current element with the element at the end
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return left

nums = [0,1,2,2,2,2,2,2]
val = 2     

# Create Solution instance
Solution.removeElement(1,nums,val)