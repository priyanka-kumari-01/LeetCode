from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0

        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                h = n - i

        return h

# Example usage:
nums = [3,0,6,1,5]
result = Solution.hIndex(1, nums)
print(result)