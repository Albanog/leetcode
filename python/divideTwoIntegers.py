class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if divisor < 1 and divisor > -1:
            raise ZeroDivisionError()
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign =1


        if dividend<0 and divisor>0 :
            dividend = -dividend
            sign = -1
        
        elif dividend>0 and divisor<0:
            divisor = -divisor
            sign = -1
 
        elif dividend<0 and divisor<0:
            divisor = -divisor
            dividend = -dividend

        n = 0
       
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            n += multiple

        if sign == -1:
            return -n
        return n

        
        