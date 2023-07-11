
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        curr_tank = 0
        start_station = 0

        for i in range(n):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]

            if curr_tank < 0:
                curr_tank = 0
                start_station = i + 1

        if total_tank < 0:
            return -1
        else:
            return start_station

# Create an instance of the Solution class
solution = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

# Example usage:
result = solution.canCompleteCircuit(gas,cost)
print(result)