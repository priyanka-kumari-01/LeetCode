class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

haystack = "leetcode"
needle = "leeto"
# haystack = "sadbutsad"
# needle = "sad"
Solution.strStr(1, haystack, needle)