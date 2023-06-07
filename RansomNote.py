#Ransom Note: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to store the frequencies of characters in the magazine string
        magazine_freq = {}
        
        # Count the frequencies of characters in the magazine string
        for char in magazine:
            if char in magazine_freq:
                magazine_freq[char] += 1
            else:
                magazine_freq[char] = 1
        
        # Check if we can construct the ransomNote from the characters in the magazine
        for char in ransomNote:
            if char not in magazine_freq or magazine_freq[char] == 0:
                return False
            magazine_freq[char] -= 1
        
        return True       


ransomNote = "aa"
magazine = "aab"
# Create Solution instance
print(Solution.canConstruct(1, ransomNote, magazine))
