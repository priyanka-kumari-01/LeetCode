#FizzBuzz: https://leetcode.com/problems/fizz-buzz/description/

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        value =[]
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                value.append("FizzBuzz")
            elif i%5 == 0:
                value.append("Buzz")
            elif i%3 == 0:
                value.append("Fizz")   
            else:
                value.append(str(i))  
        return value        

Solution.fizzBuzz(1, 15)  