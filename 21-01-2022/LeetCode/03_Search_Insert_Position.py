"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target < nums[i] and target not in nums:
                return i
            elif target > nums[i] and target not in nums and i == len(nums) - 1:
                return i + 1


a = Solution()
print(a.searchInsert([1, 3, 5, 6], 7))
