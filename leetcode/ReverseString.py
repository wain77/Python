class Solution:
    def reverse(self, x: int) -> int:
        lim = 2**31
        k = 1 if x > 0 else -1
        a = int(str(abs(x))[::-1]) * k
        return a if a in range(-lim,lim-1) else 0


""" class Solution(object):
    def reverse(self, x):
        '''
        :type x: int
        :rtype: int
        '''
        if x < 0:
            return 0 if int(str(abs(x))[::-1]) * -1 < 2**31 else int(str(abs(x))[::-1]) * -1
        else:
            return 0 if int(str(x)[::-1]) >= 2**31 else int(str(x)[::-1]) """
