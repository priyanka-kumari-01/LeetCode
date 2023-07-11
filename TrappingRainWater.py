from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
      if not height or len(height) < 3:
        return 0

      n = len(height)
      left_max = [0] * n
      right_max = [0] * n

      left_max[0] = height[0]
      for i in range(1, n):
          left_max[i] = max(left_max[i - 1], height[i])

      right_max[n - 1] = height[n - 1]
      for i in range(n - 2, -1, -1):
          right_max[i] = max(right_max[i + 1], height[i])

      trapped_water = 0
      for i in range(n):
          trapped_water += min(left_max[i], right_max[i]) - height[i]

      return trapped_water

elevation_map = [0, 1, 0, 2] #, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution.trap(1, elevation_map))