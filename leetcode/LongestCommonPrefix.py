import re

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs:
            s = min(strs)
            for i in range(len(s)):
                if len([x for x in strs if re.search(f'^{s}', x)]) == len(strs):
                    return s
                s = s[:-1]
        return ""


inputLists = [["flowers", "flow", "flight"],
              ["c", "acc", "ccc"],
              ["a"],
              ["a","b"],
              []]
              
for thisList in inputLists:
    print(Solution().longestCommonPrefix(thisList))
