class Solution:
    def reverseWords(self, s: str) -> str:
      s = s.split()
      result = ""
      for i in range(len(s)-1, -1, -1):
        result += s[i] + " "
      return result[:-1]


s = "the sky is blue"
Solution.reverseWords(1, s)