"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
l1=[2,4,3]
l2=[5,6,4]

str1=""
str2=""
for i in l1:
    str1 +=str(i)
for i in l2:
    str2 +=str(i)

res=int(str1)+int(str2)

print(res)