#Roman to Integer: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        # Define a dictionary mapping Roman numerals to their corresponding integer values
        romanInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Initialize the total sum and the previous value
        total = 0
        prev_value = 0
        
        # Iterate through each character in the input string
        for i in s:
            # Get the integer value of the current Roman numeral
            curr_value = romanInt[i]

            # Check if the current value is greater than the previous value
            if curr_value > prev_value:
                # If it is, subtract twice the previous value and add the current value to the total
                total += curr_value - 2 * prev_value
            else:
                # Otherwise, simply add the current value to the total
                total += curr_value
            # Update the previous value to the current value for the next iteration    
            prev_value = curr_value
        print(total)    
        return total 
    
Solution.romanToInt(1,"MCMXCIV")    