#169. Majority Element: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

nums = [2,2,1,1,1,2,2,3]

# Create Solution instance
Solution.majorityElement(1, nums)