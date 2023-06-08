#The K Weakest Rows in a Matrix: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = []
        # Iterate over each row in the matrix
        for i, row in enumerate(mat):
            # Count the number of soldiers in the current row
            count = sum(row)
            # Store the count and row index as a tuple in the counts list
            counts.append((count, i))

        # Sort the counts list based on the number of soldiers in each row
        counts.sort()
        
        # Extract the indices of the k weakest rows
        weakest = [index for _, index in counts[:k]]

        return weakest


# Create the matrix
mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3

# Create an instance of the Solution class
solution = Solution()

# Find the k weakest rows
weakest = solution.kWeakestRows(mat, k)

# Print the indices of the k weakest rows
print(weakest)
