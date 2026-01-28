class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        Output = ""
        len_str = len(s)
        cycle = 2 * numRows - 2

        for row in range(numRows):
            j = row
            while j in range(len_str):
                Output += s[j]
                gap = cycle - 2 * row

                if row != 0 and row != numRows - 1 and j + gap < len_str:
                    Output += s[j + gap]
                j+=cycle

        return Output