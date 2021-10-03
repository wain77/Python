# def alphabet_position(text):
#     alpha = [chr(x) for x in range(97,123)]
#     return ' '.join([str(i) for i in [alpha.index(char) + 1 for char in text.lower() if char in alpha]])

# print(alphabet_position("The sunset sets at twelve o' clock."))

# def is_isogram(string):
#     print(string)
#     print(bool(string))
#     if string:
#         print(any([char.isdigit() for char in string]))
#         if any([char.isdigit() for char in string]):
#             return False
#         for c in string.lower():
#             print(c)
#             print(string.lower().count(c))
#             if string.lower().count(c) > 1:
#                 return False
#     return True

# print(is_isogram(""))

# def move_zeros(array):
#     return [e for e in array if isinstance(e, bool) or e != 0] + [0 for z in array if not isinstance(z, bool) and z == 0]

# print(move_zeros(["a",0.0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))

# def decodeMorse(morse_code):
#     morseList = morse_code.split('   ')
#     human_readable = [MORSE_CODE[char] for char in morseList.split(' ')]
#     return human_readable

# from math import sqrt

# def find_nb(m):
#     root = sqrt(m)
#     sum = 0
#     if int(root + 0.5) ** 2 == m:
#         intRoot = int(root)
#         for n in range(1, intRoot+1):
#             sum += n
#             if sum == intRoot:
#                 return n
#     else:
#         return -1

# print(find_nb(64))

# def high(x):
#     words = x.split()
#     allWordScores = [sum([ord(char) - 96 for char in word]) for word in words]
#     return words[allWordScores.index(max(allWordScores))]

# print(high('man i need a taxi up to ubud'))

# def expanded_form(num):
#     return ' + '.join([str(digit) for digit in [(int(d) * (10 ** (len(str(num)) - str(num).index(d)))) for d in str(num)] if digit != 0])

# print(expanded_form(70302))

def isOverlapping(list1, list2):
    if list2[0] < list1[1]:
        return True
    else:
        return False

def buildIntervalList(initIntervals):
    truthyList = [isOverlapping(initIntervals[i-1], initIntervals[i]) for i in range(1,len(initIntervals))]
        

def sum_of_intervals(intervals):
    intervals = sorted([list(x) for x in intervals])
    for i in range(1,len(intervals)):
        if 
    return sum([j[1] - j[0] for j in intervals])

print(sum_of_intervals([
   (1,4), (3,5)
]))