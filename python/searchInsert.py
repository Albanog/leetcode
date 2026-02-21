class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def rec(left, right):
            if left > right:
                return left

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return rec(mid + 1, right)
            else:
                return rec(left, mid - 1)

        return rec(0, len(nums) - 1)
