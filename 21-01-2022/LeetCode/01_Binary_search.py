"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.
"""


class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif i == len(nums) - 1:
                return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
