"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


class Solution(object):
    def searchRange(self, nums, target):
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
               res.append(i)
        if res==[]:
           return [-1,-1]
        else:
            return res
a=Solution()
print(a.searchRange([],1))
