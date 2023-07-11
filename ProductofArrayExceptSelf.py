
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        # Calculate the product of all elements to the left of nums[i]
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Calculate the product of all elements to the right of nums[i]
        right_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_prod
            right_prod *= nums[i]

        return answer

# Create an instance of the Solution class
solution = Solution()

# Example usage:
nums = [1,2,3,4]
result = solution.productExceptSelf(nums)
print(result)