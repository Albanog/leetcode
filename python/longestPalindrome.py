class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_pos_actual = 0
        longest_pal_substr = 0
        aux_longest_pal_substr= 0
        substring_start = 0
        dic = {}
        
        for char in s:
            list_seen = dic.get(char)
            if list_seen !=None :  
                for pos_seen in dic[char]:
                    right = char_pos_actual
                    left = pos_seen
                    palindrome = True
                    if (right - left) >= longest_pal_substr :
                        while (palindrome) and (left < right):
                            if (s[left] != s[right]):
                                palindrome = False
                            left+=1
                            right-=1
                        if palindrome == True :
                            aux_longest_pal_substr = char_pos_actual - pos_seen + 1
                            if (aux_longest_pal_substr > longest_pal_substr) :
                                longest_pal_substr = aux_longest_pal_substr
                                substring_start = pos_seen
                            break
            else:
                dic[char] = []

            dic[char].append(char_pos_actual)
            char_pos_actual+=1
        
        if (substring_start == longest_pal_substr ) :
            return s[0]     
        return s[substring_start:substring_start + longest_pal_substr]