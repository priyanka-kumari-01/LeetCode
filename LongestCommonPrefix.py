class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

strs = ["flower","flow","flight"]
Solution.longestCommonPrefix(1, strs)