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
        # while i < len(nums):
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             result[0] = i
        #             result[1] = j
        #             return result
        #         j += 1
        #     i += 1
        #     j = i + 1

        return result