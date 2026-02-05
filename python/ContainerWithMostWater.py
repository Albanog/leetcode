class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = -1
        left_piv = height[i]
        right_piv = height[j]
        
        l_len = len(height)
        area = min(left_piv, right_piv) * (l_len-1)

        while i < l_len +j -1 :
            if left_piv < right_piv :
                i+=1
                left_piv = height[i]
                if area < min(left_piv, right_piv) * (l_len+j-i) :
                    area = min(left_piv, right_piv) * (l_len+j-i)
            else:
                j-=1
                right_piv = height[j]
                if area < min(right_piv, left_piv) * (l_len+j-i) :
                    area = min(right_piv, left_piv) * (l_len+j-i)
    
        return area


            


