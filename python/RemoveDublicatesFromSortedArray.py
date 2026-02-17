class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        newList = [nums[0]]
        for i in range(len(nums)):
            if nums[i] != newList[-1]:
                newList.append(nums[i])

        for j in range(len(newList)):
            nums[j] = newList[j]
        
        return len(newList)
        
