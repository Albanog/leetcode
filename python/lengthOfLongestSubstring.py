class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_pos = 0
        longest_substring = 0
        aux_longest_substring = 0
        substring_start = 0
        dic = {}
        
        for char in s:
            last_seen = dic.get(char)
        
            if (last_seen!=None) and (last_seen >= substring_start):
                substring_start = last_seen + 1
                aux_longest_substring = char_pos - substring_start + 1
            else:
                aux_longest_substring+=1

            dic[char] = char_pos
            char_pos+=1
            if aux_longest_substring>longest_substring:
                longest_substring = aux_longest_substring
               
        return longest_substring
