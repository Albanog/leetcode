class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        digitos = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            " ": 10,
            "-": -1,
            "+": 11
        }

        encontre_ini = False
        resp = 0
        negativ = False
        i = 0
        while i < len(s) :
            valor = digitos.get(s[i])
            if (valor is None):
                return resp
            if valor != 10:
                encontre_ini=True
                if valor == -1:
                    negativ = True
                else:
                    if valor != 11:
                        resp = valor
                i+=1
                break
            i+=1
    
        if not encontre_ini:
            return resp

        
        while i < len(s) :
            valor = digitos.get(s[i])
            if (valor is None):
                if negativ:
                    return -resp
                return resp
            if valor in (-1, 10, 11):
                if negativ:
                    return -resp
                return resp
            else:
                if resp > (INT_MAX - valor) // 10:
                    return INT_MIN if negativ else INT_MAX
                resp = resp * 10 + valor

            i+=1


        if negativ:
            return -resp
        return resp
                