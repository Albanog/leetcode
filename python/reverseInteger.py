class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new=0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        esNegativo = False
        if x<0:
            esNegativo = True
            x = -x

        while x != 0 :
            new = new * 10
            new = new +  (x % 10)
            x = x // 10

        if new < INT_MIN or new > INT_MAX:
            return 0

        if esNegativo:
            return -new
        
        return new
