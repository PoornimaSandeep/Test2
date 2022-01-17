"""
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

str="abcabcbb"

res=[str[i:j] for i in range(len(str)) for j in range(i+1,len(str)-1)]
print(res)






