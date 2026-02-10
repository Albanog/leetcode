class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        total = len(digits)
        output = []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def conversor(i, convertido, output):
            
            if i == total-1:
                for char in dic.get(digits[i]):
                    aux = convertido + char
                    output.append(aux)
                return output
            
            for char in dic.get(digits[i]):
                aux = convertido + char
                conversor(i+1, aux, output)
            
            return output

        return conversor(0,"", output)


