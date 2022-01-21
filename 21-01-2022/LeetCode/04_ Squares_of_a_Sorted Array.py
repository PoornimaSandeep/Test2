"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution(object):
    def sortedSquares(self, nums):
        res = []
        for i in nums:
            r = i * i
            res.append(r)
        return sorted(res)


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
