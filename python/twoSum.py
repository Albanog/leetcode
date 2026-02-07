class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = 1
        result = [0, 0]

        explorados = {}
        while i < len(nums):
            if explorados.get(target - nums[i]) != None:
                return [i, explorados.get(target - nums[i])]

            if explorados.get(nums[i]) == None:
                explorados[nums[i]]=i
            
            i += 1
        

        return result