class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = strs[0]
        cant_palabras = len(strs)
        cant_common_preffix = len(output)
        
        if cant_palabras == 1:
            return output
        
        i = 0
        while i < cant_palabras-1 and cant_common_preffix > 0 :

            j=0
            proxima_palabra = strs[i+1]
            while j < min(cant_common_preffix, len(proxima_palabra)) :

                if output[j] != proxima_palabra[j]:
                    break
                j+=1
            cant_common_preffix = j
            output = output[:cant_common_preffix]
            i += 1

        return output
        


