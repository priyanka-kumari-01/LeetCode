#FizzBuzz: https://leetcode.com/problems/fizz-buzz/description/

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Create an empty list to store the values
        value =[]
        # Iterate from 1 to n (inclusive)
        for i in range(1, n+1):
            # Check if the number is divisible by both 3 and 5
            if i%3 == 0 and i%5 == 0:
                value.append("FizzBuzz")
            # Check if the number is divisible by 5    
            elif i%5 == 0:
                value.append("Buzz")
            # Check if the number is divisible by 3    
            elif i%3 == 0:
                value.append("Fizz") 
            # If the number is not divisible by 3 or 5, append the number itself as a string      
            else:
                value.append(str(i))  
        return value        

Solution.fizzBuzz(1, 15)  