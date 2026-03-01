class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        pos = right//2

        if right == -1 :
            return -1
        

        while left <= right:

            pos = (left + right) //2

            if nums[left] == target: 
                return left
            if nums[right] == target: 
                return right
            if nums[pos] == target: 
                return pos    

            if nums[pos] > nums[left]:
                if nums[pos]> target > nums[left]:
                    right = pos -1
          
                else:
                    left = pos +1
                
            else:
                if nums[pos] < target < nums[right]:
                    left = pos +1
                else:
                    right = pos -1
                
        return -1
                
