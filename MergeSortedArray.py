#88. Merge Sorted Array: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      temp = len(nums1)-m

      # Loop through each element in nums2
      for i in range(0, len(nums2)):
          # Assign the last element of nums2 to nums1
          nums1[len(nums1)-temp] = nums2[n-1] 
          n-=1
          temp-=1

      # Sort nums1 in ascending order
      nums1.sort()    
      return nums1



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

# Create Solution instance
Solution.merge(1, nums1= nums1, m= m, nums2= nums2, n =n)