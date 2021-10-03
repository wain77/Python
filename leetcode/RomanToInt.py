class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        valueDict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for i in range(0,-len(s),-1):
            if s[i] == 'I' and s[i-1] in ('V','X'):
                result += valueDict[s[i-1]] - valueDict[s[i]]
        return result

print(Solution().romanToInt('III'))
print(Solution().romanToInt('IV'))