from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_reachable = nums[0]  # Maximum index reachable in the current jump
        next_max_reachable = nums[0]  # Maximum index reachable in the next jump
        jumps = 1  # Number of jumps

        for i in range(1, n):
            # If the current index is beyond the maximum reachable index in the current jump
            if i > max_reachable:
                jumps += 1
                max_reachable = next_max_reachable

            # Update the maximum index reachable in the next jump
            next_max_reachable = max(next_max_reachable, i + nums[i])

        return jumps


# Example usage:
nums = [2,3,1,1,4]
result = Solution.jump(1, nums)
print(result)