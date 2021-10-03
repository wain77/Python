from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = {'(':1, ')':-1, '[':2, ']':-2, '{':3, '}':-3}
        count = Counter(s)
        total = 0
        for i in count:
            total += count[i] * bracketDict[i]
        
        if not total:
            return True
        return False

testInput = [['(',')'],
             ['(',')','{','}','[',']'],
             ['(','{','[',']','}',')'],
             ['(',']'],
             ['(','{',')','}']]

for testList in testInput:
    print(Solution().isValid(testList))