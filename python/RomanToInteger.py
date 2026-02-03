class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        length = len(s)

        resp = 0

        for i in range(length):
            curr = s[i]
            num = roman.get(curr)
            if curr == "I":
                if i<length-1:
                    if s[i+1] == "V" or s[i+1] == "X":
                        num = -num
            elif curr == "X":
                if i<length-1:
                    if s[i+1] == "L" or s[i+1] == "C":
                        num = -num
            elif curr == "C":
                if i<length-1:
                    if s[i+1] == "D" or s[i+1] == "M":
                        num = -num
            resp += num
        
        return resp