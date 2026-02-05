class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_list = {
            1  :  "I",
            4  :  "IV",
            5  :  "V",
            9  :  "IX",
            10 :  "X",
            40 :  "XL",
            50 :  "L",
            90 :  "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }

        roman = ""
        decimal = 0
        termine = False

        while decimal < 4 and not termine:
            
            ultimo = (num % 10) * (10 ** decimal)
            num = (num//10)

            termine_decimal = False

            while not termine_decimal :
                roman_aux = roman_list.get(ultimo)
                if roman_aux is not None :
                    roman = roman_aux + roman
                    termine_decimal = True
                else:
                    if ultimo == 0 :
                        termine_decimal = True
                    else:
                        roman = roman_list.get(10 ** decimal) + roman
                        ultimo -= 10 ** decimal
             
            if num == 0:
                termine = True
            
            decimal +=1

        return roman


        