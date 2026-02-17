class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        termine = False

        while not termine :
            if val in nums:
                nums.remove(val)
            else:
                termine=True
        
        return len(nums)