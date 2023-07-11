from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Initialize candies for each child with 1

        # Traverse from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Traverse from right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        # Calculate the total minimum candies required
        total_candies = sum(candies)
        print(candies)
        return total_candies

# Example usage:
ratings = [1,2,2]#[1,0,2] #[1,2,3,4, 5, 4, 3, 2, 1]
minimum_candies = Solution.candy(1, ratings)
print("Minimum number of candies needed:", minimum_candies)