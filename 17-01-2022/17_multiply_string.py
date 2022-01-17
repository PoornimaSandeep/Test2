"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
"""


class Solution(object):
    def multiply(self, num1, num2):
        mul = int(num1) * int(num2)
        return str(mul)


a = Solution()
print(a.multiply(123, 456))
