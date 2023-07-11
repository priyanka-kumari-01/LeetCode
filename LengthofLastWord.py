class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      # Trim the string
      s = s.strip()

      # Split the string by spaces
      words = s.split()

      # Check if the array of words is empty
      if not words:
          return 0

      # Retrieve the last word and return its length
      last_word = words[-1]
      return len(last_word)


s = "luffy is still joyboy"
Solution.lengthOfLastWord(1, s)